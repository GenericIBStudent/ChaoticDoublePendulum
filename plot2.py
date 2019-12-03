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
points = []
for i in labeled_names:
    str1 = i.replace("(","")
    str2 = str1.replace(")","")
    points.append(str2)
count = 0
xcoord = []
ycoord = []
for j in points:
    if count%2 == 0:
        xcoord.append(float(j))
    elif count%2 == 1:
        ycoord.append(float(j))
    count += 1

filename2 = askopenfilename()
readfile2 = open(filename2,"r")
labeled_names_temp2 = str(readfile2.readlines()) #converts the array of lines into a string
        #print(labeled_names_temp)
labeled_names_cut2 = labeled_names_temp2[2:len(labeled_names_temp2)-3]  #removes the brackets and quotations from the array string
        #print(labeled_names_cut)
labeled_names2 = labeled_names_cut2.split(",")
#splits the string into a new array with a neuron in different indices
points2 = []
for i in labeled_names2:
    str1 = i.replace("(","")
    str2 = str1.replace(")","")
    points2.append(str2)
#print(points2)
count2 = 0
xcoord2 = []
ycoord2 = []
for j in points2:
    if count2%2 == 0:
        xcoord2.append(float(j))
    elif count2%2 == 1:
        ycoord2.append(float(j))
    count2 += 1
print(xcoord[0])
print(ycoord[0])
print(xcoord2[0])
print(ycoord2[0])
plt.plot(xcoord,ycoord)
plt.plot(xcoord2,ycoord2)
plt.ylabel('yposition(meters)')
plt.xlabel('xposition(meters)')
plt.show()


#for i in labeled_names:
    #distances.append(float(i))
