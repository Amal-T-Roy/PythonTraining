import curses
import time


def maketextbox(h, w, y, x, value="", deco=None, textColorpair=0, decoColorpair=0):
    nw = curses.newwin(h, w, y, x)
    txtbox = curses.textpad.Textbox(nw)
    if deco == "frame":
        screen.attron(decoColorpair)
        curses.textpad.rectangle(screen, y-1, x-1, y+h, x+w)
        screen.attroff(decoColorpair)
    elif deco == "underline":
        screen.hline(y+1, x, w, decoColorpair)
    nw.addstr(0, 0, value, textColorpair)
    nw.attron(textColorpair)
    screen.refresh()
    return txtbox


try:
    screen = curses.initscr()
    screen.border(0)

    box1 = curses.newwin(22, 50, 3, 5)
    box1.box()

    box2 = curses.newwin(22, 50, 3, 65)
    box2.box()

    # box3 = maketextbox(1, 40, 10, 20, "foo", deco="underline",
    #                    textColorpair=curses.color_pair(0), decoColorpair=curses.color_pair(1))
    # textInput = box3.edit()

    box1.addstr(2, 18, "Functions")
    box2.addstr(2, 18, "Processes")
    print('SUS')
    screen.refresh()
    box1.refresh()
    box2.refresh()
    # box3.refresh()

    for i in range(19):
        toWrite = "Does this move run = %d" % i
        box1.addstr(8, 9, toWrite)
        box1.refresh()
        box2.addstr(8, 9,'Hi')
        box2.refresh()
        screen.refresh()
        time.sleep(1)
    screen.getch()

except Exception as e:
    print(e.__doc__)


finally:
    curses.endwin()
