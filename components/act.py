import pygame
from ..variable import variable
from .. import components



class Act:
    """Expend next:
    """


    def __init__(self) -> None:

        self.scenes:list[components.Scene] = list()
        '''Scenes this act have.'''

        self.surface:pygame.Surface = pygame.display.get_surface()
        ''''''

        self.On_Start()

    # Expendable Call functions
    def On_Start(self) -> None:
        """Called upon this act's creation."""
    def On_Open(self) -> None:
        """Called upon this act's open."""
    def On_Close(self) -> None:
        """Called upon this act's close."""

    # Expendable Handle functions
    def On_Handle(self, event:pygame.event.Event) -> None:
        """Handle pygame event before scene."""
    def On_Late_Handle(self, event:pygame.event.Event) -> None:
        """Handle pygame event after scene."""


    def _Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame event to scene.
        \n You can expend this function by setting next functions:
        *   `self.On_Handle` - for handeling berofe scene,
        *   `self.On_Late_Handle` - for handeling after scene.
        """

        # scenes Handle
        for scene in self.scenes:
            if scene.is_opened:
                scene.On_Handle(event)
                scene._Handle(event)
                scene.On_Late_Handle(event)


    def Render(self) -> None:
        """"""

        for scene in self.scenes:
            if scene.is_opened:
                scene.Render(self.surface)
