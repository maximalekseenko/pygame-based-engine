import pygame


from .. import components


class Scene:
    """Scene can be window, ui, pop-up menus.
    \n When writing your scene, write next functions:
    *   `On_Hande` - for handling clicks, keys and other pygame events;
    *   `On_Render` - for rendering elements this scene have.
    \n You can also take a look at:
    *   `On_Tick` - for some actions before handleing and rendering.
    *   `On_Open` - for some variables, that need to be set, before this scene appears.
    *   `On_Close` - for some variables to save at the end.
    """


    def __init__(self, act) -> None:
        """When writing, you can skip super, just add next lines: 
        *   `self.act = act`
        *   `self.is_opened = False`
        """
        
        self.act:components.Act = act
        '''Act, that contains this scene.'''

        self.is_opened:bool = False
        '''Is this scene opened.'''


    # -----TICK-----
    def Tick(self, delta:float=0.0) -> None:
        """Does some action for this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Tick`)
        """
        
        # if closed
        if not self.is_opened: return False

        # if opened
        self.On_Tick(delta)
        return True


    def On_Tick(self, delta:float=0.0) -> None:
        """Called for making some actions for the scene.
        \n (For calling, use `Tick`)
        """


    # -----RENDER-----
    def Render(self, target:pygame.Surface) -> None:
        """Renders this scene's content on `target` pygame.Surface.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Render`)
        """
        
        # if closed
        if not self.is_opened: return False

        # if opened
        self.On_Render(target)
        return True


    def On_Render(self, target:pygame.Surface) -> None:
        """Called to render this scene's content on `target` surface.
        \n (For calling, use `Render`)
        """


    # -----HANDLE-----
    def Handle(self, event:pygame.event.Event) -> None:
        """Handles pygame's `event` for this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Handle`)
        """
        
        # if closed
        if not self.is_opened: return False

        # if opened
        self.On_Handle(event)
        return True


    def On_Handle(self, event:pygame.event.Event) -> None:
        """Called to handle given pygame event.
        \n (For calling, use `Handle`)
        """
        

    # -----OPEN-----
    def Open(self) -> None:
        """Opens this scene.
        \n If this scene is opened already, does nothing and returns `False`.
        \n (For codding, use `On_Open`)
        """

        # if opened
        if self.is_opened: return False
        
        # if closed
        self.is_opened = True
        self.On_Open()
        return True


    def On_Open(self) -> None:
        """Called when this scene opens.
        \n (For calling, use `Open`)
        """


    # -----CLOSE-----
    def Close(self) -> None:
        """Closes this scene.
        \n If this scene is already closed, does nothing and returns `False`.
        \n (For codding, use `On_Close`)
        """

        # if closed
        if not self.is_opened: return False
        
        # on opened
        self.is_opened = False
        self.On_Close()
        return True


    def On_Close(self) -> None:
        """Called when this scene closes.
        \n (For calling, use `Close`)
        """


    # -----TOGGLE-----
    def Toggle(self) -> None:
        """Opens this scene if closed and closes if opend.
        \n (For codding, use `On_Open` and `On_Close`)
        """

        if self.is_opened: self.Close()
        else: self.Open()

