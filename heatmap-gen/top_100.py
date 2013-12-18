import json
import csv


def cluster_trajectories():
    json_data = open('static/datasets/dj-mag-top-100.json')
    data = json.load(json_data)
    uniques_djs = set()

    for year in range(1997, 2014):
        for name in data[str(year)]:
            uniques_djs.add(name)

    dj_vectors = []

    for dj in uniques_djs:
        trajectory = ()
        for year in range(1997, 2014):
            if dj in data[str(year)]:
                trajectory += (data[str(year)].index(dj),)
            else:
                trajectory += (-999,)
        dj_vectors.append(trajectory)

    print dj_vectors

    #Close file stream
    json_data.close()

if __name__ == '__main__':
    cluster_trajectories()