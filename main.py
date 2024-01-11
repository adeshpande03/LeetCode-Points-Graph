from update_csv import update_csv
from generate_graph import generate_graph
from PIL import Image, ImageDraw
from round_corners import add_corners
import logging
import datetime


def main():
    logging.basicConfig(filename="logs.log", level=logging.INFO)
    new_entry = update_csv()
    generate_graph()
    im = Image.open("points_graph.png")
    im = add_corners(im, 100)
    im.save("points_graph_rounded_corners.png")
    logging.info(
        f"{new_entry}, time: {datetime.datetime.timestamp(datetime.datetime.now())}"
    )


main()
