import pygame as pg
import math
import random as rnd
import numpy as np
import time

pg.init()
if pg.display.Info().current_h < pg.display.Info().current_w:
    width = pg.display.Info().current_h - 100
else:
    width = pg.display.Info().current_w - 100
block_size = math.floor(width / 20)
tile_size = math.floor(width / 15)
font = pg.font.SysFont("Simplified Arabic", block_size)
WHITE = (255, 255, 255)

with open("words\\fa2.txt", "r", encoding='utf-8') as f:
    _2l_words = np.array(f.read().split("\n"))
with open("words\\fa3.txt", "r", encoding='utf-8') as f:
    _3l_words = np.array(f.read().split("\n"))
with open("words\\fa4.txt", "r", encoding='utf-8') as f:
    _4l_words = np.array(f.read().split("\n"))
with open("words\\fa5.txt", "r", encoding='utf-8') as f:
    _5l_words = np.array(f.read().split("\n"))
with open("words\\fa6.txt", "r", encoding='utf-8') as f:
    _6l_words = np.array(f.read().split("\n"))
with open("words\\fa7.txt", "r", encoding='utf-8') as f:
    _7l_words = np.array(f.read().split("\n"))
with open("words\\fa8.txt", "r", encoding='utf-8') as f:
    _8l_words = np.array(f.read().split("\n"))
with open("words\\fa9.txt", "r", encoding='utf-8') as f:
    _9l_words = np.array(f.read().split("\n"))
with open("words\\fa10.txt", "r", encoding='utf-8') as f:
    _10l_words = np.array(f.read().split("\n"))
with open("words\\fa11.txt", "r", encoding='utf-8') as f:
    _11l_words = np.array(f.read().split("\n"))
with open("words\\fa12.txt", "r", encoding='utf-8') as f:
    _12l_words = np.array(f.read().split("\n"))
with open("words\\fa13.txt", "r", encoding='utf-8') as f:
    _13l_words = np.array(f.read().split("\n"))
with open("words\\fa14.txt", "r", encoding='utf-8') as f:
    _14l_words = np.array(f.read().split("\n"))
with open("words\\fa15.txt", "r", encoding='utf-8') as f:
    _15l_words = np.array(f.read().split("\n"))

a = pg.image.load("logos\\ا.png")
a = pg.transform.scale(a, (tile_size - 4, tile_size - 4))
alef = pg.image.load("logos\\آ.png")
alef = pg.transform.scale(alef, (tile_size - 4, tile_size - 4))
be = pg.image.load("logos\\ب.png")
be = pg.transform.scale(be, (tile_size - 4, tile_size - 4))
pe = pg.image.load("logos\\پ.png")
pe = pg.transform.scale(pe, (tile_size - 4, tile_size - 4))
te = pg.image.load("logos\\ت.png")
te = pg.transform.scale(te, (tile_size - 4, tile_size - 4))
se = pg.image.load("logos\\ث.png")
se = pg.transform.scale(se, (tile_size - 4, tile_size - 4))
jim = pg.image.load("logos\\ج.png")
jim = pg.transform.scale(jim, (tile_size - 4, tile_size - 4))
che = pg.image.load("logos\\چ.png")
che = pg.transform.scale(che, (tile_size - 4, tile_size - 4))
he = pg.image.load("logos\\ح.png")
he = pg.transform.scale(he, (tile_size - 4, tile_size - 4))
khe = pg.image.load("logos\\خ.png")
khe = pg.transform.scale(khe, (tile_size - 4, tile_size - 4))
dal = pg.image.load("logos\\د.png")
dal = pg.transform.scale(dal, (tile_size - 4, tile_size - 4))
zal = pg.image.load("logos\\ذ.png")
zal = pg.transform.scale(zal, (tile_size - 4, tile_size - 4))
re = pg.image.load("logos\\ر.png")
re = pg.transform.scale(re, (tile_size - 4, tile_size - 4))
ze = pg.image.load("logos\\ز.png")
ze = pg.transform.scale(ze, (tile_size - 4, tile_size - 4))
zhe = pg.image.load("logos\\ژ.png")
zhe = pg.transform.scale(zhe, (tile_size - 4, tile_size - 4))
sin = pg.image.load("logos\\س.png")
sin = pg.transform.scale(sin, (tile_size - 4, tile_size - 4))
shin = pg.image.load("logos\\ش.png")
shin = pg.transform.scale(shin, (tile_size - 4, tile_size - 4))
sad = pg.image.load("logos\\ص.png")
sad = pg.transform.scale(sad, (tile_size - 4, tile_size - 4))
zad = pg.image.load("logos\\ض.png")
zad = pg.transform.scale(zad, (tile_size - 4, tile_size - 4))
ta = pg.image.load("logos\\ط.png")
ta = pg.transform.scale(ta, (tile_size - 4, tile_size - 4))
za = pg.image.load("logos\\ظ.png")
za = pg.transform.scale(za, (tile_size - 4, tile_size - 4))
ein = pg.image.load("logos\\ع.png")
ein = pg.transform.scale(ein, (tile_size - 4, tile_size - 4))
qein = pg.image.load("logos\\غ.png")
qein = pg.transform.scale(qein, (tile_size - 4, tile_size - 4))
fe = pg.image.load("logos\\ف.png")
fe = pg.transform.scale(fe, (tile_size - 4, tile_size - 4))
quf = pg.image.load("logos\\ق.png")
quf = pg.transform.scale(quf, (tile_size - 4, tile_size - 4))
kaf = pg.image.load("logos\\ک.png")
kaf = pg.transform.scale(kaf, (tile_size - 4, tile_size - 4))
gaf = pg.image.load("logos\\گ.png")
gaf = pg.transform.scale(gaf, (tile_size - 4, tile_size - 4))
lam = pg.image.load("logos\\ل.png")
lam = pg.transform.scale(lam, (tile_size - 4, tile_size - 4))
mim = pg.image.load("logos\\م.png")
mim = pg.transform.scale(mim, (tile_size - 4, tile_size - 4))
nun = pg.image.load("logos\\ن.png")
nun = pg.transform.scale(nun, (tile_size - 4, tile_size - 4))
vav = pg.image.load("logos\\و.png")
vav = pg.transform.scale(vav, (tile_size - 4, tile_size - 4))
he2 = pg.image.load("logos\\ه.png")
he2 = pg.transform.scale(he2, (tile_size - 4, tile_size - 4))
ye = pg.image.load("logos\\ی.png")
ye = pg.transform.scale(ye, (tile_size - 4, tile_size - 4))

change_tile_img = pg.image.load("logos\\تعویض.png")
change_tile_img = pg.transform.scale(change_tile_img, (int(13 * width / 120), int(width / 15)))
next_img = pg.image.load("logos\\بعدی.png")
next_img = pg.transform.scale(next_img, (int(13 * width / 120), int(width / 15)))
clear_img = pg.image.load("logos\\پاک.png")
clear_img = pg.transform.scale(clear_img, (int(13 * width / 120), int(width / 15)))

alphabets = {
    a: "ا", alef: "آ", be: "ب", pe: "پ", te: "ت", se: "ث", jim: "ج", che: "چ", he: "ح", khe: "خ", dal: "د", zal: "ذ",
    re: "ر", ze: "ز", zhe: "ژ", sin: "س", shin: "ش", sad: "ص", zad: "ض", ta: "ط", za: "ظ", ein: "ع", qein: "غ", fe: "ف",
    quf: "ق", kaf: "ک", gaf: "گ", lam: "ل", mim: "م", nun: "ن", vav: "و", he2: "ه", ye: "ی"
}

alphabets_on_grid = {}
for n in range(1, 226):
    alphabets_on_grid[n] = None

scores = {
    "ا": 1, "آ": 1, "ب": 1, "پ": 2, "ت": 1, "ث": 3, "ج": 2, "چ": 1, "ح": 3, "خ": 2, "د": 2, "ذ": 5, "ر": 1, "ز": 2,
    "ژ": 10, "س": 1, "ش": 2, "ص": 2, "ض": 3, "ط": 4, "ظ": 5, "ع": 3, "غ": 3, "ف": 2, "ق": 3, "ک": 2, "گ": 2, "ل": 5,
    "م": 2, "ن": 2, "و": 1, "ه": 2, "ی": 2
}

blocks = {}
tiles = {}
tiles_to_fill = {}
found_words = {}
tiles_filling = []
new_on_grid = {}
n_words = {
    2: _2l_words, 3: _3l_words, 4: _4l_words, 5: _5l_words, 6: _6l_words, 7: _7l_words, 8: _8l_words, 9: _9l_words,
    10: _11l_words, 11: _11l_words, 12: _12l_words, 13: _13l_words, 14: _14l_words, 15: _15l_words
}
score = 0

pg.display.set_caption("WordFeud")

screen = pg.display.set_mode((width, width))
screen.fill([17, 20, 26])
pg.display.set_icon(kaf)
pg.display.flip()


def draw_background():
    main_border = pg.Rect(int(width / 8), int(width / 8), 15 * block_size, 15 * block_size)
    tile_border = pg.Rect(int(width / 2) - 4 * tile_size, width - tile_size - int(width / 40), 8 * tile_size, tile_size)
    pg.draw.rect(screen, [24, 27, 31], main_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], main_border, 2, border_radius=2)
    pg.draw.rect(screen, [79, 79, 79], tile_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], tile_border, 2, border_radius=2)


def draw_grid():
    global blocks
    num = 1
    for y in range(int(width / 8), int(width / 8) + 15 * block_size, block_size):
        for x in range(int(width / 8), int(width / 8) + 15 * block_size, block_size):
            pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, y, block_size, block_size), 1, border_radius=3)
            blocks[num] = (x, y)
            num += 1
    for pos in list(alphabets_on_grid.keys()):
        if alphabets_on_grid[pos] is not None:
            index = list(alphabets.values()).index(alphabets_on_grid[pos])
            screen.blit(pg.transform.scale(list(alphabets.keys())[index], (block_size - 4, block_size - 4)),
                        (blocks[pos][0] + 2, blocks[pos][1] + 2))


def draw_tiles():
    global tiles, tiles_to_fill
    i = 1
    for x in range(int(width / 2) - 4 * tile_size, int(width / 2) + 4 * tile_size, tile_size):
        pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, width - tile_size - int(width / 40), tile_size, tile_size), 1,
                     border_radius=3)
        tiles[i] = (x, width - tile_size - int(width / 40))
        tiles_to_fill[i] = (x + 2, width - tile_size - int(width / 40) + 2)
        i += 1


def start_tile():
    global tiles_filling
    for i in range(8):
        tiles_filling.append(rnd.randint(0, 32))


def put_tiles():
    for i in range(1, len(tiles_filling) + 1):
        try:
            tile = list(alphabets.keys())[tiles_filling[i - 1]]
            screen.blit(tile, (tiles_to_fill[i]))
        except IndexError:
            pg.draw.rect(screen, [79, 79, 79], pg.Rect(tiles_to_fill[i][0], tiles_to_fill[i][1], tile_size - 4,
                                                       tile_size - 4), 0)


def move_tile(x, y):
    global tiles_filling, alphabets_on_grid
    for pos in range(1, len(tiles_filling) + 1):
        if x in range(tiles[pos][0], tiles[pos][0] + tile_size) and y in range(tiles[pos][1],
                                                                               tiles[pos][1] + tile_size):
            selected_tile = list(alphabets.keys())[tiles_filling[pos - 1]]
            click_count = 1
            tmp_num = tiles_filling[pos - 1]
            tiles_filling[pos - 1] = 34
            animate(tiles_to_fill[pos][0], tiles_to_fill[pos][1], x - int((tile_size - 4) / 2),
                    y - int((tile_size - 4) / 2),
                    selected_tile)
            tiles_filling[pos - 1] = tmp_num
            while True:
                new_pos = (False, pos)
                for mouse_event in pg.event.get():
                    if mouse_event.type == pg.MOUSEBUTTONUP:
                        click_count = 2
                if click_count == 2:
                    for block in blocks.keys():
                        if pg.mouse.get_pos()[0] in range(blocks[block][0], blocks[block][0] + block_size) and \
                                pg.mouse.get_pos()[1] in range(blocks[block][1], blocks[block][1] + block_size):
                            if alphabets_on_grid[block] is None:
                                animate(pg.mouse.get_pos()[0] + 2 - int(tile_size / 2),
                                        pg.mouse.get_pos()[1] + 2 - int(tile_size / 2), blocks[block][0] + 2,
                                        blocks[block][1] + 2, selected_tile)
                                rescale(blocks[block][0] + 2, blocks[block][1] + 2, selected_tile, 0)
                                alphabets_on_grid[block] = list(alphabets.values())[tiles_filling[pos - 1]]
                                new_on_grid[block] = alphabets_on_grid[block]
                                del tiles_filling[pos - 1]
                                new_pos = (True, block)
                                break
                    for tile in tiles.keys():
                        if pg.mouse.get_pos()[0] in range(tiles[tile][0], tiles[tile][0] + tile_size) and \
                                pg.mouse.get_pos()[1] in range(tiles[tile][1], tiles[tile][1] + tile_size):
                            try:
                                tiles_filling[tile - 1]
                            except IndexError:
                                del tiles_filling[pos - 1]
                                animate(pg.mouse.get_pos()[0] + 2 - int(tile_size / 2),
                                        pg.mouse.get_pos()[1] + 2 - int(tile_size / 2),
                                        tiles_to_fill[len(tiles_filling) + 1][0],
                                        tiles_to_fill[len(tiles_filling) + 1][1],
                                        selected_tile)
                                tiles_filling.append(list(alphabets.keys()).index(selected_tile))
                                new_pos = (True, tile)

                    if not new_pos[0]:
                        tiles_filling[pos - 1] = 34
                        animate(pg.mouse.get_pos()[0] + 2 - int(tile_size / 2),
                                pg.mouse.get_pos()[1] + 2 - int(tile_size / 2),
                                tiles_to_fill[pos][0], tiles_to_fill[pos][1],
                                selected_tile)
                        tiles_filling[pos - 1] = tmp_num
                    break

                pg.draw.rect(screen, [79, 79, 79], pg.Rect(tiles_to_fill[pos][0], tiles_to_fill[pos][1], tile_size - 4,
                                                           tile_size - 4), 0)
                screen.blit(selected_tile,
                            (pg.mouse.get_pos()[0] - tile_size / 2, pg.mouse.get_pos()[1] - tile_size / 2))
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()
            del tmp_num
    for pos in blocks.keys():
        if x in range(blocks[pos][0], blocks[pos][0] + block_size) and y in range(blocks[pos][1],
                                                                                  blocks[pos][1] + block_size):
            if pos in new_on_grid.keys():
                selected_tile = list(alphabets.keys())[list(alphabets.values()).index(new_on_grid[pos])]
                click_count = 1
                alphabets_on_grid[pos] = None

                rescale(blocks[pos][0] + 2, blocks[pos][1] + 2, selected_tile, 1)
                animate(blocks[pos][0] + 2, blocks[pos][1] + 2, x - int((tile_size - 4) / 2),
                        y - int((tile_size - 4) / 2),
                        selected_tile)

                while True:
                    on_pos = False
                    for mouse_event in pg.event.get():
                        if mouse_event.type == pg.MOUSEBUTTONUP:
                            click_count = 2
                    if click_count == 2:
                        for block in blocks.keys():
                            if pg.mouse.get_pos()[0] in range(blocks[block][0], blocks[block][0] + block_size) and \
                                    pg.mouse.get_pos()[1] in range(blocks[block][1], blocks[block][1] + block_size):
                                if alphabets_on_grid[block] is None:
                                    animate(pg.mouse.get_pos()[0] + 2 - int(tile_size / 2),
                                            pg.mouse.get_pos()[1] + 2 - int(tile_size / 2), blocks[block][0] + 2,
                                            blocks[block][1] + 2, selected_tile)
                                    rescale(blocks[block][0] + 2, blocks[block][1] + 2, selected_tile, 0)
                                    alphabets_on_grid[block] = alphabets[selected_tile]
                                    del new_on_grid[pos]
                                    new_on_grid[block] = alphabets_on_grid[block]
                                    on_pos = True
                                    break
                                else:
                                    alphabets_on_grid[pos] = alphabets[selected_tile]
                                    break
                        for tile in tiles.keys():
                            if pg.mouse.get_pos()[0] in range(tiles[tile][0], tiles[tile][0] + tile_size) and \
                                    pg.mouse.get_pos()[1] in range(tiles[tile][1], tiles[tile][1] + tile_size):
                                try:
                                    tiles_filling[tile - 1]
                                except IndexError:
                                    del new_on_grid[pos]
                                    animate(pg.mouse.get_pos()[0] + 2 - int(tile_size / 2),
                                            pg.mouse.get_pos()[1] + 2 - int(tile_size / 2), tiles_to_fill[tile][0],
                                            tiles_to_fill[tile][1], selected_tile)
                                    tiles_filling.append(list(alphabets.keys()).index(selected_tile))
                                    on_pos = True
                        if not on_pos:
                            alphabets_on_grid[pos] = alphabets[selected_tile]
                        break
                    screen.blit(selected_tile,
                                (pg.mouse.get_pos()[0] - tile_size / 2, pg.mouse.get_pos()[1] - tile_size / 2))
                    pg.display.update()

                    screen.fill([17, 20, 26])
                    draw_background()
                    draw_grid()
                    draw_tiles()
                    put_tiles()
                    bars()


def check_continuous(direction):
    # direction options:
    #                   (1, None, edge_stat) : only one new alphabet and all near blocks should be checked
    #                 (2, V or H, edge_stat) : only the blocks between the new alphabets should be checked
    #                 (3, V or H, edge_stat) : all the blocks between them should be checked
    # edge_stat:
    #        None : for more than one alphabet
    #           0 : top edge
    #           1 : right edge
    #           2 : bottom edge
    #           3 : left edge
    #           5 : not edge

    n1 = list(new_on_grid.keys())
    n1.sort()
    n1 = n1[0]
    return_stat = None

    if direction[0] == 1:
        return_stat = False
        if direction[2][0] == 0 and direction[2][1] == 0:
            if alphabets_on_grid[n1 - 1] is not None or \
                    alphabets_on_grid[n1 + 1] is not None or \
                    alphabets_on_grid[n1 + 15] is not None:
                return_stat = True
        if direction[2][0] == 0 and direction[2][1] == 1:
            if alphabets_on_grid[n1 - 1] is not None or \
                    alphabets_on_grid[n1 + 15] is not None:
                return_stat = True
        if direction[2][0] == 1 and direction[2][1] == 1:
            if alphabets_on_grid[n1 - 15] is not None or \
                    alphabets_on_grid[n1 + 15] is not None or \
                    alphabets_on_grid[n1 - 1] is not None:
                return_stat = True
        if direction[2][0] == 1 and direction[2][1] == 2:
            if alphabets_on_grid[n1 - 1] is not None or \
                    alphabets_on_grid[n1 - 15] is not None:
                return_stat = True
        if direction[2][0] == 2 and direction[2][1] == 2:
            if alphabets_on_grid[n1 - 1] is not None or \
                    alphabets_on_grid[n1 + 1] is not None or \
                    alphabets_on_grid[n1 - 15] is not None:
                return_stat = True
        if direction[2][0] == 2 and direction[2][1] == 3:
            if alphabets_on_grid[n1 + 1] is not None or \
                    alphabets_on_grid[n1 - 15] is not None:
                return_stat = True
        if direction[2][0] == 3 and direction[2][1] == 3:
            if alphabets_on_grid[n1 - 15] is not None or \
                    alphabets_on_grid[n1 + 15] is not None or \
                    alphabets_on_grid[n1 - 1] is not None:
                return_stat = True
        if direction[2][0] == 3 and direction[2][1] == 0:
            if alphabets_on_grid[n1 + 1] is not None or \
                    alphabets_on_grid[n1 + 15] is not None:
                return_stat = True
        if direction[2][0] == 5 and direction[2][1] == 5:
            if alphabets_on_grid[n1 - 15] is not None or \
                    alphabets_on_grid[n1 + 15] is not None or \
                    alphabets_on_grid[n1 + 1] is not None or \
                    alphabets_on_grid[n1 - 1] is not None:
                return_stat = True

    if direction[0] == 2 and direction[1] == "V":
        n2 = list(new_on_grid.keys())[1]
        return_stat = True
        for block in range(n1 + 15, n2, 15):
            if alphabets_on_grid[block] is None:
                return_stat = False
                break

    if direction[0] == 2 and direction[1] == "H":
        n2 = list(new_on_grid.keys())[1]
        return_stat = True
        for block in range(n1 + 1, n2):
            if alphabets_on_grid[block] is None:
                return_stat = False
                break

    if direction[0] >= 3 and direction[1] == "V":
        return_stat = True
        nums = list(new_on_grid.keys())
        for i in range(len(nums) - 1):
            for block in range(nums[i] + 15, nums[i + 1], 15):
                if alphabets_on_grid[block] is None:
                    return_stat = False
                    break
            if not return_stat:
                break

    if direction[0] >= 3 and direction[1] == "H":
        return_stat = True
        nums = list(new_on_grid.keys())
        for i in range(len(nums) - 1):
            for block in range(nums[i] + 1, nums[i + 1]):
                if alphabets_on_grid[block] is None:
                    return_stat = False
                    break
            if not return_stat:
                break

    return return_stat


def on_a_line():
    direction = None
    check_list = list(new_on_grid.keys())
    check_list.sort()
    if len(check_list) == 0:
        return False, 0

    if len(check_list) == 1:
        if check_list[0] == 1:
            edge_stat = (3, 0)
        elif check_list[0] == 15:
            edge_stat = (0, 1)
        elif check_list[0] == 211:
            edge_stat = (2, 3)
        elif check_list[0] == 225:
            edge_stat = (1, 2)
        elif check_list[0] in range(2, 15):
            edge_stat = (0, 0)
        elif check_list[0] in range(30, 226, 15):
            edge_stat = (1, 1)
        elif check_list[0] in range(212, 225):
            edge_stat = (2, 2)
        elif check_list[0] in range(16, 212, 15):
            edge_stat = (0, 0)
        else:
            edge_stat = (5, 5)
        return check_continuous((1, None, edge_stat)), 1

    for i in check_list:
        if (i - check_list[0]) % 15 == 0:
            direction = "V"
        else:
            direction = None
            break
    if direction is not None:
        return check_continuous((len(check_list), "V", None)), 2

    for j in range(1, 212, 15):
        for i in range(j, j + 15):
            if i == check_list[0]:
                for num in check_list:
                    if num < j + 15:
                        direction = "H"
                    else:
                        direction = None
                        break
                break
        if direction is not None:
            break
    if direction is not None:
        return check_continuous((len(check_list), "H", None)), 2

    else:
        return False, 2


def find_word():
    global found_words, score
    word = ""
    word_stat = None
    return_stat = True
    false_words = []
    new_words = {}
    try:
        if not on_a_line()[0] and on_a_line()[1] == 0:
            return False, "no new alphabet"
        elif not on_a_line()[0] and on_a_line()[1] == 1:
            return False, "at least 2 alphabets in a row required"
        elif not on_a_line()[0] and on_a_line()[1] == 2:
            return False, "alphabets are not in a row"
        else:
            pass
        # vertical search
        for i in range(1, 16):  # select x value of grid
            for j in range(i, 226, 15):  # change y value in a column (up -> down)
                if alphabets_on_grid[j] in list(alphabets.values()):  # check if any alphabet assigns to that block
                    word += alphabets_on_grid[j]  # add alphabet to word to make it
                    if j == i + 14 * 15:  # check if y value of grid is the last one of the column
                        # check length of word if its bigger than 1 and not found before
                        if len(word) > 1 and (j - (len(word) - 1) * 15, j) not in list(found_words.keys()):
                            new_words[(j - (len(word) - 1) * 15, j)] = word
                            # reset word value for next check
                            word = ""

                    # check if next block is empty to recognize the end of the word (checked if last "if" doesn't run)
                    elif alphabets_on_grid[j + 15] not in list(alphabets.values()):
                        # check length of word if its bigger than 1 and not found before
                        if len(word) > 1 and (j - (len(word) - 1) * 15, j) not in list(found_words.keys()):
                            new_words[(j - (len(word) - 1) * 15, j)] = word
                            # reset word value for next check
                            word = ""
                else:
                    word = ""
            word = ""
        # horizontal search
        for i in range(1, 212, 15):  # select y value of grid
            for j in range(i + 14, i - 1, -1):  # change x value in a row (right -> left)
                if alphabets_on_grid[j] in list(alphabets.values()):  # check if any alphabet assigns to that block
                    word += alphabets_on_grid[j]  # add alphabet to word to make it
                    if j == i:  # check if x value of grid is the last one of the row
                        # check length of word if its bigger than 1 and not found before
                        if len(word) > 1 and (j + len(word) - 1, j) not in list(found_words.keys()):
                            new_words[(j + len(word) - 1, j)] = word
                            # reset word value for next check
                            word = ""

                    # check if next block is empty to recognize the end of the word (checked if last "if" doesn't run)
                    elif alphabets_on_grid[j - 1] not in list(alphabets.values()):
                        # check length of word if its bigger than 1 and not found before
                        if len(word) > 1 and (j + len(word) - 1, j) not in list(found_words.keys()):
                            new_words[(j + len(word) - 1, j)] = word
                            # reset word value for next check
                            word = ""
                else:
                    word = ""
            word = ""
        # check words that found in new round

        for new_word in new_words.values():
            length = len(new_word)
            # check that the word is in the dictionary or not
            # if it is, add the word to found_words and change word_stat status to true
            # if not, add the word to false_words to show it later to player and change word_stat status to false
            if new_word in n_words[length]:
                word_stat = True
            else:
                word_stat = False
            index = list(new_words.values()).index(new_word)
            if word_stat is False:
                false_words.append(new_word)
                new_words[list(new_words.keys())[index]] = 0
                return_stat = False
            else:
                found_words[list(new_words.keys())[index]] = new_word

        return (True, list(new_words.values())) if return_stat else (False, "false words", false_words)
    except Exception as e:
        print("error occurred")
        return False, e


def next_round():
    global new_on_grid, tiles_filling, score
    if mouse_pos[0] in range(int(2 * width / 15) + 15 * block_size, int(29 * width / 120) + 15 * block_size) and \
            mouse_pos[1] in \
            range(int(width / 8), int(23 * width / 120)):
        stat = find_word()
        if stat[0]:
            print(stat[1])
            new_on_grid.clear()
            for word in stat[1]:
                if word == 0:
                    continue
                for i in word:
                    score += scores[i]
            for i in range(8 - len(tiles_filling)):
                tiles_filling.append(rnd.randint(0, 32))
        else:
            if stat[1] == "false words":
                print(stat[2], " is not in dictionary")
            else:
                print(stat[1])


def bars():
    top_bar = pg.Rect(int(width / 8), int(width / 40), 15 * block_size, int(width / 15))
    pg.draw.rect(screen, [54, 54, 54], top_bar, 0, border_radius=3)
    pg.draw.rect(screen, [0, 0, 0], top_bar, 2, border_radius=3)
    pg.draw.line(screen, [0, 0, 0], (int(width / 2), int(width / 40)), (int(width / 2), int(11 * width / 120) - 1), 2)
    screen.blit(font.render("Score : %i" % score, True, WHITE), (int(width / 8) + 5, int(width / 60)))
    screen.blit(font.render("Word : %i" % len(found_words.values()), True, WHITE),
                (int(width / 2) + 5, int(width / 60)))
    change_bar = pg.Rect(int(width / 120) - 2, int(width / 8) - 2, int(13 * width / 120) + 4, int(width / 15) + 4)
    pg.draw.rect(screen, [0, 0, 0], change_bar, 2, border_radius=3)
    screen.blit(change_tile_img, (int(width / 120), int(width / 8)))

    next_bar = pg.Rect(int(2 * width / 15) + 15 * block_size - 2, int(width / 8) - 2, int(13 * width / 120) + 4,
                       int(width / 15) + 4)
    pg.draw.rect(screen, [0, 0, 0], next_bar, 2, border_radius=3)
    screen.blit(next_img, (int(2 * width / 15) + 15 * block_size, int(width / 8)))

    clear_bar = pg.Rect(int(2 * width / 15) + 15 * block_size - 2, int(5 * width / 24) - 2, int(13 * width / 120) + 4,
                        int(width / 15) + 4)
    pg.draw.rect(screen, [0, 0, 0], clear_bar, 2, border_radius=3)
    screen.blit(clear_img, (int(2 * width / 15) + 15 * block_size, int(5 * width / 24)))


def reset_tile():
    global tiles_filling, new_on_grid
    if mouse_pos[0] in range(int(width / 120), int(7 * width / 60)) and mouse_pos[1] in range(int(width / 8),
                                                                                              int(23 * width / 120)):
        for pos in list(new_on_grid.keys()):
            tiles_filling.append(list(alphabets.values()).index(new_on_grid[pos]))
            del new_on_grid[pos]
            alphabets_on_grid[pos] = None
        for i in range(len(tiles_filling)):
            tiles_filling[i] = rnd.randint(0, 32)


def clear_grid():
    global new_on_grid, tiles_filling, alphabets_on_grid
    if mouse_pos[0] in range(int(2 * width / 15) + 15 * block_size, int(29 * width / 120) + 15 * block_size) and \
            mouse_pos[1] in \
            range(int(5 * width / 24), int(11 * width / 40)):
        for pos in list(new_on_grid.keys()):
            tiles_filling.append(list(alphabets.values()).index(new_on_grid[pos]))
            del new_on_grid[pos]
            alphabets_on_grid[pos] = None


def animate(x1, y1, x2, y2, layer):
    # stat: False  -> scale doesn't change
    # stat:  True -> scale changes

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    count = 0

    if dy > dx:
        if x1 == x2 and y2 > y1:
            for y in range(y1, y2 + 1):
                screen.blit(layer, (x1, y))
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()

        if x1 == x2 and y1 > y2:
            for y in range(y1, y2 - 1, -1):
                screen.blit(layer, (x1, y))
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()

        if dx != 0:
            y_step = math.floor(dy / dx)

        if x1 > x2 and y1 > y2:
            for x in range(x1, x2 - 1, -1):
                count += 1
                if y1 - count * y_step >= y2:
                    for y in range(y1 - (count - 1) * y_step, y1 - count * y_step - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for y in range(y1 - (count - 1) * y_step, y2 - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for X in range(x, x2 - 1, -1):
                        screen.blit(layer, (X, y2))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x2 > x1 and y1 > y2:

            for x in range(x1, x2 + 1):
                count += 1
                if y1 - count * y_step >= y2:
                    for y in range(y1 - (count - 1) * y_step, y1 - count * y_step - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for y in range(y1 - (count - 1) * y_step, y2 - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for X in range(x, x2 + 1):
                        screen.blit(layer, (X, y2))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x1 > x2 and y2 > y1:

            for x in range(x1, x2 - 1, -1):
                count += 1
                if y1 + count * y_step <= y2:
                    for y in range(y1 + (count - 1) * y_step, y1 + count * y_step + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for y in range(y1 + (count - 1) * y_step, y2 + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for X in range(x, x2 - 1, -1):
                        screen.blit(layer, (X, y2))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x2 > x1 and y2 > y1:

            for x in range(x1, x2 + 1):
                count += 1
                if y1 + count * y_step <= y2:
                    for y in range(y1 + (count - 1) * y_step, y1 + count * y_step + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for y in range(y1 + (count - 1) * y_step, y2 + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for X in range(x, x2 + 1):
                        screen.blit(layer, (X, y2))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

    if dx > dy:
        if y1 == y2 and x2 > x1:
            for x in range(x1, x2 + 1):
                screen.blit(layer, (x, y1))
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()

        if y1 == y2 and x1 > x2:
            for x in range(x1, x2 - 1, -1):
                screen.blit(layer, (x, y1))
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()

        if dy != 0:
            x_step = math.floor(dx / dy)

        if x1 > x2 and y1 > y2:

            for y in range(y1, y2 - 1, -1):
                count += 1
                if x1 - count * x_step >= x2:
                    for x in range(x1 - (count - 1) * x_step, x1 - count * x_step - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for x in range(x1 - (count - 1) * x_step, x2 - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for Y in range(y, y2 - 1, -1):
                        screen.blit(layer, (x2, Y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x2 > x1 and y1 > y2:

            for y in range(y1, y2 - 1, -1):
                count += 1
                if x1 + count * x_step <= x2:
                    for x in range(x1 + count * x_step, x1 + (count - 1) * x_step - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for x in range(x1 + (count - 1) * x_step, x2 + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for Y in range(y, y2 - 1, -1):
                        screen.blit(layer, (x2, Y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x1 > x2 and y2 > y1:

            for y in range(y1, y2 + 1):
                count += 1
                if x1 - count * x_step >= x2:
                    for x in range(x1 - (count - 1) * x_step, x1 - count * x_step - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for x in range(x1 - (count - 1) * x_step, x2 - 1, -1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()

                    for Y in range(y, y2 + 1):
                        screen.blit(layer, (x2, Y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

        if x2 > x1 and y2 > y1:

            for y in range(y1, y2 + 1):
                count += 1
                if x1 + count * x_step <= x2:
                    for x in range(x1 + (count - 1) * x_step, x1 + count * x_step + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                else:
                    for x in range(x1 + (count - 1) * x_step, x2 + 1):
                        screen.blit(layer, (x, y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    for Y in range(y, y2 + 1):
                        screen.blit(layer, (x2, Y))
                        pg.display.update()

                        screen.fill([17, 20, 26])
                        draw_background()
                        draw_grid()
                        draw_tiles()
                        put_tiles()
                        bars()
                    break

    if dx == dy:
        x = x1
        y = y1
        for i in range(dx):
            if x2 > x1 and y2 > y1:
                x += 1
                y += 1
            if x1 > x2 and y2 > y1:
                x -= 1
                y += 1
            if x2 > x1 and y1 > y2:
                x += 1
                y -= 1
            if x1 > x2 and y1 > y2:
                x -= 1
                y -= 1

            screen.blit(layer, (x, y))
            pg.display.update()

            screen.fill([17, 20, 26])
            draw_background()
            draw_grid()
            draw_tiles()
            put_tiles()
            bars()


def rescale(x, y, layer, scale_code):
    # scale_code : 0 -> for dropping on a block; shrink layer from tile_size to block_size
    # scale_code : 1 -> for dragging from a block; extend layer from block_size into tile_size

    if str(scale_code) == "0":
        for s in range(tile_size - 4, block_size - 5, -1):
            time.sleep(0.000625)
            screen.blit(pg.transform.scale(layer, (s, s)), (x - 2 + int(block_size / 2) - int(s / 2),
                                                            y - 2 + int(block_size / 2) - int(s / 2)))
            pg.display.update()

            screen.fill([17, 20, 26])
            draw_background()
            draw_grid()
            draw_tiles()
            put_tiles()
            bars()

    if str(scale_code) == "1":
        for s in range(block_size - 4, tile_size - 3):
            time.sleep(0.000625)
            screen.blit(pg.transform.scale(layer, (s, s)), (x, y))
            pg.display.update()

            screen.fill([17, 20, 26])
            draw_background()
            draw_grid()
            draw_tiles()
            put_tiles()
            bars()


start_tile()
done = False
clock = pg.time.Clock()
while not done:
    clock.tick(60)
    mouse_pos = pg.mouse.get_pos()
    draw_background()
    draw_grid()
    draw_tiles()
    put_tiles()
    bars()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                clear_grid()
                reset_tile()
                move_tile(mouse_pos[0], mouse_pos[1])
                next_round()

    pg.display.update()
