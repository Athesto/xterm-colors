#!/usr/bin/env python3
from sys import argv
CHROMATIC_LIGHTNESS = (0x00, 0x5F, 0x87, 0xAF, 0xD7, 0xFF)
SYSTEM_LIGHTNESS = (0x80, 0xC0, 0xFF)
msg = {
    "help": '''\
Welcome to Color scprit.
Please USE THIS SYNTAX

    {0} hexa-code
    {0} end-number
    {0} start-number end-number

Ex.
    {0} "#fffff"
    {0} 19
    {0} 127 256
'''
}


def main():

    if (len(argv) == 1 or argv[1] in ['--help', "-h"]):
        print(msg["help"].format(argv[0]))
        return

    if argv[1].isdigit():
        if len(argv) == 2:
            limit_a = 0
            limit_b = int(argv[1])
        else:
            limit_a = int(argv[1], 10)
            limit_b = int(argv[2], 10)
        for code in range(limit_a, limit_b):
            val_dec = code2dec(code)
            val_gray = int(val_dec/0x010101)
            if code >= 232:
                print("{0:3d}: 0x{1:06x}, gry({2:3d})".format(
                    code, val_dec, val_gray))
            else:
                print("{0:3d}: 0x{1:06x}, ".format(
                    code, val_dec), end="")
                print("rgb({:d},{:d},{:d})".format(
                    *hex2rgb(val_dec)))
    elif argv[1].startswith("#"):
        val = int(argv[1][1:], 16)
        dec2code(val)


def hex2rgb(hex_num):
    color_r = (hex_num & (0xFF0000)) >> 8 * 2
    color_g = (hex_num & (0x00FF00)) >> 8 * 1
    color_b = (hex_num & (0x0000FF)) >> 8 * 0
    return [color_r, color_g, color_b]


def dec2code(dec):
    def dist_min(array, val):
        diff = []
        for element in array:
            diff.append(abs(val - element))
        my_min = min(diff)
        idx = diff.index(my_min)
        return [idx, my_min, array[idx]]

    [color_r, color_g, color_b] = hex2rgb(dec)

    min_r = dist_min(CHROMATIC_LIGHTNESS, color_r)
    min_g = dist_min(CHROMATIC_LIGHTNESS, color_g)
    min_b = dist_min(CHROMATIC_LIGHTNESS, color_b)

    color_diff = [min_r[1], min_g[1], min_b[1]]
    diff_code = 0
    for code in range(232, 256):
        val = grayscale_code2dec(code) // (0x010101)
        grayscale_diff = 0
        grayscale_diff += abs(color_r - val)
        grayscale_diff += abs(color_g - val)
        grayscale_diff += abs(color_b - val)
        if grayscale_diff < sum(color_diff):
            min_r = [0, abs(val - color_r), val]
            min_g = [0, abs(val - color_g), val]
            min_b = [0, abs(val - color_b), val]
            diff_code = code

    color_diff = [min_r[1], min_g[1], min_b[1]]
    color_aprox = [min_r[2], min_g[2], min_b[2]]

    if diff_code == 0:
        code = chromatic_dec2code(color_aprox)
    else:
        code = diff_code

    code_rgb = "rgb({0:3d},{1:3d},{2:3d})"
    code_hex = "#{0:02x}{1:02x}{2:02x}"
    square24 = "\033[38;2;{};{};{}m██\033[0m".format(color_r, color_g, color_b)
    square8 = "\033[38;5;{}m██\033[0m".format(code)

    code_rgb24 = code_rgb.format(color_r, color_g, color_b)
    code_hex24 = code_hex.format(color_r, color_g, color_b)

    code_rgb8 = code_rgb.format(*color_aprox)
    code_hex8 = code_hex.format(*color_aprox)
    code_rgb_diff = code_rgb.format(*color_diff)
    chromatic_hex = ", ".join(["{:3x}".format(x) for x in CHROMATIC_LIGHTNESS])
    chromatic_dec = ", ".join(["{:3d}".format(x) for x in CHROMATIC_LIGHTNESS])

    print("code: {} {}".format(code, square8))
    print()
    print("24 bits: {} {}".format(code_rgb24, code_hex24))
    print(" 8 bits: {} {}".format(code_rgb8, code_hex8))
    print("   diff: {} = {}".format(code_rgb_diff, sum(color_diff)))
    print()
    print("valid color values")
    print("[{}]".format(chromatic_dec))
    print("[{}]".format(chromatic_hex))


def chromatic_dec2code(dec):
    code_r = CHROMATIC_LIGHTNESS.index(dec[0]) * 6 ** 2
    code_g = CHROMATIC_LIGHTNESS.index(dec[1]) * 6 ** 1
    code_b = CHROMATIC_LIGHTNESS.index(dec[2]) * 6 ** 0
    code = code_r + code_g + code_b + 16
    return code


def code2dec(code):
    if code < 16:
        return system_code2dec(code)
    if code < 232:
        return chromatic_code2dec(code)
    if code < 256:
        return grayscale_code2dec(code)
    return 0


def chromatic_code2dec(code):
    # def getLightness(num): return 0 if num == 0 else ((num + 1) * 8 + 3) * 5

    val = code - 16
    color_r = val // 6 ** 2 % 6
    color_g = val // 6 ** 1 % 6
    color_b = val // 6 ** 0 % 6

    # color_r = getLightness(color_r)
    # color_g = getLightness(color_g)
    # color_b = getLightness(color_b)

    color_r = CHROMATIC_LIGHTNESS[color_r]
    color_g = CHROMATIC_LIGHTNESS[color_g]
    color_b = CHROMATIC_LIGHTNESS[color_b]

    dec = 0
    dec += color_r * (0x010000)
    dec += color_g * (0x000100)
    dec += color_b * (0x000001)
    return dec


def grayscale_code2dec(code):
    val = code - 232
    dec = 10 * val + 8
    return dec * (0x010101)


def system_code2dec(code):
    color_r = (code >> 0 & 1) * (0x010000)
    color_g = (code >> 1 & 1) * (0x000100)
    color_b = (code >> 2 & 1) * (0x000001)

    if code == 8:
        color = (0x010101)
    else:
        color = color_r + color_g + color_b

    if code == 7:
        LIGHTNESS = SYSTEM_LIGHTNESS[1]
    elif code < 9:
        LIGHTNESS = SYSTEM_LIGHTNESS[0]
    else:
        LIGHTNESS = SYSTEM_LIGHTNESS[-1]

    dec = LIGHTNESS * color
    return dec


if __name__ == "__main__":
    main()
