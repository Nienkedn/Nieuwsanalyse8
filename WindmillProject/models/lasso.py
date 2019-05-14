from sklearn import linear_model
import re
import csv
import matplotlib.pyplot as plt

windmolencount = []
with open('../Data/tweets.csv', 'r', encoding='utf-16') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        windmolencount.append(len(re.findall('windmolen', row[2].lower())))
    print(windmolencount)
    file.seek(0)
    next(data)
    fit_data = []
    for i, row in enumerate(data):
        temp_array = []
        temp_array.append(int(row[1]))
        temp_array.append(len(row[2]))
        fit_data.append(temp_array)

# Decide on model and fit train data with targets
reg = linear_model.Lasso(alpha=0.05)
reg.fit(fit_data[:20], windmolencount[:20])

# Try to predict targets with new data
lasso = list(reg.predict(fit_data[20:50]))
print(lasso)
print("Avg:"+str(sum(lasso) / len(lasso)))
print(reg.coef_)
# Plot results
# x = []
# y = []
# for dot in fit_data[20:50]:
#     x.append(dot[0])
#     y.append(dot[1])
# plt.scatter(x, y)

plt.plot(lasso)
plt.show()
