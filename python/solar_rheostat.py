##################################################
#
# Python Solar Panel Characterization
# -- analyzing Arduino .csv data
#
# by Joshua Hrisko | Maker Portal LLC (c) 2021
#
##################################################
#
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv

##################################################
# Data parsing from .csv
##################################################
#
filename = "SOLARLOG.CSV" # csv filename

data_array = [] # for saving variables 
with open(filename,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader) # print header
    for row in csvreader:
        data_array.append(row) # save data to variable array

start_pt = 0 # start point
end_pt   = int(0.8*(np.shape(data_array)[0])) # end point
data_array = data_array[start_pt:end_pt] # select the portion of data with valid data
time_vector = np.array([float(ii[0]) for ii in data_array]) # time in [ms] since start of program
voltage_V   = np.array([float(ii[1]) for ii in data_array]) # voltage in [V]
current_mA  = np.array([float(ii[2]) for ii in data_array]) # current in [mA]

##################################################
# Data Plotting of Voltage [V] vs Current [mA]
##################################################
#
plt.style.use('ggplot') # style plot
fig = plt.figure(figsize=(14,9)) 
ax = fig.add_subplot(211)
ax.tick_params(labelsize=14)

ax.plot(voltage_V,current_mA,linewidth=3.5,color=plt.cm.Set1(1),
        label='54mm x 54mm Solar Panel') # plot V vs I
ax.set_xlabel(r'$V$, Voltage [V]',fontsize=16)
ax.set_ylabel(r'$I$, Current [mA]',fontsize=16)

ax2 = fig.add_subplot(212)
ax2.tick_params(labelsize=14)

power_W = voltage_V*(current_mA/1000.0) # power output [W]

ax2.plot(voltage_V,power_W,linewidth=3.5,color=plt.cm.Set1(0),
         label='54mm x 54mm Solar Panel') # plot V vs I

ax2.set_xlabel(r'$V$, Voltage [V]',fontsize=16)
ax2.set_ylabel(r'$P$, Power [W]',fontsize=16)

ax.legend(fontsize=14)
ax2.legend(fontsize=14)


plt.show() # show plot
