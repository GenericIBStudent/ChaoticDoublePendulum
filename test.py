import doublependulum


"""listofangles = []
for i in range(0,90,10):
    listofangles.append(i)
    listofangles.append(i + .1)
    listofangles.append(i + .01)
    listofangles.append(i + .001)
    listofangles.append(i + .0001)
    listofangles.append(i + .00001)
    listofangles.append(i - .1)
    listofangles.append(i - .01)
    listofangles.append(i - .001)
    listofangles.append(i - .0001)
    listofangles.append(i - .00001)
    listofangles.append(i + 1)
    listofangles.append(i - 1)
for i in listofangles:
    doublependulum.run(i)"""
i = input("enter angle: ")

doublependulum.run(float(i))
