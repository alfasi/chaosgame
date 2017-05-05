from PIL import Image
import random

__width = 5000
__height = 5000
__iterations = 5000000
__rainbow_road = True

triangle = [
    (__width / 2, 0),
    (0, __height),
    (__width, __height)
]

square = [
    (0, 0),
    (__width, 0),
    (__width, __height),
    (0, __height)
]

hexagon = [
    (__width / 5, 0),
    (4 * __width / 5, 0),
    (__width / 5, __height),
    (4 * __width / 5, __height),
    (0, __height / 2),
    (__width, __height / 2)
]


def main():
    # Vertex points are by the shape of
    vertex_points = triangle

    # Factor by
    factor = 0.5

    # Create image
    image = Image.new('RGB', (__width, __height), 'white')
    pixels = image.load()

    # Create 'seed'
    last_point = (__width / 2, __height / 2)

    # Iterate
    for i in range(__iterations):
        pixels[last_point[0], last_point[1]] = (0, 0, 0)

        chosen_vertex = vertex_points[random.randint(0, len(vertex_points) - 1)]

        last_point = ((last_point[0] + chosen_vertex[0]) * factor, (last_point[1] + chosen_vertex[1]) * factor)

    # Rainbow road
    if __rainbow_road:
        for i in range(__width):
            for j in range(__height):
                if pixels[i, j] != (255, 255, 255):
                    r = i % 255 if (i / 255) % 2 == 0 else 255 - (i % 255)
                    g = j % 255 if (j / 255) % 2 == 0 else 255 - (j % 255)
                    b = 60

                    pixels[i, j] = (r, g, b)

    image.save('image.jpg')


if __name__ == '__main__':
    main()
