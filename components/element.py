import pygame
from .. import components



class Element:
    """
    """


    def __init__(self, scene, base:pygame.Surface|pygame.Rect|None=None, surface_flags:int=None) -> None:
        """
        *   `self.scene = scene`
        *   `self.rect = pygame.Rect(rect)`
        *   `self.exists = exists`
        """

        self.scene:components.Scene = scene
        ''''''

        self.surface_flags:int = surface_flags

        self._surface:pygame.Surface
        self._rect:pygame.Rect

        # set surface and rect
        if base == None: self.rect = pygame.Rect(0, 0, 0, 0)
        elif type(base) == pygame.Surface: self.surface = base
        elif type(base) == pygame.Rect: self.rect = base
        elif type(base) in [list, tuple]: self.rect = pygame.Rect(base)
        else: raise TypeError("Wrong base type.")
        

    @property
    def surface(self) -> pygame.Surface:
        return self._surface


    @surface.setter
    def surface(self, value:pygame.Surface) -> None:
        self._surface = value
        self._rect = value.get_rect()


    @property
    def rect(self) -> pygame.Rect:
        return self._rect


    @rect.setter
    def rect(self, value:pygame.Rect) -> None:
        self._rect = value
        if self.surface_flags == None:
            self._surface = pygame.Surface(value.size)
        else: self._surface = pygame.Surface(value.size, self.surface_flags)


    # -----UPDATE-----
    def Update(self):
        """Update this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Update`)
        """

        self.On_Update()
        return True

    
    def On_Update(self):
        """Called to update this scene.
        \n (For calling, use `Update`)
        """


    # -----TICK-----
    def Tick(self) -> None:
        """Does some action for this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Tick`)
        """
    
        self.On_Tick()
        return True


    def On_Tick(self) -> None:
        """Called for making some actions for the scene.
        \n (For calling, use `Tick`)
        """


    # -----RENDER-----
    def Render(self) -> None:
        """Renders this scene's content on `target` pygame.Surface.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Render`)
        """

        self.On_Render()
        return True


    def On_Render(self) -> None:
        """Called to render this scene's content on `target` surface.
        \n (For calling, use `Render`)
        """


    # -----HANDLE-----
    def Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame's `event` for this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Handle`)
        """

        self.On_Handle(event)
        return True


    def On_Handle(self, event:pygame.event.Event) -> None:
        """Called to handle given pygame event.
        \n (For calling, use `Handle`)
        """
        
