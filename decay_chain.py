# Import Modules
import os 
#os.system('clear')

# Create element dictionaries
P1N0 = {}
P1N0['name'] = "Hydrogen-1"
P1N0['protons'] = 1
P1N0['neutrons'] = 0
P1N0['half-life'] = "stable"

# print out particle and products
def decay_products(element):
    print("element is: ", element)
    print("type(element) is: ", type(element))
    print(element['name'])
    for key, value in sorted(P1N0.items()):
	    print(" ",key, ":", value)

print(" ")
decay_products(P1N0)