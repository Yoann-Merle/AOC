import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def clean(nb_lines):
        for l in range(nb_lines):
                sys.stdout.write(CURSOR_UP_ONE)
                sys.stdout.write(ERASE_LINE)

def draw(screen, scores):
        maxHeight = max(screen, key= lambda x : x[1])[1] + 1
        minHeight = min(screen, key= lambda x : x[1])[1]
        maxWidth = max(screen, key= lambda x : x[0])[0] + 1
        minWidth = min(screen, key= lambda x : x[0])[0]
        clean(maxHeight - minHeight + len(scores) + 3 + 1)
        for h in range(minHeight, maxHeight):
                line = ''
                for c in range(minWidth, maxWidth):
                        block = ' '
                        if (c, h) in screen:
                                block = screen[(c, h)]
                        line += block
                print(line)
        drawScore(scores)

def drawScore(scores):
        print()
        print('-----------')
        for s in scores:
                print('| X: ' + str(s) + '     |')
        print('-----------')

