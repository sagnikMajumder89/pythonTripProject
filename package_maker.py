from scrapper import scrapperFuncN
import random
from output import btn_clicked
from tkinter import *

index = 0


def modify_Visiting_places(string_list):
    modified_list = []
    for string in string_list:
        words = string.split()
        if len(words) > 2:
            modified_string = " ".join(words[:2])
            modified_list.append(modified_string)
        else:
            modified_list.append(string)
    return modified_list


_destination = ""
_packages = []
_Visit = []
_visit_images = []
_visit_stars_reviews = []


# Do, Stay, Eat, new_eat_price, stay_price, ratings, image_links
def packageMaker(root, destination, budget, stayDuration, numPeople):
    scrapperOutput = scrapperFuncN(destination)
    scrapperVisit = scrapperOutput[0]
    Visit = modify_Visiting_places(scrapperVisit)
    Hotels = scrapperOutput[1]
    Restaurants = scrapperOutput[2]
    Restaurant_expense = scrapperOutput[3]
    Hotel_prices = [
        price * 80 for price in scrapperOutput[4]
    ]  # Convert hotel prices to rupees
    for price in Hotel_prices:
        if price == 0:
            Hotel_prices.remove(price)
    ratings = scrapperOutput[5]
    visit_stars_reviews = ratings[0:10]
    image_links = scrapperOutput[6]
    visit_images = image_links[0:10]
    num_packages = 5
    packages = []

    def calculate_score(hotel_price, restaurant_cost):
        return hotel_price * stayDuration - sum(restaurant_cost)

    def get_random_eat_price(cost, hotel_price):
        if hotel_price > 1000:
            # User chose an expensive hotel, prefer Mid-range or Fine Dining
            if cost == "Mid-range":
                return random.randint(600, 1100) * numPeople
            elif cost == "Fine Dining":
                return random.randint(1500, 2500) * numPeople
        else:
            # User chose a cheaper hotel, prefer Cheap Eats
            if cost == "Cheap Eats":
                return random.randint(100, 600) * numPeople

        # Default case: Randomly choose any price range
        return random.randint(100, 1000) * numPeople

    adjusted_budget = budget * numPeople

    selected_hotels = set()  # Set to store selected hotel indices

    max_attempts = 100  # Maximum attempts to find unique hotels
    attempts = 0

    while len(packages) < num_packages and attempts < max_attempts:
        remaining_budget = adjusted_budget
        hotel_index = random.randint(0, len(Hotels) - 1)
        restaurant_images = []
        if hotel_index in selected_hotels:
            attempts += 1
            continue  # Skip if the hotel has already been selected

        selected_hotels.add(hotel_index)  # Add the hotel index to selected hotels set
        attempts = 0  # Reset the attempts counter

        hotel_name = Hotels[hotel_index]
        hotel_price = Hotel_prices[hotel_index] * stayDuration * numPeople
        hotel_rating = ratings[hotel_index + 10]
        hotel_image = image_links[hotel_index + 10]
        if hotel_price * stayDuration * numPeople > remaining_budget:
            continue  # Skip the hotel if its price exceeds the remaining budget

        restaurant_list = []
        restaurant_cost = []
        restaurant_ratings = []
        temp_restaurants = Restaurants.copy()  # Create a copy of Restaurants
        temp_ratings = ratings.copy()
        temp_image_links = image_links.copy()
        while (
            remaining_budget > 0 and temp_restaurants
        ):  # Use the copied list for iteration
            restaurant_index = random.randint(0, len(temp_restaurants) - 1)
            ratings_index = restaurant_index + 20
            image_index = restaurant_index + 20
            restaurant_name = temp_restaurants[restaurant_index]
            restaurant_expense = Restaurant_expense[restaurant_index]
            eat_price = get_random_eat_price(restaurant_expense, hotel_price)

            if remaining_budget >= eat_price:
                remaining_budget -= eat_price
                restaurant_list.append(restaurant_name)
                restaurant_cost.append(eat_price)
                restaurant_ratings.append(temp_ratings[ratings_index])
                restaurant_images.append(temp_image_links[image_index])
                # print(temp_image_links[image_index])
            else:
                break  # Break the loop if remaining budget is insufficient

            temp_restaurants.remove(restaurant_name)  # Remove from the copied list
            temp_ratings.remove(temp_ratings[ratings_index])
            temp_image_links.remove(temp_image_links[image_index])
        if restaurant_list:
            package_score = calculate_score(hotel_price, restaurant_cost)
            packages.append(
                (
                    hotel_name,
                    hotel_price,
                    hotel_rating,
                    restaurant_list,
                    restaurant_cost,
                    restaurant_ratings,
                    package_score,
                    hotel_image,
                    restaurant_images,
                    visit_images,
                )
            )

    # Sort the packages based on the score in descending order
    packages.sort(key=lambda x: x[6], reverse=True)

    if len(packages) < num_packages:
        print(
            f"Only {len(packages)} packages available instead of {num_packages}. Consider adjusting the parameters."
        )
    global _destination
    _destination = destination.title()
    global _packages
    _packages = packages
    global _Visit
    _Visit = Visit
    global _visit_images
    _visit_images = visit_images
    global _visit_stars_reviews
    _visit_stars_reviews = visit_stars_reviews

    root.withdraw()  # Hide the root window

    print("Window should open now")

    btn_clicked(
        1,
        root=root,
        placeName=destination.title(),
        hotelName=packages[index][0],
        hotel_image=packages[index][7],
        hotel_price=packages[index][1],
        hotel_rating_reviews=packages[index][2],
        resturant_names=packages[index][3],
        resturant_images=packages[index][8],
        resturant_stars=packages[index][5],
        visiting_places=Visit,
        visiting_images=visit_images,
        visiting_stars_reviews=visit_stars_reviews,
        restaurant_cost=packages[index][4],
    )


def nextPackage(root):
    global index, _destination, _packages, _Visit, _visit_images, _visit_stars_reviews
    index = index + 1
    if index >= len(_packages):
        index = 0
    print(index)
    btn_clicked(
        1,
        root=root,
        placeName=_destination.title(),
        hotelName=_packages[index][0],
        hotel_image=_packages[index][7],
        hotel_price=_packages[index][1],
        hotel_rating_reviews=_packages[index][2],
        resturant_names=_packages[index][3],
        resturant_images=_packages[index][8],
        resturant_stars=_packages[index][5],
        visiting_places=_Visit,
        visiting_images=_visit_images,
        visiting_stars_reviews=_visit_stars_reviews,
        restaurant_cost=_packages[index][4],
    )
    root.mainloop()

    root.mainloop()
