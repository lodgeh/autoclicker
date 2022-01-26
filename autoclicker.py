from ctypes import windll, wintypes, byref
import win32api
import win32con

import time
import random
import argparse


def get_cursor_location():
    cursor = wintypes.POINT()
    windll.user32.GetCursorPos(byref(cursor))
    return cursor.x, cursor.y


def random_seconds_to_wait(min, max):
    random_seconds = random.uniform(min, max)
    time.sleep(random_seconds)


def left_click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)


def right_click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)


def double_click(type, x, y):
    if type == "left":
        left_click(x, y)
        random_seconds_to_wait(0.13, 0.23)
        left_click(x, y)

    elif type == "right":
        right_click(x, y)
        random_seconds_to_wait(0.13, 0.23)
        right_click(x, y)

    else:
        print('Click type can only be "left" or "right"')


def main(left_or_right, min, max, total_clicks):
    click_counter = 0
    while True:
        if click_counter > total_clicks:
            print(f"{click_counter - 1} clicks completed")
            break
        x, y = get_cursor_location()
        double_click(left_or_right, x, y)
        random_seconds_to_wait(min, max)
        click_counter += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Autoclicker with random intervals')

    parser.add_argument(
        "left_or_right",
        metavar="left_or_right",
        type=str,
        help="Left or right clicks"
    )

    parser.add_argument(
        "min_wait",
        metavar="min_wait",
        type=float,
        help="The minimum time to wait"
    )

    parser.add_argument(
        "max_wait",
        metavar="max_wait",
        type=float,
        help="The maximum time to wait"
    )

    parser.add_argument(
        "total_clicks",
        metavar="total_clicks",
        type=float,
        help="The amount of double clicks"
    )

    args = parser.parse_args()
    left_or_right = args.left_or_right
    min_wait = args.min_wait
    max_wait = args.max_wait
    total_clicks = args.total_clicks

    main(left_or_right, min_wait, max_wait, total_clicks)
