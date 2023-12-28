from enum import Enum
from random import randrange

class Color(Enum):
    BLUE = 1
    GREEN = 2
    PINK = 3
    PURPLE = 4
    TEAL = 5
    YELLOW = 6

class Pattern(Enum):
    FERNS = 1
    FLOWERS = 2
    LEAVES = 3
    MOROCCAN = 4
    POIS = 5
    STRIPES = 6

class Tile:
    def __init__(self):
        self.top_left = None
        self.top_right = None
        self.left = None
        self.right = None
        self.bottom_left = None
        self.bottom_right = None

class DesignGoalTile(Tile):
    def __init__(self, design):
        super().__init__()
        self.design = design

class PatchTile(Tile):
    def __init__(self, color, pattern):
        super().__init__()
        self.color = color
        self.pattern = pattern

    def __repr__(self):
        color_map = {
            Color.BLUE: '\033[44;1m',
            Color.GREEN: '\033[42;1m',
            Color.PINK: '\033[101;1m',
            Color.PURPLE: '\033[45;1m',
            Color.TEAL: '\033[106;1m',
            Color.YELLOW: '\033[103;1m'
        }
        color_header = color_map[self.color]
        color_footer = '\033[0m'
        row_bound = ('-'*12) + '\n' 
        column_bound = '|' + color_header +  10*' ' + color_footer + '|' + '\n'
        content = '|' + color_header + self.pattern.name.center(10) + color_footer + '|' + '\n'

        tile_repr = row_bound + column_bound + content + column_bound + row_bound
        return tile_repr
