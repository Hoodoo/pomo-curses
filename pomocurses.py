#!/usr/bin/env python
import curses
import time
import os

# Options
pomosetup=[
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],

    [20, 'Rest'],

    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],

    [20, 'Rest'],

    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],

    [20, 'Rest'],

    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
    [5,  'Rest'],
    [25, 'Task'],
]

progressbar_length = 30
progressbar_filled_sym = '='
progressbar_empty_sym = '-'
progressbar_left = '['
progressbar_right = ']'

stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.cbreak()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)

height,width = stdscr.getmaxyx()

# def percentage():
#     win = curses.newwin(20, 60, 0, 0)
#     win.border(0)
#     win.addstr(7,1,"{..}")
#     win.refresh()
#     time.sleep(2)

               
# #     loading = 0
#     while loading < 100:
#         loading += 1
#         time.sleep(0.03)
#         update_progress(win, loading)

# def update_progress(win, progress):
#     rangex = (30 / float(100)) * progress
#     pos = int(rangex)
#     display = '#'
#     if pos != 0:
#         win.addstr(1, pos, "{}".format(display))
#         win.refresh()

def pomo():
    pad.addstr(7,1,'[ hey hey ]')
    pad.refresh(0,0,0,0,height,width)
    time.sleep(1)
    pad.addstr(8,1,'[ hey hey ]')
    pad.refresh(0,0,0,0,height,width)
    pad.addstr(1,1,'[ hey hey ]')


    time.sleep(2)

def initial_screen(pad):
    for idx, period in enumerate(pomosetup):
        pos=idx+1
        # Yay colors
        if period[1] == 'Task':
            f=5 # Blue
        elif period[1] == 'Rest':
            if period[0] == 5:
                f=3 # Green
            else:
                f=6 # Magenta
    
        pad.addstr(pos, 1, future_progressbar().format(), curses.color_pair(f))

    pad.refresh(0,0,0,0,height,width)
    time.sleep(1)
    
def redraw_progressbar():
    time.sleep(1)
      
def active_progressbar(count, total, suffix=''):
    filled_len = int(round(progressbar_length * count / float(total)))
    bar = progressbar_filled_sym * filled_len + progressbar_empty_sym * (progressbar_length - filled_len)
    return(progressbar_left + bar + progressbar_right)

def future_progressbar(count = progressbar_length):
    bar = progressbar_empty_sym * count
    return(progressbar_left + bar + progressbar_right)

def past_progressbar(count = progressbar_length):
    bar = progressbar_filled_sym * count
    return(progressbar_left + bar + progressbar_right)

def run_pomo_timer(pad,pomosetup,position=0):
    if position != 0:
        position = position - 1 
    else:
        position = 0
    for idx, period in enumerate(pomosetup[position:]):
        pos=idx+1+position
        # Yay colors
        if period[1] == 'Task':
            f=5 # Blue
        elif period[1] == 'Rest':
            if period[0] == 5:
                f=3 # Green
            else:
                f=6 # Magenta
        os.system("play -q /home/hoodoo/sms-tone.mp3")
        for t in range(1,period[0] * 60):
            progbar = active_progressbar(t, period[0] * 60) + " " +  minsec(period[0] * 60, t) + " " + "[" + str(pos) + "]"
            pad.addstr(pos, 1, progbar.format(), curses.color_pair(f))
            time.sleep(1)
            pad.refresh(0,0,0,0,height,width)


def minsec(minutes_total, minutes_past):
    mins, secs = divmod(minutes_total - minutes_past, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    return timeformat

# Make sure curses stuff is cleaned up
try:
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
       
    pad = curses.newpad(height, width)
    pad.border(0)
    initial_screen(pad)
    run_pomo_timer(pad, pomosetup)
    
finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.curs_set(1)
    curses.endwin()

