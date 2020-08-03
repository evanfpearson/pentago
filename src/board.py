from typing import List
from src.block import Block
from src.marble import Marble


class Board:
    def __init__(self, blocks: List[Block]):
        self.__blocks = blocks

    def get_full_array(self) -> List[List[Marble]]:
        rows = []
        return [[Marble('black')]]

