import pygame
from typing import overload, Union



from ..variable import variable



class Element:
    """Basic element.
    \n use to create Custom elements.
    """


    def __init__(self, parent,

            # position and scale
            x:int, 
            y:int, 
            width:int, 
            height:int,

            # anchor
            anchor_x:str="left",
            anchor_y:str="top",
            self_anchor_x:str="left",
            self_anchor_y:str="top",
            ) -> None:
        """
        \n Position and Scale.
        *   `x` - `int` or `str%`. Distance from `parent_anchor_x` to `anchor_x`. 
        *   `y` - `int` or `str%`. Distance from `parent_anchor_y` to `anchor_y`. 
        *   `width` - `int` or `str%`. Distance from left to right. 
        *   `height` - `int` or `str%`. Distance from top to bottom.
        \n  Anchors to count position from:
        *   `anchor_x` - Relative to self. Possible values: `"left"`, `"center"`, `"right"`.
        *   `anchor_y` - Relative to self. Possible values: `"top"`, `"center"`, `"bottom"`.
        *   `parent_anchor_x` - Relative to parent_rect. Possible values: `"left"`, `"center"`, `"right"`.
        *   `parent_anchor_y` - Relative to parent_rect. Possible values: `"top"`, `"center"`, `"bottom"`.
        """

        # set parent surface
        self.parent = parent
        '''Parent of this element.'''

        # collision rectangle
        self.rect:pygame.Rect = pygame.Rect(0, 0, 0, 0)
        '''`pygame.Rect` for collision logic.'''
        
        # position and scale
        self._x = x
        self.Validate_x()
        self._y = y
        self.Validate_y()
        self._width = width
        self.Validate_width()
        self._height = height
        self.Validate_height()

        # anchors
        self._anchor_x = anchor_x
        self.Validate_anchor_x()
        self._anchor_y = anchor_y
        self.Validate_anchor_y()
        self._self_anchor_x = self_anchor_x
        # self.Validate_self_anchor_x()
        self._self_anchor_y = self_anchor_y
        # self.Validate_self_anchor_y()

        self.Math_Collision_Rectangle()
        

    # ---------- position and scale ----------
    @property
    def x(self) -> int: return self._x

    @x.setter
    def x(self, value:Union[int, float, str]):
        """Distance from `parent_anchor_x` to `anchor_x`.
        \n Can be `int`, `float` or `str%` (percent form `parent_rect`. Example: `"16%"`)
        """

        self._x = value
        self.Validate_x()
        self.Math_Collision_Rectangle()        

    def Validate_x(self) -> None:
        """Validate x and raise if wrong."""

        if type(self._x) not in [int, float, str]: raise TypeError(f"'{self._x}' is wrong value for x. Must be int, float or str%")
        if type(self._x) == str and (self._x[-1] != '%' or not self._x[:-1].isnumeric()): raise TypeError(f"'{self._x}' is wrong value for x. Must be int, float or str%")

    
    @property
    def y(self): return self._y

    @y.setter
    def y(self, value:Union[int, float, str]):
        """Distance from `parent_anchor_y` to `anchor_y`.
        \n Can be `int`, `float` or `str%` (percent form `parent_rect`. Example: `"16%"`)
        """
        
        self._y = value
        self.Validate_y()
        self.Math_Collision_Rectangle()

    def Validate_y(self) -> None:
        """Validate y and raise if wrong."""

        if type(self._y) not in [int, float, str]: raise TypeError(f"'{self.y}' is wrong value for y. Must be int, float or str%")
        if type(self._y) == str and (self._y[-1] != '%' or not self._y[:-1].isnumeric()): raise TypeError(f"'{self.y}' is wrong value for y. Must be int, float or str%")


    @property
    def width(self): return self._width

    @width.setter
    def width(self, value:Union[int, float, str]):
        """Distance from left to right.
        \n Can be `int`, `float` or `str%` (percent form `parent_rect`. Example: `"16%"`)
        """
        
        self._width = value
        self.Validate_width()
        self.Math_Collision_Rectangle()

    def Validate_width(self) -> None:
        """Validate width and raise if wrong."""
        if type(self._width) not in [int, float, str]: raise TypeError(f"'{self._width}' is wrong value for width. Must be int, float or str%")
        if type(self._width) == str and (self._width[-1] != '%' or not self._width[:-1].isnumeric()): raise TypeError(f"'{self._width}' is wrong value for width. Must be int, float or str%")


    @property
    def height(self): return self._height

    @height.setter
    def heigth(self, value:Union[int, float, str]):
        """Distance from top to bottom.
        \n Can be `int`, `float` or `str%` (percent form `parent_rect`. Example: `"16%"`)
        """
        
        self._height = value
        self.Validate_height()
        self.Math_Collision_Rectangle()

    def Validate_height(self) -> None:
        """Validate height and raise if wrong."""

        if type(self._height) not in [int, float, str]: raise TypeError(f"'{self._height}' is wrong value for height. Must be int, float or str%")
        if type(self._height) == str and (self._height[-1] != '%' or not self._height[:-1].isnumeric()): raise TypeError(f"'{self._height}' is wrong value for height. Must be int, float or str%")

  

    # ---------- anchors ----------
    @property
    def anchor_x(self) -> str: return self._anchor_x

    @anchor_x.setter
    def anchor_x(self, value:str):
        """Anchor to count position from. 
        \n Relative to self. 
        \n Possible values: `"left"`, `"center"`, `"right"`
        """

        self._anchor_x = value
        self.Validate_anchor_x()
        self.Math_Collision_Rectangle()       

    def Validate_anchor_x(self):
        """Validate anchor_x and raise if wrong."""

        if self._anchor_x not in ["left", "center", "right"]: raise TypeError(f"{self.anchor_x} wrong value for anchor_x. Can be \"left\", \"center\" or \"right\"")


    @property
    def anchor_y(self) -> str: return self._anchor_y
    
    @anchor_y.setter
    def anchor_y(self, value:str):
        """Anchor to count position from. 
        \n Relative to self. 
        \n Possible values: `"top"`, `"center"`, `"bottom"`
        """

        self._anchor_y = value
        self.Validate_anchor_y()
        self.Math_Collision_Rectangle()       

    def Validate_anchor_y(self):
        """Validate anchor_y and raise if wrong."""

        if self._anchor_y not in ["top", "center", "bottom"]: raise TypeError(f"{self.anchor_y} wrong value for anchor_y. Can be \"top\", \"center\" or \"bottom\"")


    @property
    def parent_anchor_x(self) -> str: return self._parent_anchor_x
    
    @parent_anchor_x.setter
    def parent_anchor_x(self, value:str):
        """Anchor to count position from. 
        \n Relative to parent_rect. 
        \n Possible values: `"left"`, `"center"`, `"right"`
        """

        self._parent_anchor_x = value
        self.Validate_parent_anchor_x()
        self.Math_Collision_Rectangle()       

    def Validate_parent_anchor_x(self):
        """Validate parent_anchor_x and raise if wrong."""

        if self._parent_anchor_x not in ["left", "center", "right"]: raise TypeError(f"{self.parent_anchor_x} wrong value for parent_anchor_x. Can be \"left\", \"center\" or \"right\"")
    

    @property
    def parent_anchor_y(self) -> str: return self._parent_anchor_y
    
    @parent_anchor_y.setter
    def parent_anchor_y(self, value:str):
        """Anchor to count position from. 
        \n Relatzive to parent_rect. 
        \n Possible values: `"top"`, `"center"`, `"bottom"`
        """

        self._parent_anchor_ = value
        self.Validate_parent_anchor_y()
        self.Math_Collision_Rectangle()       

    def Validate_parent_anchor_y(self):
        """Validate parent_anchor_y and raise if wrong."""

        if self._parent_anchor_y not in ["top", "center", "bottom"]: raise TypeError(f"{self.parent_anchor_y} wrong value for parent_anchor_y. Can be \"top\", \"center\" or \"bottom\"")
          


    # ---------- Collision Rect ----------
    def Math_Collision_Rectangle(self) -> None:
        """"""

        # get position and scale
        if type(self._x) in [int, float]: x = self._x
        if type(self._x) == str: x = self.parent.rect.x * int(self._x[:-1]) / 100
        if type(self._y) in [int, float]: y = self._y
        if type(self._y) == str: y = self.parent.rect.y * int(self._y[:-1]) / 100
        if type(self._width) in [int, float]: width = self._width
        if type(self._width) == str: width = self.parent.rect.width * int(self._width[:-1]) / 100
        if type(self._height) in [int, float]: height = self._height
        if type(self._height) == str: height = self.parent.rect.height * int(self._height[:-1]) / 100

        self.rect.x = x
        self.rect.y = y
        self.rect.width = width 
        self.rect.height = height

        # anchors x
        # if self._anchor_x == "left":
        #     if self.__anchor_x == "left": 
        #         self.rect.left = self.rect.x + self.parent.rect.left
        #     elif self.__anchor_x == "center": 
        #         self.rect.left = self.rect.x + self.parent.rect.centerx
        #     elif self.__anchor_x == "right": 
        #         self.rect.left = self.rect.x + self.parent.rect.right
        # elif self._anchor_x == "center":
        #     if self.__anchor_x == "left": 
        #         self.rect.centerx = self.rect.x + self.parent.rect.left
        #     elif self.__anchor_x == "center": 
        #         self.rect.centerx = self.rect.x + self.parent.rect.centerx
        #     elif self.__anchor_x == "right": 
        #         self.rect.centerx = self.rect.x + self.parent.rect.right
        # elif self._anchor_x == "right":
        #     if self.__anchor_x == "left": 
        #         self.rect.right = self.rect.x + self.parent.rect.left
        #     elif self.__anchor_x == "center": 
        #         self.rect.right = self.rect.x + self.parent.rect.centerx
        #     elif self.__anchor_x == "right": 
        #         self.rect.right = self.rect.x + self.parent.rect.right

        # # anchors y
        # if self._anchor_y == "top":
        #     if self.__anchor_y == "top": 
        #         self.rect.top = self.rect.y + self.parent.rect.top
        #     elif self.__anchor_y == "center": 
        #         self.rect.top = self.rect.y + self.parent.rect.centery
        #     elif self.__anchor_y == "bottom": 
        #         self.rect.top = self.rect.y + self.parent.rect.bottom
        # elif self._anchor_y == "center":
        #     if self.__anchor_y == "top": 
        #         self.rect.centery = self.rect.y + self.parent.rect.top
        #     elif self.__anchor_y == "center": 
        #         self.rect.centery = self.rect.y + self.parent.rect.centery
        #     elif self.__anchor_y == "bottom": 
        #         self.rect.centery = self.rect.y + self.parent.rect.bottom
        # elif self._anchor_y == "bottom":
        #     if self.__anchor_y == "top": 
        #         self.rect.bottom = self.rect.y + self.parent.rect.top
        #     elif self.__anchor_y == "center": 
        #         self.rect.bottom = self.rect.y + self.parent.rect.centery
        #     elif self.__anchor_y == "bottom": 
        #         self.rect.bottom = self.rect.y + self.parent.rect.bottom


    def Handle(self, event:pygame.event.Event) -> None:
        """"""


    def Render(self, target:pygame.Surface) -> None:
        """Blit element on target"""
