from tiles import PatchTile, DesignGoalTile, Color, Pattern
from random import randrange
import re

class QuiltBoard:
    def __init__(self):
        self.design_position = [(2, 3), (3, 4), (4, 2)]
        self.nrows = 7
        self.ncols = 7
        self.tiles = [[None for i in range(self.ncols)] for j in range(self.nrows)]

    ##Every even row (uneven index) is shifted by one
    def add_tile(self, new_tile, row, column):
        self.tiles[row][column] = new_tile
        offset = 1 if row%2 == 0 else 0
        
        if row > 0:
            if column - offset > - 1:
                top_left_tile = self.tiles[row - 1][column - offset]
                if top_left_tile:
                    new_tile.top_left = top_left_tile
                    top_left_tile.bottom_right = new_tile
        
            if column - offset < 6:
                top_right_tile = self.tiles[row - 1][column - offset + 1]
                if top_right_tile:
                    new_tile.top_right = top_right_tile
                    top_right_tile.bottom_left = new_tile

        if column > 0:
            left_tile = self.tiles[row][column - 1]
            if left_tile:
                new_tile.left = left_tile
                left_tile.right = new_tile

        if column < 6:
            right_tile = self.tiles[row][column + 1]
            if right_tile:
                new_tile.right = right_tile
                right_tile.left = new_tile

        if row < 6:
            if column - offset > - 1:
                bottom_left_tile = self.tiles[row + 1][column - offset]
                if bottom_left_tile:
                    new_tile.bottom_left = bottom_left_tile
                    bottom_left_tile.top_right = new_tile

            if column - offset < 6:
                bottom_right_tile = self.tiles[row + 1][column - offset + 1]
                if bottom_right_tile:
                    new_tile.bottom_right = bottom_right_tile
                    bottom_right_tile.top_left = new_tile
        return
        

    def _concat_tile_repr(self, tiles_repr, offset):
        tiles_lines = [tile.split('\n')[:-1] for tile in tiles_repr]
        num_lines = len(tiles_lines[0])
        concat_repr = ''
        for i in range(num_lines):
            concat_repr += offset + ''.join([tile[i] for tile in tiles_lines]) + '\n'

        return concat_repr

    def _compact_repr(self, board_repr):
        vertical_join_re = ' *-+\n *-+'
        board_repr = re.sub(vertical_join_re, '-'*(12*7+6), board_repr)
        return board_repr

    def __repr__(self):
        board_repr = ''
        for i in range(self.ncols):
            offset = '' if i%2 == 0 else 6*' '
            row = self.tiles[i]
            
            tile_repr = []
            for j in range(self.nrows):
                tile = row[j]
                if tile:
                    tile_repr.append(str(tile))
                else:
                    row_bound = '------------\n'
                    col_bound = '|          |\n'
                    empty_tile = row_bound + 3*col_bound + row_bound
                    tile_repr.append(empty_tile)
                    
            concat_row = self._concat_tile_repr(tile_repr, offset) 
            board_repr += concat_row

            board_repr = self._compact_repr(board_repr)

        return board_repr


if __name__ == '__main__':
    def randtile():
        color = Color(randrange(1,7))
        pattern = Pattern(randrange(1,7))
        return PatchTile(color, pattern)

    tile_matrix = []
    for i in range(7):
        rows = []
        for j in range(7):
            rows.append(randtile())
        tile_matrix.append(rows)

    board = QuiltBoard()
    for i in range(board.nrows):
        for j in range(board.ncols):
            board.add_tile(tile_matrix[i][j], i, j)

    with open('test.txt', 'w') as file:
        for i in range(30):
            row = randrange(0, 7)
            col = randrange(0, 7)
            tile = board.tiles[row][col]
            
            print("Row: {}, Col: {}".format(row+1, col+1), file=file)
            print("Top left:", file=file)
            print(tile.top_left, file=file)
            print("Top Right:", file=file)
            print(tile.top_right, file=file)
            print("Left:", file=file)
            print(tile.left, file=file)
            print("Right:", file=file)
            print(tile.right, file=file)
            print("Bottom left:", file=file)
            print(tile.bottom_left, file=file)
            print("Bottom Right:", file=file)
            print(tile.bottom_right, file=file)

    print(board)
