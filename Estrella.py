from turtle import *

setup(800, 600)
title("Estrella de cuatro picos")
screensize(900, 800)

hideturtle()

pensize(4)
fillcolor("blue")
begin_fill()
goto(60, 260)
goto(145, -1)
goto(399, -60)
goto(145, -120)
goto(60, -350)
goto(0,-120)
goto(-250,-60)
goto(0, 0)
end_fill()
