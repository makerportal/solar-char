# Solar Panel Characterization with Arduino
Solar panel characterization with Arduino, with data analyses in Python.

Get your Solar Panel Datalogger Kit: [Solar Panel Datalogger Kit for Arduino](https://makersportal.com/shop/solar-panel-datalogger-kit-for-arduino) <br>
See full tutorial here: [Solar Panel Characterization and Experiments with Arduino](https://makersportal.com/blog/solar-panel-characterization-and-experiments-with-arduino) <br>

# 
### JUMP TO:
<a href="#wiring">- Wiring Diagram</a><br>
<a href="#arduino">- Arduino Code Usage</a><br>
<a href="#python">- Arduino Code Usage</a><br>
<a href="#results">- Example Output Plots</a><br>

The TinyBlueX library can be downloaded using git:

    git clone https://github.com/makerportal/solar-char

<a id="wiring"></a>
# - Wiring Diagram for Solar Datalogging-

The wiring between the components and the Arduino BLE-Nano board is given below:
![Solar Char Wiring](/images/experiment_setup_wiring_github.jpg)

Note: we have omitted any explanation of the wiring configuration in order to declutter the tutorial, however, most of the wiring explanations can be found either on our site or in other literature/forums online. We will discuss the solar panel, potentiometer (rheostat), and INA226 current/voltage configuration later in the experimental setup section. The rest are left for the user to explore.

<a id="arduino"></a>
# - Arduino -

We first need to characterize the panel’s output range to find the optimal operating voltage. We do this by turning the rheostat (potentiometer) from minimum to maximum in order to vary the load on the solar panel. First, the Arduino code that logs and prints voltage and current must be uploaded to the microcontroller. In our case, we’re using the BLE-Nano, which acts similar to the Arduino Nano and Uno boards (ATmega328P at the center). 

The code used to log and print voltage and current is given at the following code under the arduino folder:

- solar_rheostat.ino
    
<a id="python"></a>
# - Python -

Python rheostat code:
- python_rheostat.py

<a id="results"></a>
# - Results -
![Solar Panel Char Output](images/solar_panel_char_output.png)

![Solar Panel Diurnal Plot](images/solar_output_diurnal_profile_github.png)

