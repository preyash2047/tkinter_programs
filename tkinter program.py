from tkinter import *

#event handlers or callback functions
#event handler for the calculate button
def calc_container():
    months=float(txtNumOfMonth.get())
    nights=float(txtdays.get())
    totalRate = 0
    #finding bmi
    #BMI = kilograms / (meters * meters)
    #finding total rate
    if months<=3:
        totalRate=nights * 80
    
    elif months<=6:
        totalRate=nights * 90
    
    elif months<=9:
        totalRate=nights * 120
    
    else:
        totalRate=nights * 100
    
    #output - review text formating
    #notice the use of the StringVar variables
    str_totalRate.set( "{:.2f}".format(totalRate) )
    #str_totalRate.set(totalRate)

#event handler for the exit button
def exit_program():
    frm.destroy()
  


#create the form - do this first
frm = Tk() #frm means form, it could be another name
frm.title("Coyote Inn")
frm.geometry('325x150')#set the form size

#add GUI controls, find a label
lblNumOfMonth = Label(frm, text="Enter number of months:", height=1, width=20)
lblNumOfMonth.grid(row=0, column=0)

#Entry is a single line text box in the python world
txtNumOfMonth = Entry (frm, width=8)
txtNumOfMonth.grid(row=0, column=1)

#row 1 controls
lbldays = Label(frm, text="Enter number of nights:", height=1, width=20)
lbldays.grid(row=1, column=0)

txtdays = Entry (frm, width=8)
txtdays.grid(row=1, column=1)

#row 2 controls
lblTextRate = Label(frm, text="Your total rate is:", height=1, width=12)
lblTextRate.grid(row=2, column=0)

str_totalRate = StringVar()
lblRate = Label(frm, text="", height=1, width=10, textvariable=str_totalRate)
lblRate.grid(row=2, column=1)


#add a couple buttons
#In the command = we bind the button press event handler to the control
#calc button
btnCalc = Button(frm, text="Calculate", command=calc_container, height=1, width=10)
btnCalc.grid(row=3, column=0)

#Exit button
btnExit = Button(frm, text="Exit", command=exit_program, height=1, width=10)
btnExit.grid(row=3, column=1)

# display the main form
frm.mainloop()