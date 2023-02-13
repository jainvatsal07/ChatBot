#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import tkinter as tk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    
    [
        r"what is your name ?",
        ["I'm DAN, nice to meet you!"]
    ],
    
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", "Its fine, I am sure you will be able to do better next time."]
    ],
    
    [
        r"i am fine",
        ["Great to hear that", "Awesome, I am happy for you!"]
    ],
    
    [
        r"quit",
        ["Bye bye, take care. Have a great day!"]
    ],
    
    [
        r"how are you ?",
        ["I'm fine", "I am good, how about you?"]
    ],
    
    [
        r"what is your purpose ?",
        ["I am here to help you", "I am here to answer your questions", "My purpose is to assist you with anything you need."]
    ],
    
    [
        r"what can you do ?",
        ["I can do anything you need, just ask me!", "I can provide information, answer questions, and help you with anything you need.", "I am here to help with anything, just let me know!"]
    ],
    
    [
        r"what is your favorite color ?",
        ["As an AI, I do not have the ability to have a favorite color."]
    ],
    
    [
        r"what is your favorite food ?",
        ["As an AI, I do not have the ability to eat food or have a favorite food."]
    ],
    
    [
        r"what is your favorite movie ?",
        ["As an AI, I do not have the ability to watch movies or have a favorite movie."]
    ],
    
    [
        r"what is your favorite book ?",
        ["As an AI, I do not have the ability to read books or have a favorite book."]
    ],
    
    [
        r"what is your favorite music ?",
        ["As an AI, I do not have the ability to listen to music or have a favorite genre of music."]
    ],
    
    [
        r"what is your favorite hobby ?",
        ["As an AI, I do not have the ability to have hobbies."]
    ],
    
    [
        r"what is the current date ?",
        ["I do not have access to the current date, I am sorry."]
    ],
    
    [
        r"what is the current time ?",
        ["I do not have access to the current time, I am sorry."]
    ],
    
    [
        r"what is the weather like today ?",
        ["I do not have access to current weather information, I am sorry."]
    ],
]

chatbot = Chat(pairs, reflections)

root = tk.Tk()
root.title("NLTK Chatbot")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

messages = tk.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
messages.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=messages.yview)

entry_field = tk.Entry(root, font=("Arial", 10))
entry_field.pack(pady=5)

def send_message():
    user_input = entry_field.get()
    messages.insert(tk.END, "You: " + user_input)
    response = chatbot.respond(user_input)
    messages.insert(tk.END, "DAN: " + response)
    entry_field.delete(0, tk.END)
    
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()


# In[ ]:




