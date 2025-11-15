import random
import string

def generate_wordsearch(grid_size, words):
    # Create an empty grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Function to place a word in the grid
    def place_word(word):
        word_length = len(word)
        placed = False

        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, grid_size - 1)
                col = random.randint(0, grid_size - word_length)
                if all(grid[row][col + i] == ' ' for i in range(word_length)):
                    for i in range(word_length):
