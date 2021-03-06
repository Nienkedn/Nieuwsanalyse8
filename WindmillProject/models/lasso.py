from sklearn import linear_model
import re
import csv
import datetime as dt

wordcount = []
zoekwoord = 'windmolen'

with open('../Data/data2.csv', 'r', encoding='utf-16') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        wordcount.append(len(re.findall(zoekwoord, row[2].lower())))

    print(wordcount)
    file.seek(0)
    next(data)
    fit_data = []
    for i, row in enumerate(data):
        temp_array = []
        temp_array.append(float(row[1]))
        temp_array.append(len(row[2]))
        temp_array.append(int(row[4]))
        temp_array.append(int(row[5]))
        temp_array.append(float(row[6]))
        temp_array.append(float(row[7]))

        fit_data.append(temp_array)

# Decide on model and fit train data with targets
reg = linear_model.Lasso(alpha=0.0001)
reg.fit(fit_data[:1000], wordcount[:1000])

# Try to predict targets with new data
lasso = list(reg.predict(fit_data[1001:2700]))

timestamps = []
for i in fit_data:
    time = dt.datetime.fromtimestamp(i[0])
    timestamps.append(time)

print(lasso)
print("Avg:"+str(sum(lasso) / len(lasso)))
print(f"Coefficients:\n{reg.coef_}")
print(f"Coefficients:\n{reg.sparse_coef_}")

# plt.xlabel('Timestamps')
# plt.ylabel('Number of times the word shows up')
# plt.title('Popularity of the word '+zoekwoord)
# plt.grid(True)
#
# y = []
# for dot in wordcount[1001:2700]:
#     y.append(dot)
# plt.scatter(timestamps[1001:2700], y, s=2)
#
# plt.plot(timestamps[1001:2700], lasso, linewidth=0.5)
# plt.show()
