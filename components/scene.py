import pygame


from .. import components


class Scene:
    """Write next:
    *   `self.On_Handle`
    *   `self.On_Render`
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
    def Tick(self) -> None:
        """Called at the start of each cycle.
        \n (don't misstake this with expendable `On_Tick`)
        """
        
        if self.is_opened: self.On_Tick()


    def On_Tick(self) -> None:
        """Expendable.
        \n Used to do logic.
        """


    # -----RENDER-----
    def Render(self, target:pygame.Surface) -> None:
        """Render this scene on `target` pygame.Surface.
        \n (don't misstake this with expendable `On_Render`)
        """

        if self.is_opened: self.On_Render(target)


    def On_Render(self, target:pygame.Surface) -> None:
        """Expendable.
        \n Used to Render this scene content on `target` pygame.Surface.
        """


    # -----HANDLE-----
    def Handle(self, event:pygame.event.Event) -> None:
        """Handle `event` for this scene.
        \n (don't misstake this with expendable `On_Handle`)
        """

        if self.is_opened: self.On_Handle(event)


    def On_Handle(self, event:pygame.event.Event) -> None:
        """Expendable.
        \n Used to Handle pygame.event.Event that happend for this scene.
        """
        

    # -----OPEN-----
    def Open(self) -> None:
        """Opens this window if closed.
        \n (don't misstake this with expendable `On_Open`)
        """
        if self.is_opened: return
        
        self.is_opened = True
        self.On_Open()


    def On_Open(self) -> None:
        """Expendable.
        \n Used to set or reset variables when this scene is opened.
        """


    # -----CLOSE-----
    def Close(self) -> None:
        """Closes this window if opend.
        \n (don't misstake this with expendable `On_Close`)
        """

        if not self.is_opened: return
        
        self.is_opened = False
        self.On_Close()


    def On_Close(self) -> None:
        """Expendable.
        \n Used to set or reset variables when this scene is closed.
        """


    # -----TOGGLE-----
    def Toggle(self) -> None:
        """Opens this window if closed and closes this window if opend.
        \n (make a look at expendable `On_Open` and `On_Close`)
        """

        if self.is_opened: self.Close()
        else: self.Open()

