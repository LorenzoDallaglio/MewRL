from enum import Enum

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
    
