import pgzrun 

TITLE="QUIZ MASTER"
WIDTH=870
HEIGHT=650

square_box=Rect(0,0,880,80)
question_box=Rect(20,100,650,150)
anwsear_box1=Rect(20,270,300,150)
anwsear_box2=Rect(370,270,300,150)
anwsear_box3=Rect(20,450,300,150)
anwsear_box4=Rect(370,450,300,150)
timer_box=Rect(700,100,650,150)
skip_box=Rect(700,270,300,150)
answer_boxes=[anwsear_box1,anwsear_box2,anwsear_box3,anwsear_box4]
def draw():
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(square_box,"violet")
    screen.draw.filled_rect(question_box,"green")
    screen.draw.filled_rect(timer_box,"orange")
    screen.draw.filled_rect(skip_box,"yellow")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"blue")
pgzrun.go()