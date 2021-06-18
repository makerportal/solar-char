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

Arduino rheostat code:
- solar_rheostat.ino
    
<a id="python"></a>
# - Python -

Python rheostat code:
- python_rheostat.py

<a id="results"></a>
# - Results -
![Solar Panel Char Output](images/solar_panel_char_output.png)

![Solar Panel Diurnal Plot](images/solar_output_diurnal_profile_github.png)

