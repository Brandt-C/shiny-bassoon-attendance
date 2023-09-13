import csv
from pathlib import Path
p = Path('.')
file_list = []
x = list(p.glob('*.csv'))
for entry in x:
    file_list.append(str(entry))
if 'sum.csv' in file_list:
    file_list.remove('sum.csv')
if 'output.csv' in file_list:
    file_list.remove('output.csv')
print(file_list)


# date_key = []
att_key = {}
for f in file_list:
    with open(f, 'r') as file:
        csvread = csv.reader(file)
        for row in csvread:
            # if row and (row[2][-2:] == 'AM' or row[2][-2:] == 'PM'):
            #     date_key.append(row[2][:5])
            if row and row[-1] == 'Yes':
                if row[0] not in att_key:
                    att_key[row[0]] = 1
                else:
                    att_key[row[0]] += 1
with open('output.csv', 'w', newline='') as f:
    fnames = ['name', 'days_att']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    for a in att_key:
        writer.writerow({'name': a, 'days_att' : att_key[a]})
