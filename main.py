#Random food recommendation system

import random
from menu import morning, afternoon, night, evening

meal = input("What kind of meal do you want?(Breakfast, lunch, dinner or a snack?)")

#BREAKFAST FUNCTION
def breakfast():
    taste = input("What's your mood?Spicy, Sweet, Savory, Cold Drinks, Hot Drinks?")

    if taste == "spicy":
        result = random.choice(morning["spicy"])
        return result
    
    elif taste == "sweet":
        sub = input("Do you prefer a sweet dish or a sweet fruit?")
        if sub == "dish":
            result1 = random.choice(morning["sweet_dish"])
            return result1
        elif sub == "fruit":
            result2 = random.choice(morning["sweet_fruit"])
            return result2
    
    elif taste == "savory":
        result = random.choice(morning["savory"])
        return result

    elif taste == "hot drinks":
        result = random.choice(morning["hot_drinks"])
        return result

    elif taste == "cold drinks":
        result = random.choice(morning["cold_drinks"])
        return result
    else:
        print("Enter a valid statement!")


#LUNCH FUNCTION
def lunch():
    taste = input("What's your mood?Spicy, Sweet, Savory, Cold Drinks, Hot Drinks?")
    if taste == "spicy":
        result = random.choice(afternoon["spicy"])
        return result
    
    elif taste == "sweet":
        sub = input("Do you prefer a sweet dish or a sweet fruit?")
        if sub == "dish":
            result1 = random.choice(afternoon["sweet_dish"])
            return result1
        elif sub == "fruit":
            result2 = random.choice(afternoon["sweet_fruit"])
            return result2
    
    elif taste == "savory":
        result = random.choice(afternoon["savory"])
        return result

    elif taste == "hot drinks":
        result = random.choice(afternoon["hot_drinks"])
        return result

    elif taste == "cold drinks":
        result = random.choice(afternoon["cold_drinks"])
        return result
    else:
        print("Enter a valid statement!")
    


#DINNER FUNCTION
def dinner():
    taste = input("What's your mood?Spicy, Sweet, Savory, Cold Drinks, Hot Drinks?")
    if taste == "spicy":
        result = random.choice(night["spicy"])
        return result
    
    elif taste == "sweet":
        sub = input("Do you prefer a sweet dish or a sweet fruit?")
        if sub == "dish":
            result1 = random.choice(night["sweet_dish"])
            return result1
        elif sub == "fruit":
            result2 = random.choice(night["sweet_fruit"])
            return result2
    
    elif taste == "savory":
        result = random.choice(night["savory"])
        return result

    elif taste == "hot drinks":
        result = random.choice(night["hot_drinks"])
        return result

    elif taste == "cold drinks":
        result = random.choice(night["cold_drinks"])
        return result
    else:
        print("Enter a valid statement!")



#Snack FUNCTION
def snacks():
    taste = input("What's your mood?Spicy, Sweet, Savory, Salty, Cold Drinks, Hot Drinks?")
    if taste == "spicy":
        result = random.choice(evening["spicy"])
        return result
    
    elif taste == "sweet":
        sub = input("Do you prefer a sweet dish or a sweet fruit?")
        if sub == "dish":
            result1 = random.choice(evening["sweet_dish"])
            return result1
        elif sub == "fruit":
            result2 = random.choice(evening["sweet_fruit"])
            return result2
    
    elif taste == "savory":
        result = random.choice(evening["savory"])
        return result
    
    elif taste == "salty":
        result = random.choice(evening["salty"])
        return result

    elif taste == "hot drinks":
        result = random.choice(evening["hot_drinks"])
        return result

    elif taste == "cold drinks":
        result = random.choice(evening["cold_drinks"])
        return result
    else:
        print("Enter a valid statement!")


if meal == "breakfast":
    print(breakfast())
elif meal == "lunch":
    print(lunch())
elif meal == "dinner":
    print(dinner())
elif meal == "snacks":
    print(snacks())
else:
    print("Enter a Valid Statement!")