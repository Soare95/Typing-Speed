import tim
from tkinter import *
import random


window = Tk()
window.title("Typing Speed Test")
window.minsize(width=300, height=300)

initial = time.time()
used_words = []
unused_words = []


def get_random_word():
    words_list = ["car", "wisdom", "child", "pepper", "dentist", "horizon", "dungeon", "mother", "will", "human", "few",
                  "music", "bicycle", "road", "follow", "big", "sure", "simple", "money", "true", "lead", "age",
                  "paint", "much", "if", "end", "the", "own", "clear", "possible", "watch", "port", "stay",
                  "there", "has", "house", "speed", "together", "earth", "pound", "correct", "far", "day", "snow",
                  "left", "start", "how", "gold", "in", "move", "late", "during", "began", "pose", "study"]
    random_word = random.choice(words_list)
    used_words.append(random_word)
    return random_word


def get_next_word(event):
    if user_entry.get() == used_words[-1]:
        word_label.config(text=get_random_word())
        user_entry.delete(0, "end")
        check_time()


def check_time():
    global initial
    if time.time() - initial >= 60:
        number_of_words = len(used_words)
        word_label.config(text=f"You wrote {number_of_words}\n words in one minute!\nGood Job! ")


word_label = Label(text=get_random_word(), font=("Arial", 24, "bold"))
word_label.pack()

user_entry = Entry(width=20)
user_entry.focus()
user_entry.pack()

user_entry.bind("<Return>", get_next_word)


window.mainloop()
