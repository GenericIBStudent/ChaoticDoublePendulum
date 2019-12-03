from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from PIL import Image
import matplotlib.pyplot as plt


Tk().withdraw() #using tkinter library to open a txt file
filename1 = askopenfilename()
readfile = open(filename1,"r")
labeled_names_temp = str(readfile.readlines()) #converts the array of lines into a string
        #print(labeled_names_temp)
labeled_names_cut = labeled_names_temp[2:len(labeled_names_temp)-3]  #removes the brackets and quotations from the array string
        #print(labeled_names_cut)
labeled_names = labeled_names_cut.split(",") #splits the string into a new array with a neuron in different indices
print(labeled_names)
distances = []
for i in labeled_names:
    distances.append(float(i))

print(distances)
filename2 = askopenfilename()
readfile2 = open(filename2,"r")
labeled_names_temp2 = str(readfile2.readlines()) #converts the array of lines into a string
        #print(labeled_names_temp)
labeled_names_cut2 = labeled_names_temp2[2:len(labeled_names_temp2)-3]  #removes the brackets and quotations from the array string
        #print(labeled_names_cut)
labeled_names2 = labeled_names_cut2.split(",") #splits the string into a new array with a neuron in different indices
print(labeled_names2)
distances2 = []
for i in labeled_names2:
    distances2.append(float(i))

print(len(distances))
print(len(distances2))
plt.plot(range(601),distances)
plt.plot(range(601),distances2)
plt.ylabel('distance from origin(m)')
plt.xlabel('frames(#)')
plt.suptitle('Distance from Origin(m) v.s Frames(#)' )
plt.show()
