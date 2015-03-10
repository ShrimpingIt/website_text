# Conductive Keyboard, (ShrimpKey)

This project demonstrates how to build a substitute for the <a href="http://makeymakey.com/" target="_blank">MakeyMakey</a> USB conductive keyboard. 

Because it is constructed directly from component parts, it is cheaper and arguably more educational than a MakeyMakey. You can build the project by combining a [Shrimp](../shrimp/index.html) with a handful of resistors and diodes, a hacked USB cable and some jumper wires or crocodile clips.

## Learning Outcomes

This project introduces the concept of a [voltage divider](../topics/voltagedivider.html). It demonstrates how a [pull up resistor](../topics/pullup.html) ensures an unambiguous signal from a voltage divider circuit. 

From this starting point, advanced learners will be able to create their own button keypads, use [potentiometers](../topics/potentiometer.html) to control circuit behaviour, sense light levels using [Light Dependent Resistors](../topics/ldr.html), Temperature and Acceleration Sensors using these key principles of analog electronics.

It also demonstrates the fundamentals of the [Universal Serial Bus](../topics/usb.html) (USB). The circuit appears to laptops or tablets as a USB keyboard. The circuit proves that with just 2 wires connected and controlled in a suitable way, (plus power and ground wires) it's possible to emulate a device conforming to the USB Human Interface Device (HID) keyboard standard. Advanced learners will experiment with emulating different USB devices.

## Build Process

As with all [@ShrimpingIt](http://shrimping.it) projects, the build should begin by following the instructions to  [build and program Blink](http://shrimping.it/shrimp/project/blink).

Once your Shrimp is blinking, you can then proceed through the following builds...

1) Minimal Conductive Sensor


2) Minimal USB Keyboard
- add the minimum components for the circuit to be able to emulate a [USB keyboard](../topics/usb.html).
- upload code so that the circuit 'types' the phrase `Hello World!` every 10 seconds.
  - plug the hacked USB cable into a computer, launch a suitable application, and see the typing appear on the screen

3) Minimal Conductive USB Keyboard 
- add a single [pull up resistor](../topics/pullup.html) a ground wire and a contact wire
- Upload code which senses a human body making a circuit between the ground wire and the contact wire causes the USB Keyboard to 'type' the number `1`
  - plug the USB cable into a computer, launch a suitable application, and see the typing appear on the screen

4) ShrimpKey: Full Conductive Keyboard
- add the remaining 15 [pull up resistors](../topics/pullup.html) to create a total of 16 conductive sensors, making it possible to create compelling interactive demonstrations like the MakeyMakey demos below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rfQqh7iCcOU" frameborder="0" allowfullscreen></iframe>