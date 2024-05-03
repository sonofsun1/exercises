import math
import unittest

# exercise

# Resistor Color Expert
# https://exercism.org/tracks/python/exercises/resistor-color-expert


# instructions

# convert a resistor color code to a label
# the first two or three colors represent the first digits of the resistor value
# the next color represents the multiplier
# the last color represents the tolerance
# number of colors can be 1, 4 or 5

# solution

labels = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
tolerance_labels = {
    'grey': '0.05%',
    'violet': '0.1%',
    'blue': '0.25%',
    'green': '0.5%',
    'brown': '1%',
    'red': '2%',
    'gold': '5%',
    'silver': '10%',
}

def resistor_label(colors: list) -> str:
    first_index = labels.index(colors[0])

    if len(colors) == 1:
        return format_resistion(first_index)

    res = ''
    if first_index != 0:
        res += str(first_index)

    res += str(labels.index(colors[1]))

    if len(colors) == 5:
        res += str(labels.index(colors[2]))

    res += '0' * labels.index(colors[-2])

    return f'{format_resistion(int(res))} ±{tolerance_labels[colors[-1]]}'

def format_resistion(value: int) -> str:
    main_part = 0
    prefix = ''
    if value > 1e9:
        main_part = value / 1e9
        prefix = 'giga'
    elif value > 1e6:
        main_part = value / 1e6
        prefix = 'mega'
    elif value > 1e3:
        main_part = value / 1e3
        prefix = 'kilo'
    else:
        main_part = value

    # since there is only three valueble digits, it is enough to ceil the main part
    if main_part == math.ceil(main_part):
        main_part = math.ceil(main_part)

    return f'{str(main_part)} {prefix}ohms'


# tests

class ResistorColorExpertTest(unittest.TestCase):
    def test_zero_resistion(self):
        self.assertEqual(format_resistion(0), "0 ohms")
    def test_one_number_resistion(self):
        self.assertEqual(format_resistion(5), "5 ohms")
    def test_two_number_resistion(self):
        self.assertEqual(format_resistion(55), "55 ohms")
    def test_three_number_resistion(self):
        self.assertEqual(format_resistion(555), "555 ohms")
    def test_four_number_resistion(self):
        self.assertEqual(format_resistion(1230), "1.23 kiloohms")
    def test_five_number_resistion(self):
        self.assertEqual(format_resistion(12300), "12.3 kiloohms")
    def test_six_number_resistion(self):
        self.assertEqual(format_resistion(123000), "123 kiloohms")
    def test_seven_number_resistion(self):
        self.assertEqual(format_resistion(1230000), "1.23 megaohms")
    def test_eight_number_resistion(self):
        self.assertEqual(format_resistion(12300000), "12.3 megaohms")
    def test_nine_number_resistion(self):
        self.assertEqual(format_resistion(123000000), "123 megaohms")
    def test_ten_number_resistion(self):
        self.assertEqual(format_resistion(1230000000), "1.23 gigaohms")
    def test_eleven_number_resistion(self):
        self.assertEqual(format_resistion(12300000000), "12.3 gigaohms")
    def test_twelve_number_resistion(self):
        self.assertEqual(format_resistion(123000000000), "123 gigaohms")

    def test_orange_orange_black_and_red(self):
        self.assertEqual(resistor_label(["orange", "orange", "black", "red"]), "33 ohms ±2%")
    def test_blue_grey_brown_and_violet(self):
        self.assertEqual(resistor_label(["blue", "grey", "brown", "violet"]), "680 ohms ±0.1%")
    def test_red_black_red_and_green(self):
        self.assertEqual(resistor_label(["red", "black", "red", "green"]), "2 kiloohms ±0.5%")
    def test_green_brown_orange_and_grey(self):
        self.assertEqual(
            resistor_label(["green", "brown", "orange", "grey"]), "51 kiloohms ±0.05%"
        )
    def test_one_black_band(self):
        self.assertEqual(resistor_label(["black"]), "0 ohms")
    def test_orange_orange_yellow_black_and_brown(self):
        self.assertEqual(
            resistor_label(["orange", "orange", "yellow", "black", "brown"]), "334 ohms ±1%"
        )
    def test_red_green_yellow_yellow_and_brown(self):
        self.assertEqual(
            resistor_label(["red", "green", "yellow", "yellow", "brown"]), "2.54 megaohms ±1%"
        )
    def test_blue_grey_white_brown_and_brown(self):
        self.assertEqual(
            resistor_label(["blue", "grey", "white", "brown", "brown"]), "6.89 kiloohms ±1%"
        )
    def test_violet_orange_red_and_grey(self):
        self.assertEqual(
            resistor_label(["violet", "orange", "red", "grey"]), "7.3 kiloohms ±0.05%"
        )
    def test_brown_red_orange_green_and_blue(self):
        self.assertEqual(
            resistor_label(["brown", "red", "orange", "green", "blue"]), "12.3 megaohms ±0.25%"
        )
    def test_brown_red_orange_green_and_blue(self):
        self.assertEqual(
            resistor_label(["brown", "red", "orange", "grey", "blue"]), "12.3 gigaohms ±0.25%"
        )

unittest.main()