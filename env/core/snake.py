import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """

        :param head_position: tuple
        :param direction_index: int
        :param length: int
        """

        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index

        self.alive = True

        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        :param action: int
        :return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        # Example: if snake looks left, pressing "left" or "right" buttons should change nothing
        if (self.current_direction_index != action) and (abs(self.current_direction_index - action) != 2):
            self.current_direction_index = action
        # Remove tail
        tail = self.blocks[-1]
        self.blocks = self.blocks[:-1]
        # Create new head
        new_head = tuple(map(sum, zip(self.blocks[0], DIRECTIONS[self.current_direction_index])))
        # Add new head
        self.blocks = [new_head] + self.blocks
        return new_head, tail
