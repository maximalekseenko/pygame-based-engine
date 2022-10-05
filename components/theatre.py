from .. import components



import pygame



class Theatre:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        self.is_running = True
        self._current_act = components.Act()


    @property
    def current_act(self) -> components.Act:
        return self._current_act

    @current_act.setter
    def current_act(self, value:components.Act) -> None:

        # close old act
        self._current_act.On_Close()

        # open new act
        self._current_act = value
        self._current_act.On_Open()
    

    def Finish(self):
        self.On_Finish()
        self.is_running = False

    def On_Finish(self): pass

    def Update(self):
        self.On_Update()

    def On_Update(self): pass


    def Begin(self):

        # loop
        while self.is_running:
            # tick
            self.clock.tick(60)
            self.current_act.Tick()

            # handle
            for event in pygame.event.get():

                self.current_act.Handle(event)
                
                if event.type == pygame.QUIT:
                    self.is_running = False

            # render
            self.screen.fill('#ffffff')

            self.current_act.Render()

            pygame.display.update()


        pygame.quit()