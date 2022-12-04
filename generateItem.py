import os
f = open("items.html", "r")
print(f.read())
f = open("items.html", "a")


href = input("Input the link for the item: ")
src = input("Input the src for the image of the product: ")
alt = input("Input an alt for the image: ")
item = input("Input the name of the item: ")
description = input("Input a description for the product: ")
oO = input("Is the item online only? (Y/N): ")

if oO == "Y" or oO == "y":
    oO = "\n     <p>*Online only</p>"
else:
    oO = ""

f.write(f'\n \n<article class="listItem"> \n    <a href="{href}"><img style="float: left;" src="{src}" alt="{alt}"></a>\n    <h1>{item}</h1>\n   <p>{description}</p>{oO}\n</article>')

f.close()