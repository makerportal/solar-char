/***************************************************************************
* Arduino Solar Panel Long-Term Datalogger 
*  -- with INA226 + SD module + BLE Nano + Rheostat (Potentiometer)
*  --       + LiPo battery 
*
* 
*  by Josh Hrisko | Maker Portal LLC (c) 2021
* 
* 
***************************************************************************/
#include <Wire.h>
#include <INA226_WE.h>
#include <SPI.h>
#include <SD.h>
#include <LowPower.h>

#define I2C_ADDRESS 0x40 // INA226 I2C address

const int chipSelect = 4; // chip select for SD module
 
String filename = "SolarLog.csv"; // filename for saving to SD card

INA226_WE ina226(I2C_ADDRESS); // INA226 handler

void setup() {
  Serial.begin(9600); // start serial monitor for debugging
  Wire.begin(); // start I2C comm.
  ina226.init(); // initialize INA226

  if (!SD.begin(chipSelect)) { // verify SD card and module are working
    Serial.println("SD Card not found"); 
    while (1);
  }

  if (SD.exists(filename)) {
    SD.remove(filename); // delete file if it already exists
  }
 
  data_saver("Time [ms],Voltage [V], Current [mA]"); // save data header
  
  ina226.waitUntilConversionCompleted(); // allow INA226 to settle
}

void loop() {
  // preallocate INA226 variables
  float shuntVoltage_mV = 0.0; float loadVoltage_V = 0.0;
  float busVoltage_V = 0.0; float current_mA = 0.0;
  float power_mW = 0.0;
  
  String data_to_save = ""; // data string for saving

  // Grabbing voltage/current from INA226:
  ina226.readAndClearFlags();
  shuntVoltage_mV = ina226.getShuntVoltage_mV();
  busVoltage_V = ina226.getBusVoltage_V();
  current_mA = ina226.getCurrent_mA(); // current data
  loadVoltage_V  = busVoltage_V + (shuntVoltage_mV/1000); // total load voltage

  // print voltage/current for debugging with BLExAR app or serial monitor
  Serial.print("Volt: "); Serial.print(loadVoltage_V); Serial.println(" V");
  delay(50);
  Serial.print("Curr: "); Serial.print(current_mA); Serial.println(" mA"); 

  data_to_save += String(millis())+","; // add millisecond timestamp
  data_to_save += String(loadVoltage_V,2)+","; // add voltage data in [V]
  data_to_save += String(current_mA,2); // add current data in [mA]

  data_saver(data_to_save); // save new data points

  delay(100);
  for (int ii=0;ii<8;ii++){ // sleep 64 seconds before next data point
   LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF); // sleep routine to lower power consumption
  }
  delay(100);
}

void data_saver(String WriteData){ // data saver function
  File dataFile = SD.open(filename, FILE_WRITE); // open/create file

  if (dataFile) {
    dataFile.println(WriteData); // write data to file
    dataFile.close(); // close file before continuing
  } else {
    delay(50); // prevents cluttering
    Serial.println("SD Error"); // print error if SD card issue
  }

}
