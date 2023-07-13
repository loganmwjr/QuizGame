from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(bg=THEME_COLOR,
                           padx=20,
                           pady=20)

        self.canvas = Canvas()
        self.canvas.config(width=300,
                           height=250,
                           bg='white', )
        self.question_text = self.canvas.create_text((150, 125),
                                                     text=f"",
                                                     fill=THEME_COLOR,
                                                     font=('ariel', 20, 'italic'),
                                                     width=280)

        self.canvas.grid(row=1,
                         column=0,
                         columnspan=2,
                         pady=50)

        self.score_label = Label(text=f'score {self.quiz.score}',
                                 padx=20,
                                 bg=THEME_COLOR,
                                 fg='white')
        self.score_label.grid(row=0,
                              column=1)

        #       button
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  highlightbackground=THEME_COLOR,
                                  bg=THEME_COLOR,
                                  padx=20,
                                  command=self.true_check)
        self.true_button.grid(row=2,
                              column=0)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   padx=20,
                                   command=self.false_check)
        self.false_button.grid(row=2,
                               column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text='This is the end of the quiz.')

    def true_check(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
