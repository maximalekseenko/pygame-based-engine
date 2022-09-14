import pygame
from .. import components



class Act:
    """Act is a big step in your application. for exaple, main menu, game map and game level can be three different acts.
    \n When writing your act, write next functions:
    *   `On_Hande` - for handling clicks, keys and other pygame events;
    *   `On_Render` - for rendering elements this act have.
    \n You can also take a look at:
    *   `On_Tick` - for some actions before handleing and rendering.
    *   `On_Open` - for some variables, that need to be set, before this act appears.
    *   `On_Close` - for some variables to save at the end.
    """


    def __init__(self) -> None:
        """"""

        self.surface:pygame.Surface = pygame.display.get_surface()
        ''''''




    # -----OPEN-----
    def Open(self) -> None:
        """Opens this act if closed.
        \n (don't misstake this with expendable `On_Open`)
        """
        self.On_Open()


    def On_Open(self) -> None:
        """Expendable.
        \n Called when this act opens.
        """


    # -----CLOSE-----
    def Close(self) -> None:
        """Closes this act if opened.
        \n (don't misstake this with expendable `On_Close`)
        """
        self.On_Close()


    def On_Close(self) -> None:
        """Expendable.
        \n Called when this act closes.
        """


    # -----HANDLE-----
    def Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame event when this act runs.
        \n When writing this function, pass event to all scenes, that opened.
        """

        self.On_Handle(event)


    def On_Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame event when this act runs.
        \n When writing this function, pass event to all scenes, that opened.
        """

    # -----RENDER-----
    def On_Render(self) -> None:
        """Renders this act, when it runs.
        \n When writing this function, render all opened scenes.
        """
        self.On_Render()

    def On_Render(self) -> None:
        """Renders this act, when it runs.
        \n When writing this function, render all opened scenes.
        """


    # -----TICK-----
    def Tick(self) -> None:
        """"""

    def On_Tick(self) -> None:
        """"""


