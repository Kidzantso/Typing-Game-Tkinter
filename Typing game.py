from tkinter import *
import random
import pandas as pd

df = pd.read_csv('English.csv')
df.drop('CEFR', inplace=True, axis=1)
df.columns=['words']
Word = df['words']
Word = Word.values
score = 0
timeleft = 30

def Reset():
    global timeleft
    global score
    timeleft=30
    score=0
    startGame

def startGame(event):
	if timeleft == 30:
		countdown()
	nextWord()
 
def nextWord():
	global score
	global timeleft
	if timeleft > 0:
		e.focus_set()
		if e.get() == Word[0]:			
			score += 1
		e.delete(0, 'end')
		random.shuffle(Word)
		label.config(text = str(Word[0]))
		
		scoreLabel.config(text = "Score: " + str(score))
	else:e.delete(0, 'end');root.focus()

def countdown():
	global timeleft
	if timeleft > 0:
		timeleft -= 1
		timeLabel.config(text = "Time left: "+ str(timeleft))						
		timeLabel.after(1000, countdown)


root = Tk()
root.title("Typing Game")
root.geometry("375x200")
instructions = Label(root, text = "Type the greatest numbers of words you can in 30 seconds",font = ('Helvetica', 12),bg="#5A47A5")
instructions.pack() 
scoreLabel = Label(root, text = "Press enter to start and after you press reset to restart again",font = ('Helvetica', 12),bg="#5A47A5")
scoreLabel.pack()
timeLabel = Label(root, text = "Time left: "+str(timeleft), font = ('Helvetica', 12),bg="#5A47A5")			
timeLabel.pack()
label = Label(root, font = ('Helvetica', 12),bg="#5A47A5")
label.pack()
e = Entry(root)
e.configure({"background": "#6F6F6F"})
buttonStart = Button(root, text ="Reset",command = lambda : Reset(),width=17,bg="#FF0101", activebackground="#FF0101")
root.bind('<Return>', startGame)
e.pack()
buttonStart.pack()
e.focus_set()
root.geometry('500x500')
root.resizable(width=False, height=False)
root.configure(bg="#5A47A5")
root.mainloop()
