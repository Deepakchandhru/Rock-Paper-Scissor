import random
from tkinter import *
from PIL import Image, ImageTk

def rps_game(choice):
    global cs, ps
    pc = choice
    com = random.randint(0, 2)
    cc = choices[com]
    computer_choice_label.config(text=f"Computer choice: {cc}")
    user_choice_label.config(text=f"Your choice: {pc}")

    if pc == cc:
        result_label.config(text="No point")
    elif choices[(choices.index(pc) - 1) % 3] == cc:
        ps += 1
        result_label.config(text="You won the point")
    else:
        cs += 1
        result_label.config(text="Computer won the point")

    computer_score_label.config(text=f"Computer score: {cs}")
    user_score_label.config(text=f"Your score: {ps}")

    if ps == 5:
        result_label.config(text="You Won the game. Keep it up.")
        disable_buttons()
    elif cs == 5:
        result_label.config(text="Computer won the game. Better luck next time.")
        disable_buttons()

def disable_buttons():
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)

def reset_game():
    global cs, ps
    cs = 0
    ps = 0
    computer_score_label.config(text=f"Computer score: {cs}")
    user_score_label.config(text=f"Your score: {ps}")
    computer_choice_label.config(text="Computer choice:")
    user_choice_label.config(text="Your choice:")
    result_label.config(text="")
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissor_button.config(state=NORMAL)

cs = 0
ps = 0
choices = ["Rock", "Paper", "Scissor"]

root = Tk()
root.title("Rock Paper Scissors Game")

welcome_label = Label(root, text="...Welcome to the ROCK PAPER SCISSOR game...", font=("Calibri", 14))
welcome_label.pack()

user_choice_label = Label(root, text="Your choice:", font=("Calibri", 12))
user_choice_label.pack()

computer_choice_label = Label(root, text="Computer choice:", font=("Calibri", 12))
computer_choice_label.pack()

result_label = Label(root, text="", font=("Calibri", 12))
result_label.pack()

computer_score_label = Label(root, text=f"Computer score: {cs}", font=("Calibri", 12))
computer_score_label.pack()

user_score_label = Label(root, text=f"Your score: {ps}", font=("Calibri", 12))
user_score_label.pack()

frame = Frame(root)
frame.pack()

rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((120, 120)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((120, 120)))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png").resize((120, 120)))

rock_button = Button(frame, image=rock_img, command=lambda: rps_game("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = Button(frame, image=paper_img, command=lambda: rps_game("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissor_button = Button(frame, image=scissor_img, command=lambda: rps_game("Scissor"))
scissor_button.grid(row=0, column=2, padx=10, pady=10)

reset_button = Button(root, text="Play Again", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
