import sys
import os
import math
import glob
import imageio
import sys
import datetime
import gif2mp4
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


# Pendulum rod lengths (m), bob masses (kg).
L1, L2 = 2, 1
m1, m2 = 1, 1
r = 0.05
# Plot a trail of the m2 bob's position for the last trail_secs seconds.
trail_secs = 1
# Maximum time, time point spacings and the time grid (all in s).
tmax, dt = 30, 0.001
t = np.arange(0, tmax+dt, dt)
# This corresponds to max_trail time points.
max_trail = int(trail_secs / dt)
arrayofpoints = []
arrayofdistances = []
# The gravitational acceleration (m.s-2).
g = 9.81
filenames = []
listofangles = []


# Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
# Make an image every di time points, corresponding to a frame rate of fps
# frames per second.
# Frame rate, s-1
fps = 20
di = int(1/fps/dt)
fig = plt.figure(figsize=(8.3333, 6.25), dpi=72)
ax = fig.add_subplot(111)
def deriv(y, t, L1, L2, m1, m2):
    """Return the first derivatives of y = theta1, z1, theta2, z2."""
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)

    theta1dot = z1
    z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
             (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2dot = z2
    z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) +
             m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    return theta1dot, z1dot, theta2dot, z2dot

def calc_E(y):
    """Return the total energy of the system."""

    th1, th1d, th2, th2d = y.T
    V = -(m1+m2)*L1*g*np.cos(th1) - m2*L2*g*np.cos(th2)
    T = 0.5*m1*(L1*th1d)**2 + 0.5*m2*((L1*th1d)**2 + (L2*th2d)**2 +
            2*L1*L2*th1d*th2d*np.cos(th1-th2))
    return T + V
def convert(file,overwrite=False,keep=True):
    if not file.endswith('.gif'):
        return
    base_name = file[:-4]
    target = base_name + ".mp4"
    if os.path.exists(target) and not overwrite:
        return
    duration = get_duration(file)
    frame_count = get_frame_count(file)
    if not frame_count:
        return
    if not duration:
        frame_rate = 5
    else:
        frame_rate = frame_count/duration
    cmd("ffmpeg -v quiet -r " + str(frame_rate) + " -i  " + file + " -crf 20 -tune film -preset veryslow -y -an " + target)
    if not keep:
        os.system("rm " + file)
def calc_distance(x2, y2):
    return math.sqrt(math.pow(x2, 2) + math.pow(y2,2))
def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)
    filenames = []
    return output_file
for i in range(-80,90,10):
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
    listofangles.append(i + 10)
    listofangles.append(i - 10)
"""angle1 = 0 #float(input("Angle 1: "))
velocity1 = 0
angle2 = angle1
velocity2 = 0
y0 = np.array([math.radians(angle1 + 90), velocity1, math.radians(angle2 + 90), velocity2])

# Do the numerical integration of the equations of motion
y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))

# Check that the calculation conserves total energy to within some tolerance.
EDRIFT = 2 #0.05
# Total energy from the initial conditions
E = calc_E(y0)
if np.max(np.sum(np.abs(calc_E(y) - E))) > EDRIFT:
    sys.exit('Maximum energy drift of {} exceeded.'.format(EDRIFT))

# Unpack z and theta as a function of time
theta1, theta2 = y[:,0], y[:,2]

# Convert to Cartesian coordinates of the two bob positions.
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2) """


"""framepath = "a1.{}v1.{}a2.{}v2.{}".format(angle1, velocity1, angle2, velocity2)
os.mkdir(framepath)
os.chdir(framepath)
os.mkdir(framepath + "frames")"""

def make_plot(i, framepath, x1, x2, y1, y2):
    # Plot and save an image of the double pendulum configuration for time
    # point i.
    # The pendulum rods.
    ax.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], lw=2, c='k')
    # Circles representing the anchor point of rod 1, and bobs 1 and 2.
    c0 = Circle((0, 0), r/2, fc='k', zorder=10)
    c1 = Circle((x1[i], y1[i]), r, fc='b', ec='b', zorder=10)
    c2 = Circle((x2[i], y2[i]), r, fc='r', ec='r', zorder=10)
    print(x2[i],y2[i])
    print(calc_distance(x2[i], y2[i]))

    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)
    arrayofpoints.append(("({},{})").format(x2[i],y2[i]))
    arrayofdistances.append(calc_distance(x2[i],y2[i]))

    # The trail will be divided into ns segments and plotted as a fading line.
    ns = 20
    s = max_trail // ns

    for j in range(ns):
        imin = i - (ns-j)*s
        if imin < 0:
            continue
        imax = imin + s + 1
        # The fading looks better if we square the fractional length along the
        # trail.
        alpha = (j/ns)**2
        ax.plot(x2[imin:imax], y2[imin:imax], c='r', solid_capstyle='butt',
                lw=2, alpha=alpha)

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    ax.set_xlim(-L1-L2-r, L1+L2+r)
    ax.set_ylim(-L1-L2-r, L1+L2+r)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    #framepath = "a1.{}v1.{}a2.{}v2.{}".format(angle1, velocity1, angle2, velocity2)
    #os.mkdir(framepath)
    plt.savefig('{}/{}_img{:04d}.png'.format(framepath + "frames",framepath, i//di), dpi=72)
    filenames.append('{}/{}_img{:04d}.png'.format(framepath + "frames",framepath, i//di))
    #plt.savefig('{}/img{:04d}.png'.format(framepath + "frames", i//di), dpi=72)
    plt.cla()


# add something so that it can write the set of points to a file
def run(angle):
    angle1 = angle #float(input("Angle 1: "))
    velocity1 = 0
    angle2 = angle
    velocity2 = 0
    print(angle1)
    print(angle2)
    y0 = np.array([math.radians(angle1 + 90), velocity1, math.radians(angle2 + 90), velocity2])

    # Do the numerical integration of the equations of motion
    y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))

    # Check that the calculation conserves total energy to within some tolerance.
    EDRIFT = 7 #0.05
    # Total energy from the initial conditions
    E = calc_E(y0)
    if np.max(np.sum(np.abs(calc_E(y) - E))) > EDRIFT:
        sys.exit('Maximum energy drift of {} exceeded.'.format(EDRIFT))

    # Unpack z and theta as a function of time
    theta1, theta2 = y[:,0], y[:,2]

    # Convert to Cartesian coordinates of the two bob positions.
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    # Plotted bob circle radius
    r = 0.05
    # Plot a trail of the m2 bob's position for the last trail_secs seconds.
    trail_secs = 1
    angle1 = angle
    angle2 = angle
    framepath = "a1.{}v1.{}a2.{}v2.{}".format(angle, 0, angle, 0)
    os.mkdir(framepath)
    os.chdir(framepath)
    os.mkdir(framepath + "frames")
    print(angle)
    for i in range(0, t.size, di):
        print(i // di, '/', t.size // di)
        make_plot(i, framepath, x1, x2, y1, y2)
    filepath = "Desktop/Double\ Pendulum/Point\ Data/"
    filename = "a1.{}v1.{}a2.{}v2.{}.txt".format(angle, 0, angle, 0)
    filename1 = "a1.{}v1.{}a2.{}v2.{}distances.txt".format(angle, 0, angle, 0)
    file = open(filename, "w")
    for temp in arrayofpoints:
        file.write(temp + ",")
    file.close()
    file1 = open(filename1, "w")
    for temp in arrayofdistances:
        tempstring = "{},".format(temp)
        file1.write(tempstring)
    file1.close()
    #gifname = create_gif(filenames, tmax)
    #gif2mp4.convert(gifname)
    os.chdir("..")

    print(os.getcwd())

    print("done")
