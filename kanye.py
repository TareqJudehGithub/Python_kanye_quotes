from tkinter import *
import requests


class Kanye:
    def __init__(self):
        window = Tk()
        window.title("Kanye Says...")
        window.config(padx=50, pady=50)
        self.canvas = Canvas(width=300, height=414)
        background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=background_img)
        self.text = self.canvas.create_text(
            150, 207,
            text=None,
            width=250,
            font=("Arial", 20, "bold"),
            fill="black"
        )
        self.canvas.grid(row=0, column=0)
        kanye_img = PhotoImage(file="kanye.png")
        kanye_button = Button(image=kanye_img, highlightthickness=0,
                              command=self.get_quote)
        kanye_button.grid(row=1, column=0)
        window.mainloop()

    def get_quote(self):
        response = requests.get(url="https://api.kanye.rest")
        response.raise_for_status()
        data = response.json()
        quote = data["quote"]
        self.canvas.itemconfig(self.text, text=quote, fill="black")


Kanye()


