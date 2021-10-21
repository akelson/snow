import sys
import curses
import time
from snow import Snow, PinholeCamera

if __name__ == "__main__":
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0) # Hide the cursor

        screen_size = [curses.COLS, curses.LINES]
        num_snowflakes = curses.COLS * 2

        camera = PinholeCamera(50e-3, screen_size)
        snowflakes = Snow(num_snowflakes, camera)

        while True:
            snowflakes.step()

            x_all = snowflakes.project()

            stdscr.clear()
            for x in x_all.T:
                size = -15 / x[2]
                ch = '*' if size > 1 else '.'
                row = int(x[1])
                col = int(x[0])
                stdscr.insch(row, col, ch)
            stdscr.refresh()
            time.sleep(1/30)
    except:
        curses.nocbreak()
        curses.echo()
        curses.endwin()

