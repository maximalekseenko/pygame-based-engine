# **Pygame based engine**

Simplyfies projec development by spliting complex logic to separed elements.

---

## **How the does this works**
This engine provides with next usefull elements: **Theatre**, **Act**, **Scene** and **Element**.

> <h3 align="center"> Theatre </h3>
>
> ---
>
> **Theatre** is the heart of the program. It handle all requests and global game managment. **Theatre** should also used to handle logic and hold data that may be requaired at any time of the program running (e.g. settings)
>
> ---
> 
> Take a look at usefull components of the **Theatre**:
> 
> - `.current_act` - **act** that is currently playing. By setting other **act**, `.Close()` will be called  for previous **act**, and `.Open()` for a new one.
> - `.Begin()` - function to run the main loop (! this functions finishes only after program finishes).
> - `.is_running` - boolean that is used to exit the main loop.
>
> ---
>
> **Theatre** can be used as it is by writing next lines of code in `main.py`:
> ```py
> from engine import Theatre
> theatre = Theatre()
>
> from mainmenu import Main_Menu_Act
> theatre.current_act = Main_Menu_Act()
> 
> theatre.Begin() 
> ```
> But i highly suggest to expand **theatre** for bigger projects.

> <h3 align="center"> Act </h3>
>
> **Act**

