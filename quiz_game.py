# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:24:11 2020

@author: Preyash Patel
"""

#importing random librarey
import random

#question set
"""
question_list  is two
first dimention defines the question no
second dimention defines the question and answers with correct ans no
it is as follow
at 0th index: question,
at 1th index: option 1,
at 2th index: option 2,
at 3th index: option 3,
at 4th index: option 4,
at 5th index: Correect answer in range of 1 to 4
"""
question_list = [
        [
            ['The ratio between the length and the breadth of a rectangular park is 3 '],
            ['15360'],['153600'],["30720"],["307200"],[2]
            
        ],
        [
            ['a'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['b'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['c'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['d'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['e'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
                [
            ['If a man cycling along the boundary of the park at the speed of 12 km/hr completes'],
            ['15360'],['153600'],["30720"],["307200"],[2]
            
        ],
        [
            ['a'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['b'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['c'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['d'],
            ['x'],['y'],["z"],["s"],[4]
            
        ],
        [
            ['e'],
            ['x'],['y'],["z"],["s"],[4]
            
        ]
    ]

#function to return randimg q number
def qusNo():
    return random.sample(range(0, len(question_list)), 5)    

#calling the function for further use
list_of_q = qusNo()


#GUI Designing starting
from tkinter import *
window = Tk()
window.title("Quiz Time")
window.geometry("1000x500+400+100")

#defining required variables
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
checkvar4=IntVar()
checkvar5=IntVar()

strans=StringVar(window)
points = 0

#final methods to count result
def submitAns():
    global points
    points = 0
    if question_list[list_of_q[0]][-1][0] == int(checkvar1.get()):
        points += 1
    if question_list[list_of_q[1]][-1][0] == int(checkvar2.get()):
        points += 1
    if question_list[list_of_q[2]][-1][0] == int(checkvar3.get()):
        points += 1
    if question_list[list_of_q[3]][-1][0] == int(checkvar4.get()):
        points += 1    
    if question_list[list_of_q[4]][-1][0] == int(checkvar5.get()):
        points += 1
    strans.set(points)
    print(points)


"""
Here i am usoing dynamic variable to set row of content using row variable
and q for iterating the q no
qNo is to reduce the line editiong 
"""
#q1
row = 0
q = 0
qNo = list_of_q[q]
lblNo1 = Label(window,text = "Question 1:").grid(row = row, column = 0)
lblNo2 = Label(window,text = question_list[qNo][0]).grid(row = row+1)
lblNo3 = Label(window,text = "Select Answer").grid(row = row+2, column = 0)
rdb1 =Radiobutton(window,text=question_list[qNo][1],variable=checkvar1,value=1)
rdb1.grid(row=row+2,column=1)
rdb2 =Radiobutton(window,text=question_list[qNo][2],variable=checkvar1,value=2)
rdb2.grid(row=row+2,column=2)
rdb3 =Radiobutton(window,text=question_list[qNo][3],variable=checkvar1,value=3)
rdb3.grid(row=row+2,column=3)
rdb4 =Radiobutton(window,text=question_list[qNo][4],variable=checkvar1,value=4)
rdb4.grid(row=row+2,column=4)

#q2
row += 3
q += 1
qNo = list_of_q[q]
lblNo1 = Label(window,text = "Question 1:").grid(row = row, column = 0)
lblNo2 = Label(window,text = question_list[qNo][0]).grid(row = row+1)
lblNo3 = Label(window,text = "Select Answer").grid(row = row+2, column = 0)
rdb1 =Radiobutton(window,text=question_list[qNo][1],variable=checkvar2,value=1)
rdb1.grid(row=row+2,column=1)
rdb2 =Radiobutton(window,text=question_list[qNo][2],variable=checkvar2,value=2)
rdb2.grid(row=row+2,column=2)
rdb3 =Radiobutton(window,text=question_list[qNo][3],variable=checkvar2,value=3)
rdb3.grid(row=row+2,column=3)
rdb4 =Radiobutton(window,text=question_list[qNo][4],variable=checkvar2,value=4)
rdb4.grid(row=row+2,column=4)

#q3
row += 3
q += 1
qNo = list_of_q[q]
lblNo1 = Label(window,text = "Question 1:").grid(row = row, column = 0)
lblNo2 = Label(window,text = question_list[qNo][0]).grid(row = row+1)
lblNo3 = Label(window,text = "Select Answer").grid(row = row+2, column = 0)
rdb1 =Radiobutton(window,text=question_list[qNo][1],variable=checkvar3,value=1)
rdb1.grid(row=row+2,column=1)
rdb2 =Radiobutton(window,text=question_list[qNo][2],variable=checkvar3,value=2)
rdb2.grid(row=row+2,column=2)
rdb3 =Radiobutton(window,text=question_list[qNo][3],variable=checkvar3,value=3)
rdb3.grid(row=row+2,column=3)
rdb4 =Radiobutton(window,text=question_list[qNo][4],variable=checkvar3,value=4)
rdb4.grid(row=row+2,column=4)

#q4
row += 3
q += 1
qNo = list_of_q[q]
lblNo1 = Label(window,text = "Question 1:").grid(row = row, column = 0)
lblNo2 = Label(window,text = question_list[qNo][0]).grid(row = row+1)
lblNo3 = Label(window,text = "Select Answer").grid(row = row+2, column = 0)
rdb1 =Radiobutton(window,text=question_list[qNo][1],variable=checkvar4,value=1)
rdb1.grid(row=row+2,column=1)
rdb2 =Radiobutton(window,text=question_list[qNo][2],variable=checkvar4,value=2)
rdb2.grid(row=row+2,column=2)
rdb3 =Radiobutton(window,text=question_list[qNo][3],variable=checkvar4,value=3)
rdb3.grid(row=row+2,column=3)
rdb4 =Radiobutton(window,text=question_list[qNo][4],variable=checkvar4,value=4)
rdb4.grid(row=row+2,column=4)

#q5
row += 3
q += 1
qNo = list_of_q[q]
lblNo1 = Label(window,text = "Question 1:").grid(row = row, column = 0)
lblNo2 = Label(window,text = question_list[qNo][0]).grid(row = row+1)
lblNo3 = Label(window,text = "Select Answer").grid(row = row+2, column = 0)
rdb1 =Radiobutton(window,text=question_list[qNo][1],variable=checkvar5,value=1)
rdb1.grid(row=row+2,column=1)
rdb2 =Radiobutton(window,text=question_list[qNo][2],variable=checkvar5,value=2)
rdb2.grid(row=row+2,column=2)
rdb3 =Radiobutton(window,text=question_list[qNo][3],variable=checkvar5,value=3)
rdb3.grid(row=row+2,column=3)
rdb4 =Radiobutton(window,text=question_list[qNo][4],variable=checkvar5,value=4)
rdb4.grid(row=row+2,column=4)

#this is submit btn code
btnSubmit = Button(window, text = "Submit",command=submitAns).grid(row = row+3, column = 0)
lblNo1 = Label(window,text = "Answer: ").grid(row = row+4, column = 0)
txtAns = Entry(window,textvariable = strans).grid(row = row+4, column = 1)


window.mainloop()
