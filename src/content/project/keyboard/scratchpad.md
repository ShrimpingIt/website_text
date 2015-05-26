# 

From MakeyMakey - the starting keys...

int keyCodes[NUM_INPUTS] = {
  // top side of the makey makey board

  KEY_UP_ARROW,      // up arrow pad
  KEY_DOWN_ARROW,    // down arrow pad
  KEY_LEFT_ARROW,    // left arrow pad
  KEY_RIGHT_ARROW,   // right arrow pad
  ' ',               // space button pad
  MOUSE_LEFT,        // click button pad

  // female header on the back left side

  'w',                // pin D5
  'a',                // pin D4
  's',                // pin D3
  'd',                // pin D2
  'f',                // pin D1
  'g',                // pin D0

  // female header on the back right side

  MOUSE_MOVE_UP,      // pin A5
  MOUSE_MOVE_DOWN,    // pin A4
  MOUSE_MOVE_LEFT,    // pin A3
  MOUSE_MOVE_RIGHT,   // pin A2
  MOUSE_LEFT,         // pin A1
  MOUSE_RIGHT         // pin A0
};

## Equipment for Heysham High

#Tasks

* Laptops
	* Pack 1 through 22 or so
	* Get them networked 
	* Put the shrimpingit Sketchbook in place
	* Copy Arduino 1.6.4? Needed?
* Components
	* Strip and crimp Male USB cables
	* Replace 22kOhm resistors (cables too fat)
	* Bag jumpers or solid-core wire
* Vector Art
	* Voltage Divider layout(s)  
* Code
	* Augment sketchbook with
		* Potential divider demo
			* BBC Bitesize GCSE Electronics 
		* USB Hello World demo
		* USB 1 Resistor demo
		* USB 11 Resistor demo   

# To take

* 20 lots of 
	* Conductive Keyboard Addon
	* Shrimp Parts
	* 400 point breadboard
	* USB UART 
	* Potentiometer
	* Light Dependent Resistor
	* Tactile button
* A USB keyboard for Scratch Piano demo
* Fruit
	* Bananas, Onions
* 2B Pencils 
* * Blank white paper

# Sequence

* Video
	* Arduino Compilation video?
	* MakeyMakey video
* Blink build
* Voltage Divider intro
* Voltage divider demos
	* Arduino Analog example
	* Potentiometer
	* Light Dependent Resistor
	* Button
* Partial Conductive Keyboard build
	* Metal-to-metal
	* Human beans
	* Tape
	* Fruit
* Scratch Banana Piano
* USB Keyboard Hello World demo 
* USB Keyboard Add a Resistor
* USB Keyboard Add all the resistors

## Learning Outcomes

This project introduces the concept of a [voltage divider](../../topic/voltagedivider.html). It demonstrates how a [pull up resistor](../../topic/pullup.html) ensures an unambiguous signal from a voltage divider circuit. 

From this starting point, advanced learners will be able to create their own button keypads, use [potentiometers](../../topic/potentiometer.html) to control circuit behaviour, sense light levels using [Light Dependent Resistors](../../topic/ldr.html), Temperature and Acceleration Sensors using these key principles of analog electronics.

It also demonstrates the fundamentals of the [Universal Serial Bus](../../topic/usb.html) (USB). The circuit appears to laptops or tablets as a USB keyboard. The circuit proves that with just 2 wires connected and controlled in a suitable way, (plus power and ground wires) it's possible to emulate a device conforming to the USB Human Interface Device (HID) keyboard standard. Advanced learners will experiment with emulating different USB devices.

## Build Process

As with all [@ShrimpingIt](http://shrimping.it) projects, the build should begin by following the instructions to  [build and program Blink](http://shrimping.it/shrimp/project/blink).

Once your Shrimp is blinking, you can then proceed through the following builds...

1) Minimal Conductive Sensor


2) Minimal USB Keyboard
- add the minimum components for the circuit to be able to emulate a [USB keyboard](../../topic/usb.html).
- upload code so that the circuit 'types' the phrase `Hello World!` every 10 seconds.
  - plug the hacked USB cable into a computer, launch a suitable application, and see the typing appear on the screen

3) Minimal Conductive USB Keyboard 
- add a single [pull up resistor](../../topic/pullup.html) a ground wire and a contact wire
- Upload code which senses a human body making a circuit between the ground wire and the contact wire causes the USB Keyboard to 'type' the number `1`
  - plug the USB cable into a computer, launch a suitable application, and see the typing appear on the screen

4) ShrimpKey: Full Conductive Keyboard
- add the remaining 15 [pull up resistors](../../topic/pullup.html) to create a total of 16 conductive sensors, making it possible to create compelling interactive demonstrations like the MakeyMakey demos below.

