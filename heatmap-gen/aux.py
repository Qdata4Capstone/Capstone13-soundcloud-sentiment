import heatmap_gen
import jso

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

if __name__ == '__main__':
    #target = open('URLs.txt', 'r')
    #lines = target.read().splitlines()
    #target.close()
    #
    #if not check_dups(lines):
    #     print 'All good'
    #     scrape_comments_flat(lines)
    pass