import numpy as np
import array as arr
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from prettytable import PrettyTable
#--------from dataset----------#
galaxies = [
    "UGC858",
    "UGC1554",
    "UGC1633",
    "UGC3834",
    "UGC4888",
    "UGC5183",
    "UGC6376",
    "UGC7122",
    "UGC7393",
    "UGC7412",
    "UGC8033",
    "UGC9358",
    "UGC11218"
]

z = arr.array('d', [
    0.00795,
    0.00703,
    0.01426,
    0.00680,
    0.00756,
    0.00447,
    0.01426,
    0.00607,
    0.01412,
    0.00380,
    0.00832,
    0.00637,
    0.00496
])

m = arr.array('d', [
    10.9,
    11.4,
    11.4,
    11.4,
    11.3,
    10.3,
    10.4,
    11.8,
    12.4,
    10.2,
    10.8,
    10.2,
    10.0
])

M = arr.array('d', [
    -21.9,
    -20.7,
    -22.2,
    -20.9,
    -21.2,
    -21.3,
    -23.6,
    -20.7,
    -21.6,
    -20.6,
    -21.8,
    -21.8,
    -21.4
])

velocity = []
distance = []
#-------converting from given values to dataset----------------#
l = len(galaxies)
for i in range(l):
    t1 = (z[i]*3*10**(5)*(z[i]+2))/(z[i]*z[i] + 2*z[i] + 2)
    velocity.append(t1)
    t2 = (10**((m[i]-M[i]+5)/5))/(10**6)
    distance.append(t2)

#--------printing the table 1 --------------------------------#
t1 = PrettyTable()
t1.field_names = ["Galaxies", "Redshift", "Absolute Magnitude", "Apparent Magnitude"]
for i in range(l):
    t1.add_row([galaxies[i],z[i],M[i],m[i]])
print(t1)

#--------printing the table 2---------------------------------#
t2 = PrettyTable()
t2.field_names = ["Galaxies", "Radial Velocity(in km/s)", "Distance(in Mpc)"]
for i in range(l):
    t2.add_row([galaxies[i],velocity[i],distance[i]])
print(t2)

#----------finding slope of best-fit line of graph ----------#
y = np.array(velocity)
x = np.array(distance)
m, b = np.polyfit(x, y, 1)
print("Slope(Hubble's constant) : ",m)
print("Y-intercept : ",b)

#------------------------calculating the time---------------#
time_seconds = pow(10,20)/(m*3.2408)
time_minutes = time_seconds/60
time_hours = time_minutes/60
time_days = time_hours/24
time_years = time_days/365
time_billion = time_years/(pow(10,9))
print("age of univere: ",time_billion,"Billion Years")


#--------------------plotting the graph-------------------#
plt.grid()
plt.plot(x, y, 'o')
plt.plot(x, m*x+b)
for i in range(l):
    plt.annotate(galaxies[i], (x[i], y[i]))
plt.xlabel("Distance in Mpc or Mega-parsecs")
plt.ylabel("Radial velocity in km/s")
plt.show()
