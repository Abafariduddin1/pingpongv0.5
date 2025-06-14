import tkinter

screen = tkinter.Tk()
screen.geometry("670x500")
screen.resizable(False, False)
screen.config(bg="Black")
screen.title("Countdown")

canvas = tkinter.Canvas(screen, width=670, height=500, bg="black")
canvas.pack()
canvas.create_line(335, 0, 335, 500, fill="white")
canvas.create_oval(335 - 50, 250 - 50, 335 + 50, 250 + 50, outline="white")

class Paddle:
    def __init__(self, canvas, x, color):
        self.canvas = canvas
        self.x = x
        self.y1 = 210
        self.y2 = 290
        self.color = color
        self.rectangle = canvas.create_rectangle(x, self.y1, x + 10, self.y2, fill=color)

    def moveup(self):
        if self.y1 > 0:
            self.y1 = self.y1 - 20
            self.y2 = self.y2 - 20
            self.canvas.delete(self.rectangle)
            self.rectangle = self.canvas.create_rectangle(self.x, self.y1, self.x + 10, self.y2, fill=self.color)

    def movedown(self):
        if self.y2 < 500:
            self.y1 = self.y1 + 20
            self.y2 = self.y2 + 20
            self.canvas.delete(self.rectangle)
            self.rectangle = self.canvas.create_rectangle(self.x, self.y1, self.x + 10, self.y2, fill=self.color)

lpaddle = Paddle(canvas, 30, "orange")
rpaddle = Paddle(canvas, 640, "light green")

def key_pressed(event):
    key = event.keysym
    if key == 'w':
        lpaddle.moveup()
    elif key == 's':
        lpaddle.movedown()
    elif key == 'Up':
        rpaddle.moveup()
    elif key == 'Down':
        rpaddle.movedown()

screen.bind('<KeyPress>', key_pressed)
screen.mainloop()
