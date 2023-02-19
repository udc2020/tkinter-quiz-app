#       That Script Made By UltrasDzCoder
#       Script : Quiz App Tkinter 
#       author : UltrasDzCoder 


from tkinter import *
from app.config import *
from app.db import Db


class App(Tk):
    score: int
    player_name: str
    next_page: int
    str_var: str

    def __init__(self) -> None:
        super().__init__()

        self.score = 0

        self.player_name = ""
        self.next_page = 0

        self.str_var = StringVar()
        self.str_var.set(f"Score:{self.score}")

        self.Gui()

    def Gui(self):
        # Title
        self.title(TITLE)

        # Center Window
        self.center_app()

        # Background app
        self.config(
            bg=PRIMARY
        )

        # Add Name of this Player
        self.add_player_name_gui()

    def add_player_name_gui(self):
        self.cleaning_frames()

        # Reset player Score 
        self.score = 0
        self.str_var.set(f"Score:{self.score}")

        # 
        frame = Frame(self)
        frame.config(
            pady=(APP_HIEGHT/2)-100,
            height=5,
            bg=PRIMARY
        )
        frame.pack()

        question = Label(frame,
                         text="Your Name",
                         pady=10,
                         padx=20,
                         bg=PRIMARY,
                         fg="white",
                         font=("Arial", 30)
                         )
        question.pack()

        player_name = Text(
            frame,
            height=1,
            width=30,
            bg=PRIMARY,
            border=2,
            font=("Arail", 20),
            fg="white",
            pady=3,
            padx=10
        )
        player_name.pack(pady=10,)

        send_btn = Button(
            frame,
            text="Lets Start",
            padx=5,
            pady=3,
            border=2,
            relief=FLAT,
            font=("Arail", 14),
            command=lambda:  self.start_game(
                player_name.get("1.0", "end").strip())
        )
        send_btn.pack()


    def main_page(self):
        self.cleaning_frames()

        frame = Frame(self)
        frame.config(
            pady=(APP_HIEGHT/2)-300,
            height=5,
            bg=PRIMARY,
            padx=50

        )
        frame.pack()

        Label(frame,
              text="Quiz App",
              pady=10,
              padx=30,
              bg=PRIMARY,
              fg="white",
              font=("Arial", 30),
              ).pack()

        data = Db()

        for i in range(data.get_list_len()):
            
            for quiz in data.get_list_index(i):
                Button(frame, width=5, text=quiz, fg=PRIMARY, bg="white",
                       font=("Arial", 20),
                       relief=FLAT,
                       command=lambda quiz=quiz, i=i: self.indecator(
                           quiz, i)
                       ).pack(side=LEFT, padx=5)

    def indecator(self, quiz, i):
        self.cleaning_frames()

        data = Db()
        quizes_list = data.get_list_quizes(i, quiz)

        self.quiz_page_gui(quizes_list)

    def quiz_page_gui(self, quizes_list):
        self.cleaning_frames()

        q = quizes_list[self.next_page]['Q']
        c = quizes_list[self.next_page]['C']
        a = quizes_list[self.next_page]['A']

        Label(self, textvariable=self.str_var, bg=PRIMARY,
              fg="white",
              font=("Arial", 30),
              justify=RIGHT,
              width=100
              ).pack(pady=2)

        frame = Frame(self)
        frame.config(
            pady=(APP_HIEGHT/2)-300,
            height=5,
            bg=PRIMARY
        )
        frame.pack(pady=5)

        question = Label(frame,
                         text=q,
                         pady=10,
                         padx=20,
                         bg=PRIMARY,
                         fg="white",
                         font=("Arial", 30),
                         wraplength=500

                         )
        question.pack(padx=30)

        for i, ch in enumerate(c):
            btn = Button(
                frame,
                text=ch,
                padx=10,
                pady=5,
                border=2,
                font=("Arail", 18),
                width=30,
                height=1,
                relief=FLAT,
                wraplength=350,
                command=lambda i=i:  self.check_result(i, a, quizes_list),

            ).pack(pady=5)

    def check_result(self, i, a, quizes_list):

        if i == a:
            self.score += 10
            self.str_var.set(f"Score:{self.score}")

            self.update()

        self.next_page += 1
        if self.next_page < len(quizes_list):
            self.quiz_page_gui(quizes_list)
        else:
            self.next_page = 0
            self.result(len(quizes_list))

    def result(self, l):
        self.cleaning_frames()

        # final results 
        frame = Frame(self)
        frame.config(
            pady=(APP_HIEGHT/2)-100,
            height=5,
            bg=PRIMARY
        )
        frame.pack()

        question = Label(frame,
                         text=self.player_name,
                         pady=8,
                         padx=20,
                         bg=PRIMARY,
                         fg="white",
                         font=("Arial", 30)
                         )
        question.pack()

        Label(
            frame,
            text=f"Score:{self.score}/{l*10}",
            pady=10,
            padx=20,
            bg=PRIMARY,
            fg="white",
            font=("Arial", 30)
        ).pack()

        Button(
            frame,
            text="New Game",
            padx=5,
            pady=3,
            border=2,
            relief=FLAT,
            font=("Arail", 14),
            command=self.add_player_name_gui
        ).pack()

    def start_game(self, name):
        # Check if name is empty
        if name == "":
            return

        # set player name 
        self.player_name = name

        self.main_page()

    def center_app(self):

        SCREEN_WIDTH: int = self.winfo_screenwidth()
        SCREEN_HIGHT: int = self.winfo_screenheight()

        x: int = int((SCREEN_WIDTH/2)-(APP_WIDTH/2))
        y: int = int((SCREEN_HIGHT/2)-(APP_HIEGHT/2))

        self.geometry(f"{APP_WIDTH}x{APP_HIEGHT}+{x}+{y}")

    def cleaning_frames(self):
        # remove all frames 
        for frame in self.winfo_children():
            frame.destroy()
