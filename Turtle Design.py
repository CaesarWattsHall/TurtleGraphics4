# Python program to draw 
# Rainbow Benzene 
# using Turtle Programming 
import turtle 
colors = ['#05668d', '#028090', '#00a896', '#02c39a', '#f0f3bd', '#FFFFFF'] 
t = turtle.Pen() 
turtle.bgcolor('#000000') 
for x in range(360): 
	t.pencolor(colors[x%6]) 
	t.width(x/100 + 1) 
	t.forward(x) 
	t.left(59) 
