from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO


def cost_range(cost):
    x = round(cost, -2)
    y = 1.5 * x
    return f"₹{x}-{int(y)}/person"


def clicked():
    pass


def next_button_clicked(root):
    from package_maker import nextPackage

    nextPackage(root)


def btn_clicked(
    f,
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_stars,
    resturant_images,
    visiting_places,
    visiting_images,
    visiting_stars_reviews,
    restaurant_cost,
):
    if f == 1:
        stayOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        )
    if f == 2:
        eatOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        )
    if f == 3:
        visitOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        )


def stayOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
    visiting_images,
    visiting_stars_reviews,
    restaurant_cost,
):
    window = Toplevel(root)  # Create a Toplevel window
    root.withdraw()
    hotel_stars = hotel_rating_reviews[0:3]
    hotel_reviews = hotel_rating_reviews[16:]

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="assets/Stay_Output_Page/background.png")
    background = canvas.create_image(440.0, 287.5, image=background_img)

    img0 = PhotoImage(file="assets/Stay_Output_Page/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )
    b0.place(x=67, y=11, width=158, height=47)

    img1 = PhotoImage(file="assets/Stay_Output_Page/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )
    b1.place(x=361, y=11, width=158, height=47)

    img2 = PhotoImage(file="assets/Stay_Output_Page/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )
    b2.place(x=655, y=11, width=158, height=47)

    response = requests.get(
        f"{hotel_image}"
    )  # Replace with the URL of your network image
    image = Image.open(BytesIO(response.content))
    image = image.resize((346, 340), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label = Label(window, image=image)
    image_label.place(x=95, y=149)

    text_label = Label(
        window,
        text=f"{hotelName}",
        font=("Impact", 15),
    )
    text_label.place(x=464, y=214, width=298, height=40)
    text_label.configure(foreground="white")  # Set text color to white
    text_label.configure(bg="#002074")  # Set background color to blue

    text_label2 = Label(
        window,
        text=f"{hotel_stars}/5",
        font=("Verdana", 10, "bold"),
    )
    text_label2.place(x=497, y=434, width=43, height=21)
    text_label2.configure(foreground="white")  # Set text color to white
    text_label2.configure(bg="#002074")  # Set background color to blue

    text_label3 = Label(
        window,
        text=f"{hotel_reviews}",
        font=("Verdana", 10, "bold"),
    )
    text_label3.place(x=667, y=433, width=102, height=22)
    text_label3.configure(foreground="white")  # Set text color to white
    text_label3.configure(bg="#002074")  # Set background color to blue

    text_label4 = Label(
        window,
        text=f"₹{hotel_price}",
        font=("Verdana", 10),
    )
    text_label4.place(x=687, y=176, width=71, height=26)
    text_label4.configure(foreground="white")  # Set text color to white
    text_label4.configure(bg="#002074")  # Set background color to blue

    text_label5 = Label(
        window,
        text=f"{placeName}",
        font=("Lato", 9, "bold"),
    )
    text_label5.place(x=490, y=176, width=122, height=24)
    # text_label5.place(x=492, y=173, width=122, height=24)
    text_label5.configure(foreground="white")  # Set text color to white
    text_label5.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)
    window.mainloop()


# stayOutput('pondicherry','hotelName','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmX8VjCUeVbyF-0pBN0BSmLJ5_mJ4Z4pcDsckmNoeH&s',85)


def visitOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
    visiting_images,
    visiting_stars_reviews,
    restaurant_cost,
):
    window = Toplevel(root)
    root.withdraw()

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"assets/Visit_images/background.png")
    background = canvas.create_image(439.0, 292.5, image=background_img)

    img0 = PhotoImage(file=f"assets/Visit_images/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b0.place(x=68, y=13, width=140, height=42)

    img1 = PhotoImage(file=f"assets/Visit_images/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b1.place(x=361, y=13, width=140, height=42)

    img2 = PhotoImage(file=f"assets/Visit_images/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b2.place(x=653, y=13, width=140, height=41)
    # ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    img3 = PhotoImage(file=f"assets/Visit_images/img3.png")
    b3 = Button(
        window,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_button_clicked(window),
        relief="flat",
    )

    b3.place(x=668, y=72, width=193, height=38)

    # img4 = PhotoImage(file=f"assets/Visit_images/img4.png")
    # b4 = Button(
    #     window,
    #     image=img4,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=clicked,
    #     relief="flat",
    # )

    # b4.place(x=699, y=522, width=141, height=55)

    name1 = Label(
        window,
        text=f"{visiting_places[0]}",
        font=("Helvetica", 12, "bold"),
    )
    name1.place(x=218, y=205, width=169, height=22)
    name1.configure(foreground="white")  # Set text color to white
    name1.configure(bg="#002074")  # Set background color to blue

    name2 = Label(
        window,
        text=f"{visiting_places[1]}",
        font=("Helvetica", 12, "bold"),
    )
    name2.place(x=416, y=205, width=169, height=22)
    name2.configure(foreground="white")  # Set text color to white
    name2.configure(bg="#002074")  # Set background color to blue

    name3 = Label(
        window,
        text=f"{visiting_places[2]}",
        font=("Helvetica", 12, "bold"),
    )
    name3.place(x=102.25, y=439.58, width=169, height=22)
    name3.configure(foreground="white")  # Set text color to white
    name3.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)

    name4 = Label(
        window,
        text=f"{visiting_places[3]}",
        font=("Helvetica", 12, "bold"),
    )
    name4.place(x=302, y=439.58, width=169, height=22)
    name4.configure(foreground="white")  # Set text color to white
    name4.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)

    name5 = Label(
        window,
        text=f"{visiting_places[4]}",
        font=("Helvetica", 12, "bold"),
    )
    name5.place(x=502, y=439.58, width=169, height=22)
    name5.configure(foreground="white")  # Set text color to white
    name5.configure(bg="#002074")  # Set background color to blue
    # -------------------------------------------------------------------------------
    print(visiting_images[0])
    response = requests.get(
        f"{visiting_images[0]}"
    )  # Replace with the URL of your network image
    image1 = Image.open(BytesIO(response.content))
    image1 = image1.resize((179, 113), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    image1_label = Label(window, image=image1)
    image1_label.place(x=208, y=74)

    print(visiting_images[1])
    response = requests.get(
        f"{visiting_images[1]}"
    )  # Replace with the URL of your network image
    image2 = Image.open(BytesIO(response.content))
    image2 = image2.resize((177, 113), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)
    image2_label = Label(window, image=image2)
    image2_label.place(x=405.41, y=74)

    print(visiting_images[2])
    response = requests.get(
        f"{visiting_images[2]}"
    )  # Replace with the URL of your network image
    image3 = Image.open(BytesIO(response.content))
    image3 = image3.resize((179, 113), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(image3)
    image3_label = Label(window, image=image3)
    image3_label.place(x=91, y=309)

    response = requests.get(
        f"{visiting_images[3]}"
    )  # Replace with the URL of your network image
    image4 = Image.open(BytesIO(response.content))
    image4 = image4.resize((177, 113), Image.ANTIALIAS)
    image4 = ImageTk.PhotoImage(image4)
    image4_label = Label(window, image=image4)
    image4_label.place(x=291, y=309)

    response = requests.get(
        f"{visiting_images[4]}"
    )  # Replace with the URL of your network image
    image5 = Image.open(BytesIO(response.content))
    image5 = image5.resize((177, 113), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(image5)
    image5_label = Label(window, image=image5)
    image5_label.place(x=491, y=309)

    text_label1 = Label(
        window,
        text=f"{visiting_stars_reviews[0][0:3]}",
        font=("Helvetica", 9, "bold"),
    )
    text_label1.place(x=236.08, y=273.77, width=24, height=11)
    text_label1.configure(foreground="white")
    text_label1.configure(bg="#002074")

    text_label2 = Label(
        window,
        text=f"{visiting_stars_reviews[1][0:3]}",
        font=("Helvetica", 9, "bold"),
    )
    text_label2.place(x=433.01, y=273.77, width=24, height=11)
    text_label2.configure(foreground="white")
    text_label2.configure(bg="#002074")

    text_label3 = Label(
        window,
        text=f"{visiting_stars_reviews[2][0:3]}",
        font=("Helvetica", 9, "bold"),
    )
    text_label3.place(x=119.21, y=508.77, width=24, height=11)
    text_label3.configure(foreground="white")
    text_label3.configure(bg="#002074")

    text_label4 = Label(
        window,
        text=f"{visiting_stars_reviews[3][0:3]}",
        font=("Helvetica", 9, "bold"),
    )
    text_label4.place(x=318.6, y=508.77, width=24, height=11)
    text_label4.configure(foreground="white")
    text_label4.configure(bg="#002074")

    text_label5 = Label(
        window,
        text=f"{visiting_stars_reviews[4][0:3]}",
        font=("Helvetica", 9, "bold"),
    )
    text_label5.place(x=518.6, y=508.77, width=24, height=11)
    text_label5.configure(foreground="white")
    text_label5.configure(bg="#002074")

    review_text_label1 = Label(
        window,
        text=f"{visiting_stars_reviews[0][16::]}",
        font=("Arial Narrow", 9, "bold"),
    )
    review_text_label1.place(x=306, y=274.44, width=65, height=14)
    review_text_label1.configure(foreground="white")
    review_text_label1.configure(bg="#002074")

    review_text_label2 = Label(
        window,
        text=f"{visiting_stars_reviews[1][16::]}",
        font=("Arial Narrow", 9, "bold"),
    )
    review_text_label2.place(x=501.01, y=274.44, width=65, height=14)
    review_text_label2.configure(foreground="white")
    review_text_label2.configure(bg="#002074")

    review_text_label3 = Label(
        window,
        text=f"{visiting_stars_reviews[2][16::]}",
        font=("Arial Narrow", 9, "bold"),
    )
    review_text_label3.place(x=188.72, y=509.4, width=65, height=14)
    review_text_label3.configure(foreground="white")
    review_text_label3.configure(bg="#002074")

    review_text_label4 = Label(
        window,
        text=f"{visiting_stars_reviews[3][16::]}",
        font=("Arial Narrow", 9, "bold"),
    )
    review_text_label4.place(x=386.6, y=509.4, width=65, height=14)
    review_text_label4.configure(foreground="white")
    review_text_label4.configure(bg="#002074")

    review_text_label5 = Label(
        window,
        text=f"{visiting_stars_reviews[4][16::]}",
        font=("Arial Narrow", 9, "bold"),
    )
    review_text_label5.place(x=586.6, y=509.4, width=65, height=14)
    review_text_label5.configure(foreground="white")
    review_text_label5.configure(bg="#002074")

    window.resizable(False, False)

    window.mainloop()


def eatOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
    visiting_images,
    visiting_stars_reviews,
    restaurant_cost,
):
    window = Toplevel(root)
    root.withdraw()

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"assets/eat_images/background.png")
    background = canvas.create_image(526.5, 304.0, image=background_img)

    img0 = PhotoImage(file=f"assets/eat_images/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b0.place(x=366, y=10, width=158, height=48)

    img1 = PhotoImage(file=f"assets/eat_images/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b1.place(x=660, y=11, width=158, height=47)

    img2 = PhotoImage(file=f"assets/eat_images/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_stars,
            resturant_images,
            visiting_places,
            visiting_images,
            visiting_stars_reviews,
            restaurant_cost,
        ),
        relief="flat",
    )

    b2.place(x=72, y=11, width=158, height=47)

    img3 = PhotoImage(file=f"assets/eat_images/img3.png")
    b3 = Button(
        window,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=clicked,
        relief="flat",
    )

    b3.place(x=378, y=514, width=142, height=61)

    # resturant 1 name:
    name1 = Label(
        window,
        text=f"{resturant_names[0]}",
        font=("Helvetica", 12, "bold"),
    )
    name1.place(x=61, y=326, width=201, height=23)
    name1.configure(foreground="white")  # Set text color to white
    name1.configure(bg="#002074")

    # resturant 2 name:
    name2 = Label(
        window,
        text=f"{resturant_names[1]}",
        font=("Helvetica", 12, "bold"),
    )
    name2.place(x=341.83, y=327.32, width=201, height=30)
    name2.configure(foreground="white")  # Set text color to white
    name2.configure(bg="#002074")
    # resturant 3 name:
    name3 = Label(
        window,
        text=f"{resturant_names[2]}",
        font=("Helvetica", 12, "bold"),
    )
    name3.place(x=621.83, y=328.32, width=201, height=30)
    name3.configure(foreground="white")  # Set text color to white
    name3.configure(bg="#002074")
    print(resturant_images[0])
    # resturant 1 image:
    response = requests.get(
        f"{resturant_images[0]}"
    )  # Replace with the URL of your network image
    image1 = Image.open(BytesIO(response.content))
    image1 = image1.resize((239, 179), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    image1_label = Label(window, image=image1)
    image1_label.place(x=43, y=135)
    print(resturant_images[1])
    # resturant 2 image:
    response = requests.get(
        f"{resturant_images[1]}"
    )  # Replace with the URL of your network image
    image2 = Image.open(BytesIO(response.content))
    image2 = image2.resize((239, 179), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)
    image2_label = Label(window, image=image2)
    image2_label.place(x=324, y=135)
    print(resturant_images[2])
    # resturant 3 image:
    response = requests.get(
        f"{resturant_images[2]}"
    )  # Replace with the URL of your network image
    image3 = Image.open(BytesIO(response.content))
    image3 = image3.resize((239, 179), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(image3)
    image3_label = Label(window, image=image3)
    image3_label.place(x=604, y=135)
    print("------------------------------------------")
    print(resturant_stars[0])
    # resturant 1 rating:
    rating1 = Label(
        window,
        text=f"{resturant_stars[0][0:3]}/5",
        font=("Helvetica", 8, "bold"),
    )
    rating1.place(x=227, y=362, width=45, height=12)
    rating1.configure(foreground="white")  # Set text color to white
    rating1.configure(bg="#002074")
    print(resturant_stars[1])
    # resturant 2 rating:
    rating2 = Label(
        window,
        text=f"{resturant_stars[1][0:3]}/5",
        font=("Helvetica", 8, "bold"),
    )
    rating2.place(x=504.83, y=362, width=45, height=12)
    rating2.configure(foreground="white")  # Set text color to white
    rating2.configure(bg="#002074")
    print(resturant_stars[2])
    # resturant 3 rating:
    rating3 = Label(
        window,
        text=f"{resturant_stars[2][0:3]}/5",
        font=("Helvetica", 8, "bold"),
    )
    rating3.place(x=784.83, y=362, width=45, height=12)
    rating3.configure(foreground="white")  # Set text color to white
    rating3.configure(bg="#002074")

    # resturant 1 review:
    review1 = Label(
        window,
        text=f"{resturant_stars[0][16:]}",
        font=("Arial Narrow", 8, "bold"),
    )
    print(hotel_rating_reviews[0][16:])
    review1.place(x=204, y=382, width=75, height=13)
    review1.configure(foreground="white")  # Set text color to white
    review1.configure(bg="#002074")

    # resturant 2 review:
    review2 = Label(
        window,
        text=f"{resturant_stars[1][16:]}",
        font=("Arial Narrow", 8, "bold"),
    )
    review2.place(x=481.83, y=382, width=75, height=13)
    review2.configure(foreground="white")  # Set text color to white
    review2.configure(bg="#002074")
    print(hotel_rating_reviews[1][16:])

    # resturant 3 review:
    review3 = Label(
        window,
        text=f"{resturant_stars[2][16:]}",
        font=("Arial Narrow", 8, "bold"),
    )
    review3.place(x=761.83, y=382, width=75, height=13)
    review3.configure(foreground="white")  # Set text color to white
    review3.configure(bg="#002074")
    print(resturant_stars[2][16:])

    cost1 = Label(
        window,
        text=f"{cost_range(restaurant_cost[0])}",
        font=("Arial Narrow", 10, "bold"),
    )
    cost1.place(x=61, y=370, width=120, height=20)
    cost1.configure(foreground="white")  # Set text color to white
    cost1.configure(bg="#002074")  # Set background color to blue

    cost2 = Label(
        window,
        text=f"{cost_range(restaurant_cost[1])}",
        font=("Arial Narrow", 10, "bold"),
    )
    cost2.place(x=341.6, y=370, width=120, height=20)
    cost2.configure(foreground="white")  # Set text color to white
    cost2.configure(bg="#002074")  # Set background color to blue

    cost3 = Label(
        window,
        text=f"{cost_range (restaurant_cost[2])}",
        font=("Arial Narrow", 10, "bold"),
    )
    cost3.place(x=621.83, y=370, width=120, height=20)
    cost3.configure(foreground="white")  # Set text color to white
    cost3.configure(bg="#002074")  # Set background color to blue

    window.resizable(False, False)
    window.mainloop()
