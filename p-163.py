# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:46:58 2023

@author: Ankan Datta
"""

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("DETECTING CARDIOVASCULAR SYMPTOMS")
root.geometry("700x450")
root.configure(bg = "pink")

question1_radioButton = StringVar(value = "0")

question1 = Label(root, text = "Do you experience shortness of breath during routine activities?", bg = "pink")
question1.pack()
question1_r1 = Radiobutton(root, text = "Yes", variable=question1_radioButton, value = "yes", bg = "pink")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "No", variable=question1_radioButton, value = "no", bg = "pink")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")

question2 = Label(root, text = "Do you have swelling in the feet/ ankles/ legs(shoes fell tighter) or abdomen?", bg = "pink")
question2.pack()
question2_r1 = Radiobutton(root, text = "Yes", variable=question2_radioButton, value = "yes", bg = "pink")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "No", variable=question2_radioButton, value = "no", bg = "pink")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")

question3 = Label(root, text = "Do you feel any of this symptoms - confusion, disorientation or loss of memory?", bg = "pink")
question3.pack()
question3_r1 = Radiobutton(root, text = "Yes", variable=question3_radioButton, value = "yes", bg = "pink")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "No", variable=question3_radioButton, value = "no", bg = "pink")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")

question4 = Label(root, text = "Do you experience shortness of breath while at rest/ lying down?", bg = "pink")
question4.pack()
question4_r1 = Radiobutton(root, text = "Yes", variable=question4_radioButton, value = "yes", bg = "pink")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "No", variable=question4_radioButton, value = "no", bg = "pink")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")

question5 = Label(root, text = "Do you experience persistant wheezing / coughing that produces white pink blood tinged mucus?", bg = "pink")
question5.pack()
question5_r1 = Radiobutton(root, text = "Yes", variable=question5_radioButton, value = "yes", bg = "pink")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "No", variable=question5_radioButton, value = "no", bg = "pink")
question5_r2.pack()

def cardiovascular_score():
    score = 0
    if question1_radioButton.get() == "yes":
        score = score+10
        print(score)
    
    if question2_radioButton.get() == "yes":
        score = score+10
        print(score)
        
    if question3_radioButton.get() == "yes":
        score = score+10
        print(score)
        
    if question4_radioButton.get() == "yes":
        score = score+10
        print(score)
        
    if question5_radioButton.get() == "yes":
        score = score+10
        print(score)


    if score <= 10 :
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
    
    elif score > 10 and score <= 30 :
        messagebox.showinfo("Report", "You might perhaps to visit a doctor.")

    else :
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor")
    
btn = Button(root, text = "Show me report", command = cardiovascular_score)
btn.pack()

root.mainloop()