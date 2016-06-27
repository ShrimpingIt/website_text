# Voltage Divider

<img src="diag.png" />

<!-- 
@ShrimpingIt provides a step-by-step [wiring guide](build.html), [example software](program.html) and detailed [sourcing information](../../kit/pov.html) for the components you need to make this project.
-->

This project demonstrates how the same simple [Voltage Divider](https://en.wikipedia.org/wiki/Voltage_divider) circuit, attached to a Shrimp's [Analog input](https://www.arduino.cc/en/Tutorial/AnalogInput) can be used to monitor many different sensors, measuring the following items which are available as part of an Addon kit of sensors that we ship for £1.50 retail, but which can easily be sourced for yourself...

* Temperature (Thermistor)
* Light (Light Dependent Resistor)
* Rotation (Potentiometer)
* Pressing (Button)
* Orientation (Tilt Switch)
* Albedo (Reflectance Sensor)
* Human touch (Human Skin)

Each of these items behaves like a variable resistor, so if you chain the item [in series](https://en.wikipedia.org/wiki/Series_and_parallel_circuits) with another resistor, the voltage measured in between them will vary as the share of resistance changes.

Using the Arduino [Analog Input](https://www.arduino.cc/en/Tutorial/AnalogInput) example, we can then get the Shrimp to report the changing voltage value over the [Serial link](https://www.arduino.cc/en/Reference/Serial) to your laptop.

It is also possible to treat the Shrimp as an 'IO Board' and query and control its pins [from Javascript or Python](https://github.com/firmata/arduino#firmata-client-libraries)

## Self-sourced resistive sensors

Although we have bundled a collection of the cheapest available resistive sensors in our kit, the following can also be sourced (below listed with indicative bulk cost per unit if you source for yourself from a wholesaler)

* 2-axis Joystick $0.60
* Humidity Sensor ~$0.80
* Weight Sensor ~$1.00
* Slide potentiometer/fader $1.00
* Resistive touchscreen digitizer $3
* Flex Sensor ~$8
* Membrane Potentiometer ~$10
* Motorized slide potentiometer/fader ~$30