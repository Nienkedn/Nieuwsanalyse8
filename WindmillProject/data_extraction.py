import csv
with open('Data/tweets.csv', 'r', encoding='utf-16') as old_file:
    with open('Data/tweets_data.csv', 'w', encoding='utf-16') as new_file:
        old_rows = csv.reader(old_file)

        for old_row in old_rows:
            print(old_row)
            content = old_row[1]
            char_len = str(len(content))
            word_count = str(len(content.split()))
            old_row.append(char_len)
            old_row.append(word_count)

            new_file.writelines(",".join(old_row)+'\n')

