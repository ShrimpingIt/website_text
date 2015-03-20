# Minimal Button Circuit, and Conductive Sensor

This activity demonstrates the construction of a voltage divider which operates like a button circuit.

one half of the divider is a very high-value resistor, and the circuit is completed by a human body touching two contacts. 

## Build

- add a single 20 MegaOhm [pull up resistor](../topics/pullup.html), a ground wire and a sensor wire
- upload code which reports the sensed voltage by sending number characters over the Serial link
  - use the Serial Monitor feature within the Arduino IDE to monitor the numbers sent
  - observe the effect on the numbers when a human body connects the two wires
  - it's possible to plot the voltage signal by using Processing or Python

Open the AnalogInOutSerial sketch