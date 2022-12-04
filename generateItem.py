import os
f = open("items.html", "r")
print(f.read())
f = open("items.html", "a")

price = input("Input the price of the Product")
href = input("Input the link for the Product: ")
src = input("Input the src for the image of the product: ")
alt = input("Input an alt for the image: ")
item = input("Input the name of the item: ")
description = input("Input a description for the product: ")
oO = input("Is the item online only? (Y/N): ")

if oO == "Y" or oO == "y":
    oO = "\n     <p>*Online only</p>"
else:
    oO = ""

f.write(f'\n \n    <p style="float: inline-start[];">{price}</p>\n    <article class="listItem"> \n    <a href="{href}" target="_blank"><img style="float: left;" src="{src}" alt="{alt}"></a>\n    <h1>{item}</h1>\n   <p>{description}</p>{oO}\n</article>')

f.close()