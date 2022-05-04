# Import Modules
import os
import random
from random import seed
from random import randint
import numpy as np


#seed(1)
#os.system('clear')

# Create element dictionaries

P0N1 = {}
P0N1['name'] = "Neutron"
P0N1['protons'] = 0
P0N1['neutrons'] = 1
P0N1['half-life'] = [611,'seconds']
#P0N1['half-life'] = "10 minutes 11 seconds"
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
P1N2['half-life'] = [12.32,'years']
P1N2['decay_chains'] = [['P2N1','e-','-Ve']]

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
    print(" > running decay_products ")
    #print("element is: ", element)
    #print("type(element) is: ", type(element))
    #print(element['name'])
    for key, value in (element.items()):
	    print(" ",key, ":", value)


def populate_sample(element, number_atoms):
    print(" ")
    print(" > running populate_sample ")
    sample = []
    #print(" element is: ", element['id'])
    #print(" number_atoms is: ", number_atoms)
    for item in range(number_atoms):
        sample.append(element['id'])
    #print("  sample is: ")
    print("   sample is: ", sample)
    return sample


# update sample based on decay rates
def update_sample(sample):
    """
    iterates through the sample, passes each element to the did_element_decay and if it did updates the sample with the new element. 
    
    Arguments:
    sample - dictionary of elements that make up the sample
    """
    print(" ")
    print(" > running update_sample")
    for item_index in range(len(sample)):
        current_item = sample[item_index]
        #print("    current item is: ", sample[item_index], type(sample[item_index]))
        current_element = elements[sample[item_index]]
        #print("    current_element is: ", current_element, type(current_element))
        element = decay_element(current_element)
        #print("    current_element is: ", current_element, type(current_element))
        sample[item_index] = element
    print(" ")
    print(" sample is: ", sample)


def display_sample(simulation_length):
    print(" ")
    print(" > running display_sample")
    #print( " running DISPLAY SAMPLE")
    time_steps_length = simulation_length / 100     # 1 / 10 = .1
    #print(" time_step_length: ", time_steps_length)
    time_steps_total = int(10000 * time_steps_length)       # 100 * .1 = 10
    #print(" time_steps_total: ", time_steps_total)
    time_count = 0
    for step in range(time_steps_total):
        os.system('cls')
        print(" time step: ", step)
        print(sample)
        update_sample(sample)


def decay_element(element):
    """
    takes an example element, determines if it decays in the timestep, and returns the decay products as strings

    Arguments:
    element - dictionary of element entry
    timestep - float in years
    products - a list contining the decay products, if any are atoms it returns a dictionary of that element nested in the table
    """
    #https://scipython.com/book2/chapter-6-numpy/examples/simulating-radioactive-decay/
    print(" ")
    print(" > > running decay_element")
    #print("  element is: ", element)
    #print("  element['half-life']: ", element['half-life'])
    #print("  element['decay_chains']:", element['decay_chains'])
    
    half_life = element['half-life'][0]
    lifetime = half_life / np.log(2)
    #print("  lifetime:",lifetime)
    delta_time = 12.32
    probability_of_decay = (delta_time / lifetime) * 1000
    #print("  probability_of_decay: ", probability_of_decay)
    
    random_num = random.random() * 1000
    
    #print("   random_num: ", random_num)

    if random_num < probability_of_decay:
        #this nuclear decays
        element = element['decay_chains'][0][0]     # first decay chain, first entry is element id
        print("   element is now: ", element)
        return str(element)
    else:
        #did not decay
        print("   element is: ", element['id'])
        return element['id']

    



# prompt for inputs of element
print(" ")
#start_element = input("What element are you starting with? (format, P1N2 = Protons 1 Neutrons 2): ")
#number_atoms = int(input("How many atoms of this element: "))
#simulation_length = int(input("How long is the simulation (years): "))

# for testing
start_element = 'P1N2'
number_atoms = 2
simulation_length = 1
print(" ")
print("you are starting with: ", start_element)
print("starting with:         ", number_atoms, "atoms")
print("simulation length is:  ", simulation_length)


current_element = elements[start_element]
#print(" current_element is: ", current_element)
simulation_integer = simulation_length / 100

# test preconditions and valid input

# determine decay products
print(" ")
sample = populate_sample(current_element, number_atoms)     # populates sample
update_sample(sample)                                       # updates sample, this is where the decay happens

#decay_products(current_element)
#display_sample(simulation_length)


# test decay_element 
#decay_element(P1N2)

#print(sample)
