from tkinter import *
import tkinter as tk
from scrapper import scrapperFuncN
from package_maker import packageMaker
import re


def clicked(currentWindow):
    currentWindow.withdraw()


def errorPage(root):
    window = Toplevel(root)

    window.geometry("880x575")
    window.configure(bg="#00203d")
    canvas = Canvas(
        window,
        bg="#00203d",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"assets/Error Page/background.png")
    background = canvas.create_image(437.0, 253.5, image=background_img)

    img0 = PhotoImage(file=f"assets/Error Page/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clicked(window),
        relief="flat",
    )

    b0.place(x=316, y=477, width=220, height=50)

    img1 = PhotoImage(file=f"assets/Error Page/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clicked(window),
        relief="flat",
    )

    b1.place(x=59, y=477, width=220, height=50)

    window.resizable(False, False)
    window.mainloop()


def explore_clicked(whereto, budget, days, travelers):
    temp_budget = budget.get()
    print("temp budget: ", temp_budget)
    temp_whereto = whereto.get()
    print("where budget: ", temp_whereto)

    temp_days = days.get()
    print("temp days: ", temp_days)

    temp_travelers = travelers.get()
    print("travellers days: ", temp_travelers)

    if (
        budget.get() == ""
        or whereto.get() == ""
        or days.get() == ""
        or travelers.get() == ""
    ):
        errorPage(window)

    if (
        re.match("^[0-9]*$", temp_budget)
        and re.match("[A-Za-z]*$", temp_whereto)
        and re.match("[0-9]*$", temp_days)
        and re.match("[0-9]*$", temp_travelers)
    ):
        pass
    else:
        errorPage(window)

    days_contents = int(days.get())
    budget_contents = int(budget.get())
    whereto_contents = whereto.get()
    travelers_contents = int(travelers.get())
    print("-----------------------------")
    print("Destination: ", whereto_contents)
    print("-----------------------------")
    print("Budget: ", budget_contents)
    print("-----------------------------")
    print("Day: ", days_contents)
    print("---------------------")
    print("Travelers = ", travelers_contents)

    packageMaker(
        window, whereto_contents, budget_contents, days_contents, travelers_contents
    )


window = Tk()

window.geometry("893x560")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=560,
    width=893,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"assets/First_page/background.png")
background = canvas.create_image(446.5, 280.0, image=background_img)

img0 = PhotoImage(file=f"assets/First_page/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: explore_clicked(whereto, budget, days, travelers),
    relief="flat",
)

b0.place(x=579, y=464, width=219, height=46)

days_img = PhotoImage(file=f"assets/First_page/img_textBox0.png")
days_bg = canvas.create_image(688.5, 311.5, image=days_img)

days = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

days.place(x=594.5, y=296, width=188.0, height=29)

budget_img = PhotoImage(file=f"assets/First_page/img_textBox1.png")
budget_bg = canvas.create_image(689.5, 224.5, image=budget_img)

budget = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

budget.place(x=595.5, y=209, width=188.0, height=29)

whereto_img = PhotoImage(file=f"assets/First_page/img_textBox2.png")
whereto_bg = canvas.create_image(688.5, 137.5, image=whereto_img)

whereto = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

whereto.place(x=594.5, y=122, width=188.0, height=29)

travelers_img = PhotoImage(file=f"assets/First_page/img_textBox3.png")
travelers_bg = canvas.create_image(687.5, 398.5, image=travelers_img)

travelers = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

travelers.place(x=593.5, y=383, width=188.0, height=29)

window.resizable(False, False)
window.mainloop()
