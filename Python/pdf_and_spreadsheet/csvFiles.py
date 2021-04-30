import csv
data=open('example.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
print(data_lines[0])

for line in data_lines[10][:5]:
    print(line)

