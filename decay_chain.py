# Import Modules
import os 
#os.system('clear')

# Create element dictionaries
P1N0 = {}
P1N0['name'] = "Hydrogen-1"
P1N0['protons'] = 1
P1N0['neutrons'] = 0
P1N0['half-life'] = "stable"

P1N1 = {}
P1N1['name'] = "Deuterium"
P1N1['protons'] = 1
P1N1['neutrons'] = 1
P1N1['half-life'] = "stable"

P1N2 = {}
P1N2['name'] = "Tritium"
P1N2['protons'] = 1
P1N2['neutrons'] = 2
P1N2['half-life'] = 12.32  # years
P1N2['num decay chains'] = 1
P1N2['decay chain 1 step 1 product 1'] = 'P2N1'
P1N2['decay chain 1 step 1 product 2'] = "e-"
P1N2['decay chain 1 step 1 product 3'] = "-Ve"

elements = {}
elements['P1N0'] = P1N0
elements['P1N1'] = P1N1
elements['P1N2'] = P1N2
# print(elements)

# print out particle and products
def decay_products(element):
    print("element is: ", element)
    print("type(element) is: ", type(element))
    print(element['name'])
    for key, value in (element.items()):
	    print(" ",key, ":", value)


# prompt for input of element
print(" ")
start_element = input("What element are you starting with? (format, P1N2 = Protons 1 Neutrons 2): ")
print("you are starting with: ", start_element)
current_element = elements[start_element]
#print(" current_element is: ", current_element)

# determine decay products
print(" ")
decay_products(current_element)

