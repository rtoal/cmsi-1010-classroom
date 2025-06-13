from math import pi, radians
from Tree.core import Tree
from PIL import Image


def main():
    tree = Tree(
        pos=(0, 0, 0, -500),
        branches=(
            (.5, radians(-30)),
            (.6, radians(30)),
            (.4, radians(60))))

    # Let the tree grow
    tree.grow(10)

    # Make sure the tree fits in the image
    tree.move_in_rectangle()

    im = Image.new("RGB", tree.get_size(), (239, 239, 239))
    tree.draw_on(im, (85, 25, 0, 128, 53, 21), (0, 62, 21), 10)
    im.show()


main()
