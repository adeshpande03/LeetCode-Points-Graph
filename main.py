from update_csv import update_csv
from generate_graph import generate_graph
from PIL import Image, ImageDraw
from round_corners import add_corners


def main():
    update_csv()
    generate_graph()
    im = Image.open("points_graph.png")
    im = add_corners(im, 10)
    im.save("points_graph_rounded_corners.png")


main()
