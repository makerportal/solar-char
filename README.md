# Solar Panel Characterization with Arduino
Solar panel characterization with Arduino, with data analyses in Python.

Get your Solar Panel Characterization Kit: [solar panel kit](https://makersportal.com/shop/solar-panel-characterization-kit) <br>

# 
### JUMP TO:
<a href="#wiring">- Wiring Diagram</a><br>
<a href="#example">- TinyBlueX BLE Chat with the BLExAR iOS App</a><br>
<a href="#control">- Control Code for TinyBlueX</a><br>
<a href="#data">- Sending Temperature Data From TinyBlueX to iOS Device</a><br>

The TinyBlueX library can be downloaded using git:

    git clone https://github.com/makerportal/solar-char

<a id="wiring"></a>
# - Wiring Diagram for Uploading Code to the TinyBlueX-

The wiring between the TinyBlueX and Arduino Uno board required for uploading code to the TinyBlueX is given below:
![TinyBlueX Arduino Wiring](/images/TinyBlueX_arduino_uno_wiring.jpg)
| Arduino Uno | TinyBlueX |
| --- | --- |
| 5V | VCC |
| GND | GND | 
| D10 | 1 |
| D11 | 5 |
| D12 | 6 |
| D13 | 7 |
