import json
from cluster import KMeansClustering

def cluster_trajectories():
    json_data = open('static/datasets/../heatmap-gen/static/datasets/dj-mag-top-100.json')
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

def get_trajectory(dj, data):
    years = []
    rank = []

    for year in range(1997, 2014):
        if dj in data[str(year)]:
            years.append(year)
            rank.append(data[str(year)].index(dj) + 1)

    return years, rank

def get_streak(years):
    if len(years) == 1:
        return 1

    best = 1
    current = 1
    for i in range(0, len(years) - 1):
        if years[i+1] == years[i] + 1:
            current += 1
            best = max(current, best)
        else:
            current = 0

    return best

def generate_stats():
    json_data = open('static/datasets/../heatmap-gen/static/datasets/dj-mag-top-100.json')
    data = json.load(json_data)

    uniques_djs = set()

    for year in range(1997, 2014):
        for name in data[str(year)]:
            uniques_djs.add(name)

    out = {}

    for dj in uniques_djs:
        dj_meta = {}
        years, ranks = get_trajectory(dj, data)
        points = []
        for i in range(0, len(years)):
            points.append([years[i], ranks[i]])
        dj_meta["data"] = points
        dj_meta["highest"] = min(ranks)
        dj_meta["first"] = ranks[0]
        dj_meta["spread"] = max(ranks) - min(ranks)
        dj_meta["num_consecutive"] = get_streak(years)

        out[dj] = dj_meta

    print json.dumps(out)

    #Close file stream
    json_data.close()

if __name__ == '__main__':
    generate_stats()