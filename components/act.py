import pygame
from .. import components



class Act:
    """You can write:
    *   `self.On_Handle`
    *   `self.On_Render`
    *   `self.On_Open`
    *   `self.On_Close`
    """


    def __init__(self) -> None:
        """"""

        self.surface:pygame.Surface = pygame.display.get_surface()
        ''''''


    # Expendable Call functions
    def On_Open(self) -> None:
        """Called upon this act's open."""
    def On_Close(self) -> None:
        """Called upon this act's close."""

    # Expendable Handle functions
    def Tick(self) -> None:
        """"""

    def Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame event when this act runs.
        \n When writing this function, pass event to all scenes, that opened.
        """


    def Render(self) -> None:
        """Renders this act, when it runs.
        \n When writing this function, render all opened scenes.
        """
