from turtle import*

def damier(n):
    up()
    goto(-n*100/2,-n*100/2)
    down()
    setheading(0)
    for j in range(n):
        for i in range(n):
                if i%2==j%2:
                    pencolor('black')
                    begin_fill()
                for i in range(4):
                    forward(100)
                    left(90)
                forward(100)
                end_fill()