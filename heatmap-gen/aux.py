import heatmap_gen
from pprint import pprint

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

def scrape_comments(file_contents):
    comments = heatmap_gen.getCommentsFromURL(file_contents[0])

    for comment in comments:
        if hasattr(comment.obj, 'id'):
            print comment.obj.id
        else:
            print comment.id

if __name__ == '__main__':
    target = open('URLs.txt', 'r')
    lines = target.read().splitlines()
    target.close()

    if not check_dups(lines):
        print 'All good'
        scrape_comments(lines)