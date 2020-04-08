from tkinter import Tk, Label, Button, Checkbutton, IntVar, messagebox


class ConfigurationDialog:

    """
    Configuration dialog.
    """

    def __init__(self):
        self.window=None
        self.value = 0
        self.shows = None
        self.run = False

    def show(self):
        """
        Init and show the window.
        """

        # init and config
        self.window=Tk()
        self.window.title('Configurations')
        self.window.resizable(False, False)
        self.window.configure(bg='#2c2825')
        # center the window
        self.center_window()

        # main label
        txt1 = Label(self.window, text="Please choose an algorithm", fg="#cfaf4f", bg="#2c2825")
        txt1.place(x=22, y=1)

        # the three buttons
        b1=Button(self.window, text='A*', command=lambda: self.choose(0), height=1, width=6, bg="#cfaf4f", fg="black")
        b2=Button(self.window, text='BFS', command=lambda: self.choose(1), height=1, width=6, bg="#cfaf4f", fg="black")
        b3=Button(self.window, text='DFS', command=lambda: self.choose(2), height=1, width=6, bg="#cfaf4f", fg="black")

        b1.place(x=10, y=30)
        b2.place(x=70, y=30)
        b3.place(x=130, y=30)

        # check box
        self.shows = IntVar(value=1)
        chbtn1 = Checkbutton(self.window, text="show steps", fg="#cfaf4f",  bg="#2c2825", variable=self.shows)
        chbtn1.place(x=190, y=30)

        # run main loop
        self.window.mainloop()

    def choose(self, index: int):
        """
        change algorithm index value.

        :param index: algorithm index
        :type index: int
        """
        self.value = index
        self.run = True
        # close the window
        self.window.destroy()

    def center_window(self, w=280, h=70):
        """
        Center dialog on the screen.
        """
        # get screen width and height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    @staticmethod
    def show_report(distance: int): 
        """
        show distance repost message.

        :param distance: distance from start position to the target
        :type distance: int
        """
        # hide the window
        mwindow = Tk()
        mwindow.withdraw()
        # show message box
        if distance: 
            messagebox.showinfo('Distance report', f'The shortest distance to the target is {distance} block(s) away.')
        else: 
            messagebox.showinfo('Distance report', 'There is no solution!')
        # destroy the window
        mwindow.destroy()
