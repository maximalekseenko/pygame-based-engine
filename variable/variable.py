from ..components import Act


mouse_press_position = (-1, -1)


_current_act:Act = Act()

def Get_Current_Act() -> Act:
    return _current_act

def Set_Current_Act(value:Act) -> None:
    global _current_act

    # close old act
    _current_act.On_Close()

    # open new act
    _current_act = value
    _current_act.On_Open()