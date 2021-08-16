from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
flip_counter = None

############################## Create New Flash Card ###################################

data = pd.read_csv("data/french_words.csv")
data_list = data.to_dict(orient="records")

def get_new_card():
    global flip_counter
    if flip_counter:
        window.after_cancel(flip_counter)
    current_card = random.choice(data_list)
    canvas.itemconfigure(card_img, image=card_front_img)
    canvas.itemconfigure(card_title, text="French", fill="black")
    canvas.itemconfigure(card_word, text=f"{current_card['French']}", fill="black")
    flip_counter = window.after(3000, flip_card, current_card)

def flip_card(card):
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=f"{card['English']}", fill="white")
    canvas.itemconfigure(card_img, image=card_back_img)



################################# USER INTERFACE #######################################

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=get_new_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=get_new_card)
right_btn.grid(column=1, row=1)

get_new_card()

window.mainloop()