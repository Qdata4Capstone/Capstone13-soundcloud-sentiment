import json
import csv

if __name__ == '__main__':
    json_data = open('../datasets/dj-mag-top-100.json')
    data = json.load(json_data)
    table = []
    table.append(["Rank"])
    table[0].extend(range(1997, 2014))

    count = 1
    for rank in range(0, 100):
        table.append([rank + 1])
        for x in range(1997, 2014):
            table[count].append(data[str(x)][rank])
        count = count + 1

    fl = open('../datasets/dj-mag-top-100.csv', 'w')

    writer = csv.writer(fl)
    for values in table:
        writer.writerow(values)

    fl.close()

    #Close file stream
    json_data.close()