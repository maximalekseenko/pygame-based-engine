import pygame
from typing import Union



from .. import components



class Element:
    """
    """


    def __init__(self, scene, rect=None, exists=True) -> None:
        """
        *   `self.scene = scene`
        *   `self.rect = pygame.Rect(rect)`
        *   `self.exists = exists`
        """

        self.scene:components.Scene = scene
        ''''''

        if rect == None: rect = (0,0,0,0)
        self.rect:pygame.Rect = pygame.Rect(rect)
        ''''''

        self.exists:bool = exists
        ''''''
        


    # -----UPDATE-----
    def Update(self):
        """Update this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Update`)
        """

        # if closed
        if not self.exists: return False

        # if opened
        self.On_Update()
        return True

    
    def On_Update(self):
        """Called to update this scene.
        \n (For calling, use `Update`)
        """


    # -----TICK-----
    def Tick(self, delta:float=0.0) -> None:
        """Does some action for this scene.
        \n If this scene is closed, does nothing and returns `False`.
        \n (For codding, use `On_Tick`)
        """
        
        # if closed
        if not self.exists: return False

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
        if not self.exists: return False

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
        if not self.exists: return False

        # if opened
        self.On_Handle(event)
        return True


    def On_Handle(self, event:pygame.event.Event) -> None:
        """Called to handle given pygame event.
        \n (For calling, use `Handle`)
        """
        
