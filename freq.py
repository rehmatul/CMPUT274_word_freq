#--------------------------------------------
#   Name: Fatima Rehmatullah
#   ID: 1631703
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 


# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys

#checks the command line and extracts the filename
def demo_command_line():

    # the first argument is the program name
    # so the filename is the second argument

    filename = sys.argv[1]

    return(filename)

#function takes the filename as an argument
#reads the file and copies content as seperate words in a list
def listformation(filename):

    my_list = []

    #reads the file line by line and keeps splitting 
    #the file contents into seperate words
    with open(demo_command_line(), "r") as file:
        for line in file:
            for word in line.split():
                my_list.append(word)
    #sorts the list into lexicologic order 
    #so that the dictionary is also sorted beforehand
    my_list = sorted(my_list)
    file.close()
    return my_list


#takes the sorted list as a parameter 
#to convert to a dictionary
#with key-value pairs of word-count

def dictionaryformation(my_list):
#iterates through the list to find words 
#and maintain a count of how many times each appears

    frequency = {}
    for i in my_list:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] = frequency[i] + 1
    #returns the frequency dictionary created
    return frequency

#takes my_list, frequency and filename as arguments
#and uses them to write into the file in the format
#word count frequency
def outputfile(my_list, frequency, filename):

    #uses the filename to create a new file of a similar name
    f = open(filename + ".out", "w")

    #uses the my_list to find the total number of words 
    #in order to calculate the density
    length = len(my_list)
    density = 0
    for key in frequency:
        density = str(round((frequency[key] / length), 3))
        f.write(str(key) + " " + str(frequency[key]) + " " + str(density))
        f.write("\n")
    f.close()
    return None

#ensures that the command line argument is complete
#and accurate. Runs the functions if the command is 
#right, produces error messages otherwise
#also checks if the input file is empty

def errorhandling():
    if len(sys.argv) == 2:
        filename = demo_command_line()
        my_list = listformation(filename)
        if my_list==[]:
            print("The file is empty")
            sys.exit(1)
        else:
            frequency = dictionaryformation(my_list)
            outputfile(my_list, frequency, filename)
    else:
        if len(sys.argv) > 2:
            print("ERROR: Your command has too many arguments.")
        elif len(sys.argv) < 2:
            print("ERROR: Your command has too few arguments.")
        print("Enter in the format: 'python3 freq.py <filename>'.")
    sys.exit(1)


if __name__ == "__main__":
    errorhandling()
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    pass
