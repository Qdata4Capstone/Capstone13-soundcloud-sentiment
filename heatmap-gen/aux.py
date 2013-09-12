def checkDups(file):
    target = open(file, 'r')
    lines = target.read().splitlines()
    target.close()

    tracks = set()

    for line in lines:
        if line in tracks:
            print 'Duplicate: ' + line
        else:
            tracks.add(line)

if __name__ == '__main__':
    checkDups('URLs.txt')
    print 'Check complete'