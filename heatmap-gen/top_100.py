import json
import cluster
from cluster import KMeansClustering

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
    clusters = cl.getclusters(20)

    print clusters

    #Close file stream
    json_data.close()

if __name__ == '__main__':
    cluster_trajectories()