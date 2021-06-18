# Solar Panel Characterization with Arduino
Solar panel characterization with Arduino, with data analyses in Python.

Get your Solar Panel Datalogger Kit: [solar panel kit](https://makersportal.com/shop/solar-panel-datalogger-kit-for-arduino) <br>

# 
### JUMP TO:
<a href="#wiring">- Wiring Diagram</a><br>
<a href="#example">- TinyBlueX BLE Chat with the BLExAR iOS App</a><br>
<a href="#control">- Control Code for TinyBlueX</a><br>
<a href="#data">- Sending Temperature Data From TinyBlueX to iOS Device</a><br>

The TinyBlueX library can be downloaded using git:

    git clone https://github.com/makerportal/solar-char

<a id="wiring"></a>
# - Wiring Diagram for Solar Datalogging-

The wiring between the components and the Arduino BLE-Nano board is given below:
![Solar Char Wiring](/images/experiment_setup_wiring_github.jpg)

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

