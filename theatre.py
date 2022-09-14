from .components import Theatre
import pygame

class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()
        self.font16 = pygame.font.Font(None,16)
