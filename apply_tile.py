from PIL import Image

room_img_1 = Image.open('room1.jpeg')
room_img_2 = Image.open('room2.jpeg')
tile_img = Image.open('tile.jpeg')

tile_size = (90, 90)
tile_img = tile_img.resize(tile_size)

room_area = 28.07
tile_area = 0.81


def create_tiled_floor(image, tile, room_size):
    room_width, room_height = image.size
    tile_width, tile_height = tile.size

    num_tiles_horizontal = room_width // tile_width + 1
    num_tiles_vertical = room_height // tile_height + 1

    tiled_floor = Image.new('RGB', (room_width, room_height))

    for i in range(num_tiles_horizontal):
        for j in range(num_tiles_vertical):
            tiled_floor.paste(tile, (i * tile_width, j * tile_height))

    return tiled_floor


tiled_floor_1 = create_tiled_floor(room_img_1, tile_img, room_area)
tiled_floor_2 = create_tiled_floor(room_img_2, tile_img, room_area)

room_with_tiles_1 = Image.blend(room_img_1, tiled_floor_1, alpha=0.5)
room_with_tiles_2 = Image.blend(room_img_2, tiled_floor_2, alpha=0.5)

room_with_tiles_1.save('room_with_tiles_1.jpeg')
room_with_tiles_2.save('room_with_tiles_2.jpeg')

room_with_tiles_1.show()
room_with_tiles_2.show()
