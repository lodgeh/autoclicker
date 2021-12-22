import mouse
import time
import random
import argparse


def doubleclick():
    mouse.click("left")
    time.sleep(0.1)
    mouse.click("left")


def time_to_wait(min, max):
    random_float = random.uniform(min, max)
    print(random_float)
    time.sleep(random_float)


def main(min, max, clicks):
    n = 0
    while True:
        if n > clicks:
            break
        doubleclick()
        time_to_wait(min, max)
        n += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Autoclicker with random intervals')

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
    min_wait = args.min_wait
    max_wait = args.max_wait
    total_clicks = args.total_clicks

    main(min_wait, max_wait, total_clicks)
