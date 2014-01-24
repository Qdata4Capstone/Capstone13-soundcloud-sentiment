import heatmap_gen
import json
import operator

def check_dups(file_contents):
    tracks = set()
    dupFound = False

    for line in file_contents:
        if line in tracks:
            print 'Duplicate: ' + line
            dupFound = True
        else:
            tracks.add(line)
    return dupFound

def scrape_comments_json(file_contents):
    out_list = []
    count = 1

    for url in file_contents:
        print 'Fetching comments for ' + str(count)
        comments = heatmap_gen.get_comments_from_url(url)
        for comment in comments:
            if hasattr(comment.obj, 'id'):
                out_list.append(parseFields(comment.obj))
            else:
                out_list.append(parseFields(comment))
        count += 1

    with open('comments.json', 'a') as outfile:
        json.dump(out_list, outfile, indent=2)

def scrape_comments_flat(file_contents):
    out_list = []
    count = 1

    for url in file_contents:
        print 'Fetching comments for ' + str(count)
        comments = heatmap_gen.get_comments_from_url(url)
        for comment in comments:
            if hasattr(comment.obj, 'id'):
                out_list.append(parseFields(comment.obj)['body'])
            else:
                out_list.append(parseFields(comment)['body'])
        count += 1

    with open('comments.txt', 'a') as outfile:
        for line in out_list:
            outfile.write(line.encode('utf8') + "\n")

def parseFields(comment):
    out = {'id': comment.id, 'timestamp': comment.timestamp, 'body': comment.body, 'track_id': comment.track_id}
    return out

def max_incoming(data):
    seen_djs = {}
    for dj in data:
        for played in dj['imports']:
            if not played in seen_djs:
                seen_djs[played] = 1
            else:
                seen_djs[played] += 1

    return max(seen_djs.iteritems(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    pass