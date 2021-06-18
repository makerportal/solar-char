##################################################
#
# Python Solar Panel Diurnal Analysis
# -- analyzing Arduino long-term .csv data
#
# by Joshua Hrisko | Maker Portal LLC (c) 2021
#
##################################################
#
#
import numpy as np
import matplotlib.pyplot as plt
import csv,datetime

##################################################
# Data parsing from .csv
##################################################
#
filename = "SOLARLOG_06_15_2021_to_05_16_2021.CSV" # csv filename

data_array = [] # for saving variables 
with open(filename,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader) # print header
    for row in csvreader:
        data_array.append(row) # save data to variable array

start_pt = 0 # start point
end_pt   = int(1.0*(np.shape(data_array)[0])) # end point
data_array = data_array[start_pt:end_pt] # select the portion of data with valid data
time_vector = (np.array([float(ii[0]) for ii in data_array])/1000.0) # time in [ms] since start of program
start_time = "06/15/2021 08:00 AM"
start_datetime = datetime.datetime.strptime(start_time,"%m/%d/%Y %H:%M %p")
t_datetime = [start_datetime+datetime.timedelta(ii/(3600.0*24.0)) for ii in time_vector]
voltage_V   = np.array([float(ii[1]) for ii in data_array]) # voltage in [V]
current_mA  = np.array([float(ii[2]) for ii in data_array]) # current in [mA]
power_W = voltage_V*(current_mA/1000.0)
#
##################################################
# Data Plotting of Power over Time
##################################################
#
plt.style.use('ggplot') # style plot
fig = plt.figure(figsize=(15,10)) 
ax = fig.add_subplot(211)
ax.tick_params(labelsize=14)

ax.plot(t_datetime,power_W,linewidth=3.5,color=plt.cm.tab20c(0),
        label='Time-Series Data') # plot t vs P
ax.set_xlabel(r'$t$, Time [m-d HH]',fontsize=16)
ax.set_ylabel(r'$P$, Power [W]',fontsize=16)
ax.legend()

#
##################################################
# Daily Power Output Approximation
##################################################
#
ax2 = fig.add_subplot(212)

t_hours = [ii.hour for ii in t_datetime] # convert to hours
unq_hours = np.unique(t_hours) # capture hours
mean_power = [] # storing mean values for each hour
for hour_ii in unq_hours:
    mean_power.append(np.mean(power_W[np.where(t_hours==hour_ii)]))

ax2.plot(unq_hours,mean_power,linewidth=3.5,color=plt.cm.tab20c(4),
        label='Hourly-Averaged Data',linestyle='-',marker='o',markersize=10,
         markerfacecolor=plt.cm.tab20c(6)) # plot V vs I
ax2.set_xlabel(r'$t_h$, Time-of-Day [hour]',fontsize=16)
ax2.set_ylabel(r'$P$, Power [W]',fontsize=16)
ax2.legend()

cell_area = 0.01*0.038 # cell area [m^2]
num_cells = 4 # number of cells contained in panel 
panel_area = (cell_area)*num_cells # panel area [m^2]
power_density = (np.trapz(mean_power,x=unq_hours)/1000.0)/panel_area # kWh/m^2
print("Daily Power Output: {0:2.1f} kWh/m^2/day".format(power_density))

ax.set_title('Solar Panel Diurnal Power Output',fontsize=20)
plt.show() # show plot
