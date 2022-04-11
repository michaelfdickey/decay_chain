# Import Modules
import os
import random
from random import seed
from random import randint
seed(1)
#os.system('clear')

# Create element dictionaries

P0N1 = {}
P0N1['name'] = "Neutron"
P0N1['protons'] = 0
P0N1['neutrons'] = 1
P0N1['half-life'] = "10 minutes 11 seconds"
P0N1['# decay chains'] = 1
P0N1['decay chain 1 product 1'] = "P"
P0N1['decay chain 1 product 2'] = "e-"
P0N1['decay chain 1 product 3'] = "-Ve"
P0N1['decay chain 1 products'] = 3

P1N0 = {}
P1N0['id'] = 'P1N0'
P1N0['name'] = "Hydrogen-1"
P1N0['protons'] = 1
P1N0['neutrons'] = 0
P1N0['half-life'] = "stable"

# Deuterium
P1N1 = {}
P1N1['id'] = 'P1N1'
P1N1['name'] = "Deuterium"
P1N1['protons'] = 1
P1N1['neutrons'] = 1
P1N1['half-life'] = "stable"

# Tritium
P1N2 = {}
P1N2['id'] = 'P1N2'
P1N2['name'] = "Tritium"
P1N2['protons'] = 1
P1N2['neutrons'] = 2
P1N2['half-life'] = 12.32  # years
P1N2['decay_isotopes'] = ['P2N1']
P1N2['decay_particles'] = ['e-','-Ve']

## Helium 3 - P2N1
P2N1 = {}
P2N1['name'] = "Helium-3"
P2N1['protons'] = 2
P2N1['neutrons'] = 1
P2N1['half-life'] = "stable"


elements = {}
elements['P0N1'] = P0N1
elements['P1N0'] = P1N0
elements['P1N1'] = P1N1
elements['P1N2'] = P1N2
elements['P2N1'] = P2N1

# print(elements)

# print out particle and products
def decay_products(element):
    #print("element is: ", element)
    #print("type(element) is: ", type(element))
    #print(element['name'])
    for key, value in (element.items()):
	    print(" ",key, ":", value)

def populate_sample(element, number_atoms):
    sample = []
    print(" ")
    print(" element is: ", element['id'])
    print(" number_atoms is: ", number_atoms)
    for item in range(number_atoms):
        sample.append(element['id'])
    #print("  sample is: ")
    #print(sample)
    return sample

# update sample based on decay rates
def update_sample(sample):
    #print(" ~ running update sample ~ ")
    for item_index in range(len(sample)):
        current_item = sample[item_index]
        #print(" current item is: ", sample[item_index])
        # get decay product(s)
        current_entry = elements[sample[item_index]]
        #print("  current_entry is: ", current_entry)
        
        #if current_entry['half-life'] != 'stable':
        #
        #    #print("  decay_isotope is: ", decay_isotope)

        # randomly decay list entry    
        dice_roll = randint(0,10)
        #print("  dice_roll was: ", dice_roll)
        if dice_roll == 1:   # replace with actual propbability of decay
            print("   >> radioactive decay << ")
            #print("    current_item: ",current_item, "has decayed into ", decay_isotope )
            if current_entry['half-life'] != 'stable':
                decay_isotope = current_entry['decay_isotopes']
                decay_isotope = decay_isotope[0]
                sample[item_index] = decay_isotope


def display_sample(simulation_length):
    #print( " running DISPLAY SAMPLE")
    time_steps_length = simulation_length / 10     # 1 / 10 = .1
    #print(" time_step_length: ", time_steps_length)
    time_steps_total = int(100 * time_steps_length)       # 100 * .1 = 10
    #print(" time_steps_total: ", time_steps_total)
    time_count = 0
    for step in range(time_steps_total):
        print(" time step: ", step, )
        update_sample(sample)
        print(sample)



# prompt for inputs of element
print(" ")
#start_element = input("What element are you starting with? (format, P1N2 = Protons 1 Neutrons 2): ")
#number_atoms = int(input("How many atoms of this element: "))
#simulation_length = int(input("How long is the simulation (years): "))

# for testing
start_element = 'P1N2'
number_atoms = 10
simulation_length = 2

print(" ")
print("you are starting with: ", start_element)
print("starting with: ", number_atoms, "atoms")
print("simulation length is: ", simulation_length)
current_element = elements[start_element]
#print(" current_element is: ", current_element)
simulation_integer = simulation_length / 100


# test preconditions and valid input


# determine decay products
print(" ")
decay_products(current_element)
sample = populate_sample(current_element,number_atoms)
#update_sample(sample)
display_sample(simulation_length)


#print(sample)
