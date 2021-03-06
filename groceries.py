# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


# pprint(products)

# TODO: write some Python code here to produce the desired output

# I imported the price function to let every item get a $ next to the price
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# the below code counts the number of products in the provded data and uses that count to print a title
# the code iterates through the data to pull out products from the provided dictionaries along with the corresponding price
count = len(products)
print("------------")
print(f"THERE ARE {count} PRODUCTS:")
print("------------")

products2 = [prod["name"] + " " + "(" + str(to_usd(prod["price"])) + ")" for prod in products]
products2.sort()
#I've added a sort method to make the result be sorted alphabetically 
for prod in products2:
    products_final = "+ " + prod
    print(products_final)

#need a separate list with only the items from Department
#I've added a sort method to tailor the eventual output to be sorted alphabetically
list = [prod["department"] for prod in products]
list.sort()
#need a unique list of items so we can use that list remove duplicate entries from dept_list
unique_list = []
#dept_list is supposed to be a list that contains each item as a string that reads the Department and the number of products
# all list items must be unique
dept_list = []
# the below code iterates through all departments, counts how many times each department appears
# Each iteration prints one string for each department, with the total count of how many times each department appears
for li in list:
    if li in unique_list:
        continue
    elif li not in unique_list:
        unique_list.append(li)
        count = list.count(li)
        if count == 1:
            dept_list.append("+ " + str(li.title()) + " (" + str(count) + " Product)")
        else:
            dept_list.append("+ " + str(li.title()) + " (" + str(count) + " Products)")
count_ul = len(unique_list)
print("-----------")
print(f"THERE ARE {count_ul} DEPARTMENTS:")
print("-----------")
for de in dept_list:
    print(de)



