# groceries-exercise
Setup the vitual environment in Git Bash
How to:
1. conda create -n groceries-env python=3.7
2. conda activate groceries-env

To run a script:
1. python groceries.py 
    Make sure you're navigated to the right path

Setting up the Product Count
1. Print the dash structure "----"
2. Print a string that says THERE ARE {} PRODUCTS.
    USe a count of the product to fill in the {}

 I imported the price function to let every item get a $ next to the price

The code then counts the number of products in the provded data and uses that count to print a title
The code then iterates through the data to pull out products from the provided dictionaries along with the corresponding price

The dept_list is supposed to be a list that contains each item as a string that reads the Department and the number of products
All list items must be unique

The code iterates through all departments, counts how many times each department appears
Each iteration prints one string for each department, with the total count of how many times each department appears