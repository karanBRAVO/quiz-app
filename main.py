import tkinter
from tkinter import *
import random


questions = [
    "Which of the following will not produce hydrogen gas ?",
    "Among the C-X bond (where, X = Cl, Br, I) the correct decreasing order of bond energy is:",
    "When excess of KI is added to copper sulphate solution: ?",
    "In general, the Boron Trihaides act as: ?",
    "Ammonia gas can be dried by: ?",
    "CsOH is: ?",
    "What are Oxoacids: ?",
    "The basic strength of which hydroxide is maximum ?",
    "Which of the following alkali metals has the least melting point? ?",
    "The hydration energy of Mg2+ is larger than that of ?",
]

answers_choice = [
    ["Reaction between Fe and dil. HCl","Reaction between Zn and NaOH","Reaction between Zn and conc. H2SO4","Electrolysis of NaCl in Nelsons cell",],
    ["C−I > C−Cl > C−Br","C−I > C−Br > C−Cl","C−Cl > C−Br > C−I","C−Br > C−Cl > C−I",],
    [" Cuprous iodide is formed","I2 is liberated","Potassium iodide is oxidized","All",],
    ["Strong Reducing agent","Lewis Acid","Lewis Base","Dehydrating agents",],
    ["Quick Lime","CaCl2","P2O5","Conc.H2SO4",],
    ["Slightly Acidic","Strongly Basic","Weakly Basic","Amphoteric",],
    ["Acid containing Oxygen"," Acid containing Sulphur"," Acid containing Carbon", "None of the Above"],
    ["LiOH","NaOH","Ca(OH)2","KOH",],
    ["Na","K","Rb","Cs",],
    ["Al3+","Na+","Be26","Mg3+",],
] 


answers = [2,2,3,1,0,1,0,3,3,1] # 0 = option1 , 1 = option2 , 2 = option3 , 3 = option4

user_answer = []


indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
    
        if x in indexes:
            continue
        else:
            indexes.append(x)
    # print(indexes)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border =0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas", 20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img =PhotoImage(file ="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text = "You Are EXCELLENT !!!")
    elif (score >= 10 and score < 20):
        img =PhotoImage(file ="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text = "Good\nYou Can Do Better !!!")
    else:
        img =PhotoImage(file ="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text = "You Should Work Hard !!!")

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)        

ques = 1
def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        calc()

def startquiz():
    global lblQuestion, r1 ,r2, r3, r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font =("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar =IntVar()
    radiovar.set(-1)


    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Who wanna be Chemistrionaire!!!")
root.geometry("750x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Chemstudent of the YEAR",
    font = ("Comic sans MS", 24, "bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief =FLAT,
    border = 0,
    command  = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text ="Read the Rules and\nClick Start Once you are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify ="center",
)
lblInstruction.pack(pady=(10,95))

lblRules = Label(
    root,
    text = "This quiz contain 15 questions\nYou will get 10sec to solve a question\nOnce you select a radio button that will be final choice\n Hence think before you select.",
    width = "100",
    font = ("Times",14),
    background ="#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()