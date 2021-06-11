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
fig = plt.figure(figsize=(15,10)) 
ax = fig.add_subplot(211)
ax.tick_params(labelsize=14)

ax.plot(voltage_V,current_mA,linewidth=3.5,color=plt.cm.tab20c(0),
        label='54mm x 54mm Solar Panel') # plot V vs I
ax.set_xlabel(r'$V$, Voltage [V]',fontsize=16)
ax.set_ylabel(r'$I$, Current [mA]',fontsize=16)

ax2 = fig.add_subplot(212)
ax2.tick_params(labelsize=14)

power_W = voltage_V*(current_mA/1000.0) # power output [W]
max_P_volt = voltage_V[np.argmax(power_W)] # max power Voltage [V] 
maX_P_curr = current_mA[np.argmax(power_W)] # max power current [mA]
max_power_W = np.max(power_W) # max power [W]

ax.plot(np.repeat(np.max(voltage_V),len(current_mA)),current_mA,
        linestyle='dotted',color=plt.cm.tab20c(4)) # open-circuit voltage
ax.plot(voltage_V,np.repeat(np.max(current_mA),len(voltage_V)),
        linestyle='--',color=plt.cm.tab20c(1)) # short-circuit current

ax2.plot(voltage_V,power_W,linewidth=3.5,color=plt.cm.tab20c(8),
         label='54mm x 54mm Solar Panel') # plot V vs I

ax2.plot(np.repeat(max_P_volt,len(power_W)),power_W,
         linestyle='dotted',color=plt.cm.tab20c(12)) # plot max voltage
ax2.plot(voltage_V,np.repeat(max_power_W,len(voltage_V)),
         color=plt.cm.tab20c(9),linestyle='--') # plot max current

ax2.set_xlabel(r'$V$, Voltage [V]',fontsize=16)
ax2.set_ylabel(r'$P$, Power [W]',fontsize=16)

ax.legend(fontsize=14)
ax2.legend(fontsize=14)

print("Max Power: {0:2.2f} W\nMax Power Voltage: {1:2.2f} V\nMax Power Current: {2:2.2f} mA".format(
    max_power_W,max_P_volt,maX_P_curr)+"\nOpen-Circuit Voltage: {0:2.2f} V".format(np.max(voltage_V))+
      "\nShort-Circuit Current: {0:2.2f} mA".format(np.max(current_mA)))

plt.savefig('solar_panel_char_output.png',dpi=300,bbox_inches='tight',facecolor='#FFFFFF')
plt.show() # show plot
