import turtle

def draw_triangle(length, depth):
    if depth == 0:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        draw_triangle(length/2, depth-1)
        turtle.forward(length/2)
        draw_triangle(length/2, depth-1)
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        draw_triangle(length/2, depth-1)
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)

# 초기 설정
turtle.speed(0)
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()

# 삼각형 그리기
draw_triangle(300, 4)

# 화면 유지
turtle.done()
