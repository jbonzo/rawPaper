from Tkinter import *
from rawPaper import *



class App:
    def __init__(self, master):
        frame = Frame(
            master, width=200, height=50
        )
        frame.pack()

        title = Label(master, text="rawPaper", )
        title.pack(side=TOP)

        self.input = StringVar()
        self.input.set("woahdude")
        sub_input = Entry(
            master, textvariable=self.input
        )
        sub_input.pack(side=TOP)

        top_from_ = ["Day", "Week", "All", "Hot"]
        self.vars = []

        r = 0
        c = 0
        for source in top_from_:
            var = StringVar()

            check = Checkbutton(
                master, text="Top {}?".format(source), variable=var,
                onvalue=source, offvalue=""
            )
            #check.grid(row=r % 2, column=c % 2)
            check.pack(side=BOTTOM)
            # debug
            check.select()
            self.vars.append(var)
            r += 1
            c += r

        b = Button(
            master, text="Go", command=self.pull_pics, relief=FLAT
        )

        b.pack(side=RIGHT)

        # Subreddit object
        self.sub = Subreddit()

    @staticmethod
    def print_status(var):
        return "Top from " + str(var.get())

    def print_report(self):
        self.sub = self.input.get()

        print map(self.print_status, self.vars)
        print self.sub

    def pull_pics(self):
        self.sub = self.input.get().lower()
        map(pull_from_leader, self.vars)






def get_app():
    return app

def main():
    print app.input.get()


    root.mainloop()
    root.destroy()



root = Tk()
app = App(root)
if __name__ == '__main__':
    main()
