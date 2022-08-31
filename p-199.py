from email import message
import socket
from threading import Thread
import random
from tkinter.messagebox import QUESTION

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'

port = 8000



server.bind((ip_address, port))
server.listen()

print("Server is running .... ")
index = []

question=[
    "What is the Italian word for pie? \n a.Mozarella \n b.Pasty \n c.Patty \n d.Pizza"
]
answers = ["d"]

def get_random_QnAs(conn):
    random_index=random.randint(0.len(question)-1)
    random_question= question[random_index]
    random_answer=answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index,random_question , random_answer

def remove_question(index):
    question.pop(index)
    answers.pop(index)

def clientThread(conn):
    score=0
    conn.send("Welcome to the quiz".encode('utf-8'))
    conn.send("YOu will recieve a MCQ question. Answer correctly".encode('utf-8'))
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index,question,answers  = get_random_QnAs(conn)
    while True:
        try:
            message=conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score+=1
                    conn.send(f"Bravo ! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect! Beter luck nest time\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answers=get_random_QnAs(conn)
            else:
                remove(conn)
        
        except:
            continue
