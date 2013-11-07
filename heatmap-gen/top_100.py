import json

if __name__ == '__main__':
    json_data = open('../datasets/dj-mag-top-100.json')
    data = json.load(json_data)
    uniques = set()
    for x in range(1997, 2014):
        for name in data[str(x)]:
            uniques.add(name)

    uniques = sorted(list(uniques))

    for name in uniques:
        print(name)

    #Close file stream
    json_data.close()