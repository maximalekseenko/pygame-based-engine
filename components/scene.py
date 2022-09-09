import pygame


from .. import components


class Scene:
    """Window for your program.
    \n To create your window, create chield from this class.
    Add function `self.Reset` to your window. 
    In it fill `self.uielements` with elements, that will be present on this window.
    \n In pygame loop pass each event into `self.Handle`
    and render this window with `self.Render`

    \n There also some function for you to expend (read the doc of the function before touching!):
    *   `self.Open` - Actions, that happend on window openning.
    *   `self.Close` - Actions, that happend on window closeing.
    *   `self.Handle` - pygame.Event, for handleing.
    """


    def __init__(self, act, is_opened=False) -> None:
        """`surface` - `pygame.Surface` to blit on. If `None`, will be `pygame.display.get_surface()`."""
        
        self.act:components.Act = act
        '''Act, that contains this scene.'''

        self.rect:pygame.Rect = self.act.surface.get_rect()
        '''`pygame.Rect`, from `pygame.Surface`.'''
        
        self.elements:list[components.Element] = list()
        '''List of `Elements` on this window.'''

        self.is_opened = is_opened
        '''Is this window opened.'''

        self.mouse_press_position = (-1, -1)
        '''Position of the mouse click.'''

        # initilaze all components
        self.On_Start()


    def Toggle(self) -> None:
        """Opens self if closed, Closes if opened."""


    def Open(self) -> None:
        """Opens this window if closed.
        \n By default function checks if not already opend, and opens if not.
        \n For expending, wright `if not super().Open: return` at the start of your function.
        """

        # check not to open twice
        if self.is_opened: return False

        # open
        self.is_opened = True

        # for expending
        return True


    def Close(self) -> None:
        """Closes this window if opend.
        \n By default function checks if not already closed, and closes if not.
        \n For expending, wright `if not super().Close: return` at the start of your function.
        """

        # check not to close twice
        if not self.is_opened: return False

        # open
        self.is_opened = False

        # for expending
        return True


    def On_Start(self) -> None:
        """Called upon this act's creation."""


    def Render(self, target:pygame.Surface) -> None:
        """"""

        # do not render closed window
        if not self.is_opened: return False

        # blit elements
        for uielement in self.elements:
            uielement.Render(target)

        # for expending
        return True


    # Expendable Handle functions
    def On_Handle(self, event:pygame.event.Event) -> None:
        """Handle pygame event before elements."""
    def On_Late_Handle(self, event:pygame.event.Event) -> None:
        """Handle pygame event after elements."""


    def _Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame event to elements.
        \n You can expend this function by setting next functions:
        *   `self.On_Handle` - for handeling berofe elements,
        *   `self.On_Late_Handle` - for handeling after elements.
        """

        # if closed
        if not self.is_opened: return

        # elements
        for element in self.elements:
            element.Handle(event)

        if event.type == pygame.WINDOWRESIZED:
            self.rect = self.surface.get_rect()
            for element in self.uielements:
                element.parent_rect = self.rect
                element.Math_Collision_Rectangle()

        # return
        return True
