from Tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(
            master, width=200, height=50
        )
        frame.pack()

        self.input = StringVar()
        subreddit = Entry(
            master, textvariable=self.input
        )
        subreddit.pack(side=TOP)

        top_from_ = ["Day", "Week", "All", "Hot"]
        self.vars = []

        for source in top_from_:
            var = IntVar()

            check = Checkbutton(
                master, text="Top {}?".format(source), variable=var
            )
            check.pack(side=LEFT)
            self.vars.append(var)

        b = Button(
            master, text="Go", command=self.print_report, relief=FLAT
        )

        b.pack(side=RIGHT)

    @staticmethod
    def print_status(var):
        return "This: " + str(var.get())

    def print_report(self):
        print map(self.print_status, self.vars)
        print self.input.get()


def main():
    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()
