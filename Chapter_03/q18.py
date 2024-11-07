# Exercise 18
print("Please answer either \"Yes\" or \"No\".")
answer_veget = input("Will there be a vegetarian at dinner?\n")
answer_vegan = input("Will there be a vegan at dinner?\n")
answer_glut = input("Will there be a gluten-free diet follower at dinner?\n")

Veget_flag = answer_veget == "Yes"
Vegan_flag = answer_vegan == "Yes"
Glut_flag = answer_glut == "Yes"

print("Here are the suitable restaurants:")
# no no no
if not Veget_flag and not Vegan_flag and not Glut_flag:
    print('"Joe\'s Gourmet Hamburgers"')
    print('"Central Pizzeria"')
    print('"Corner Cafe"')
    print('"Italian Mom\'s Dishes"')
    print('"Chef\'s Kitchen"')

# no yes no
elif not Veget_flag and Vegan_flag and not Glut_flag:
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')
# yes no no
elif Veget_flag and not Vegan_flag and not Glut_flag:
    print('"Central Pizzeria"')
    print('"Corner Cafe"')
    print('"Italian Mom\'s Dishes"')
    print('"Chef\'s Kitchen"')
# no no yes
elif not Veget_flag and not Vegan_flag and Glut_flag:
    print('"Central Pizzeria"')
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')

# no yes yes
elif not Veget_flag and Vegan_flag and Glut_flag:
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')
# yes yes no
elif Veget_flag and Vegan_flag and not Glut_flag:
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')
# yes no yes
elif Veget_flag and not Vegan_flag and Glut_flag:
    print('"Central Pizzeria"')
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')

# yes yes yes
elif Veget_flag and Vegan_flag and Glut_flag:
    print('"Corner Cafe"')
    print('"Chef\'s Kitchen"')


# Joe's Gourmet Hamburgers - no no no
# Central Pizzeria - yes no yes
# Corner Cafe - yes yes yes
# Italian Mom's Dishes - yes no no
# Chef's Kitchen - yes yes yes

