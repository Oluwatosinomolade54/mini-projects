print("Hello, welcome to Python Pizza delivery")
size = input("What size of pizza do you want? S, M, L\n")
pepperoni = input("Would like to add Pepperoni to your pizza? Y or N\n")
cheese = input("Would you like to add cheese to your pizza? Y or N\n")
s_pizza = 15
m_pizza = 20
l_pizza = 25
Pepperoni_s = 2
Pepperoni_ml = 3
cheese_sml = 1


if size == "S":
    if pepperoni == "Y":
        if cheese == "Y":
            print("The small size pizza is","$", s_pizza + Pepperoni_s + cheese_sml)
        elif cheese == "N":
            print("The small pizza is", "$", s_pizza + Pepperoni_s)
    if pepperoni == "N":
        if cheese == "Y":
            print("The small size pizza is","$", s_pizza + cheese_sml)
        elif cheese == "N":
            print("The small pizza is", "$", s_pizza)

if size == "M":
    if pepperoni == "Y":
        if cheese == "Y":
            print("The medium size pizza is","$", m_pizza + Pepperoni_ml + cheese_sml)
        elif cheese == "N":
            print("The medium pizza is", "$", m_pizza + Pepperoni_ml)
    if pepperoni == "N":
        if cheese == "Y":
            print("The medium size pizza is","$", m_pizza + cheese_sml)
        elif cheese == "N":
            print("The medium pizza is", "$", m_pizza)

if size == "L":
    if pepperoni == "Y":
        if cheese == "Y":
            print("The large size pizza is","$", l_pizza + Pepperoni_ml + cheese_sml)
        elif cheese == "N":
            print("The large pizza is", "$", l_pizza + Pepperoni_ml)
    if pepperoni == "N":
        if cheese == "Y":
            print("The large size pizza is","$", l_pizza + cheese_sml)
        elif cheese == "N":
            print("The medium pizza is", "$", l_pizza)

