import json
import csv

if __name__ == '__main__':
    json_data = open('static/datasets/dj-mag-top-100.json')
    data = json.load(json_data)
    uniques = set()

    for year in range(1997, 2014):
        for name in data[str(year)]:
            uniques.add(name)


    print "[" + ",".join(uniques) + "]"
    print len(uniques)

    #Close file stream
    json_data.close()