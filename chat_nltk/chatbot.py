import tkinter as tk
import sqlite3
import nltk
import random
from tkinter import *
from PIL import ImageTk, Image




def get_response(sentence):
    cursor.execute('select b.sentence, b.sentiment from REQUEST a, RESPONSE b '
                   'where a.sentence = ? and a.intent_id=b.intent_id', (sentence,))
    row = cursor.fetchall()
    return row


def simplify(sentence):
    return sentence.strip().lower()

# w = None
# entry_value = None
# res_label = None


def stop_word_processing(sentence):
    postag = nltk.pos_tag(nltk.word_tokenize(sentence))
    stop_tag_list = ['RB', 'LS', 'FW', 'UH']
    print(postag)
    sentence = sentence.replace(' is', "'s")
    sentence = sentence.replace(' am', "'m")
    for letter in sentence:
        if not(letter.isalnum()):
            if letter == "'" or letter == ' ':
                continue
            sentence = sentence.replace(letter, '')
    for item in postag:
        if item[1] == 'RB' or item[1] == 'LS' or item[1] == 'FW' or item[1] == 'UH':
            sentence = sentence.replace(item[0], '')

    sentence = sentence.strip()
    sentence = sentence.replace('  ', ' ')
    return sentence


def set_ui():
    window = tk.Tk()
    window.title("Chatbot")
    window.geometry("300x400")
    window.configure(background='white')

    res_label = Label(text="Hello")
    entry_value = StringVar()

    req_entry = Entry(textvariable=entry_value)

    image_file_name = ["normal", "normal2", "awkward_smile",
                       "big_smile", "boast", "brrrr",
                       "confused", "confused2", "cry",
                       "difficult", "disorder", "kidding",
                       "kiss", "no_comment", "relief",
                       "sick", "sleep", "smile1",
                       "smile2", "wink"
                       ]
    images = []

    for fname in image_file_name:
        print("fname:"+fname)
        full_name = "emotion_icon/"+fname+".jpg"
        img = ImageTk.PhotoImage(Image.open(full_name))
        images.append(img)

    label = Label(text="Hobert").pack()

    w = tk.Label(window, image=img)
    w.pack(expand="yes")

    label = Label(text="응답").pack()

    res_label.pack()

    req_entry.pack()

    def on_click():
        num = random.randint(0, 19)
        # if w == None:
        #     return

        w.configure(image=images[num])
        origin_value = entry_value.get()

        target_value = stop_word_processing(origin_value)

        request = simplify(target_value)
        results = get_response(request)
        if len(results) > 0:
            value = random.choice(results)
            # print(results[0])
            res_label['text'] = value[0]

    b = tk.Button(window, text="입력", command=on_click).pack()

    #on_click()

    window.mainloop()


# initialize the connection to the database
connection = sqlite3.connect('chat_data.db')
cursor = connection.cursor()
set_ui()
