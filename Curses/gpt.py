import curses
import random
import time

# initialize the curses module
stdscr = curses.initscr()

# clear the screen
stdscr.clear()

# get the screen size
max_y, max_x = stdscr.getmaxyx()

# generate 3 random numbers
numbers = [random.randint(1, 100) for i in range(3)]

# print the numbers on the screen
for i in range(3):
    # choose a random position for the number
    x = random.randint(0, max_x - 2)
    y = random.randint(0, max_y - 1)
    # print the number at the chosen position
    stdscr.addstr(y, x, str(numbers[i]))
    time.sleep(3)
    stdscr.refresh()

# refresh the screen to show the changes
stdscr.refresh()

# wait for a key press before exiting
stdscr.getch()

# end the curses module
curses.endwin()
