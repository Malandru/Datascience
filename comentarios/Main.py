from sys import argv

def write(file, text):
    file.write(text + '\n')

def readcomment(positive, negative, commentary):
    pcount, ncount = 0, 0
    wcount, wrdist = 0, -1
    # commentary = raw_input()
    commentary = commentary.split(' ')
    for word in commentary:
        word = word + '\n'
        if word in positive:
            pcount += 1
        elif word in negative:
            ncount +=1
        wcount += 1
        wrdist += 1
    return pcount, ncount, wcount

def main():
    fposw = open('positive-words.txt')
    fnegw = open('negative-words.txt')

    fpos = open('positive_comments.csv', 'w')
    fneg = open('negative_comments.csv', 'w')

    positive = fposw.readlines()
    negative = fnegw.readlines()

    # header = raw_input()
    # write(fpos, header)
    # write(fneg, header)

    try:
        while True:
            line = raw_input()
            pcount, ncount, wcount = readcomment(positive, negative, line)
            print pcount, ncount, wcount
            if pcount > ncount:
                write(fpos, line)
            else:
                write(fneg, line)
    except EOFError:
        fpos.close()
        fneg.close()
        pass

main()