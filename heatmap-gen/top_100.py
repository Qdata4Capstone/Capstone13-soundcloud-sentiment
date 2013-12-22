import json
import cluster
from cluster import KMeansClustering
import colorsys
from math import fmod

def cluster_trajectories():
    json_data = open('static/datasets/dj-mag-top-100.json')
    data = json.load(json_data)
    uniques_djs = set()

    for year in range(1997, 2014):
        for name in data[str(year)]:
            uniques_djs.add(name)

    dj_vectors = []
    dj_vector_map = {}

    for dj in uniques_djs:
        trajectory = ()
        for year in range(1997, 2014):
            if dj in data[str(year)]:
                trajectory += (data[str(year)].index(dj),)
            else:
                trajectory += (-999,)
        dj_vectors.append(trajectory)
        dj_vector_map[trajectory] = dj

    cl = KMeansClustering(dj_vectors)
    clusters = cl.getclusters(10)

    dj_clusters = []
    for cluster in clusters:
        dj_group = []
        for vector in cluster:
            dj_group.append(dj_vector_map[vector])
        dj_clusters.append(dj_group)

    print json.dumps(dj_clusters)

    #Close file stream
    json_data.close()

if __name__ == '__main__':
    cluster_trajectories()