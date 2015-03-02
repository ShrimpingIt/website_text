# Building the Conductive Keyboard

![Conductive Keyboard Kit cover][header]

This guide provides details for learners to wire, program and configure a @ShrimpingIt conductive keyboard.

For orientation, see the [Conductive Keyboard](../keyboard/index.html) project page.

## Requirements

The build assumes you have the following kits...

* A [Conductive Keyboard Addon](../keyboard/kit.html) kit
* A [Shrimp Parts](../shrimp/kit.html) kit
* A [Programmer](../shrimp/kit.html) kit

For convenience, pre-bagged kits are available to order from @ShrimpingIt online. If you do not wish to buy from us, information is provided for you to source commodity parts direct from electronics wholesalers.

In addition you will need a Linux, Mac or Windows computer running the latest [Arduino IDE](../topics/ide.html). 

Mac and Windows computers need a [CP2102 driver](../cp2102/driver.html) to be installed for the USB Programmer to be recognised.

## Getting started

Before embarking on the Conductive Keyboard, you should have **successfully completed the [Blink build](../blink/index.html)**. This build uses the Blink circuit as its starting point. 

### Step 1: Remove unnecessary parts

![Blink Layout][step01]

You can remove the Blink LED and resistor as these are not used in the circuit, and it will be easier to wire the circuit with them out of the way.

### Step 2: Connect Right-hand Power Rails 

![Connecting power rails][step02]

We will be using 

### Step 3: A hacked USB cable to connect as a keyboard

![Hacked USB Cable][step03]

### Step 4: Regulate USB signal levels with Zener Diodes  

![][step04]

### Step 5: USB Signalling and Pull-up Resistors 

![][step05]

### Step 6: Adding a pull-up resistor to test conductive sensing

![Pullup Resistor #1][step06]

### Step 7: Remaining Right Hand Pullups

![Pullup Resistors #2 to #15][step07]

### Step 8: Connecting the Left Power Rails

![Connecting Left Power Rails][step08]

### Step 9: Accessible Left Hand Pullups

![Connecting Left Power Rails][step09]

### Step 9: Last (bonus) pullup if needed

![Pullup Resistor #16][step10]

[header]: keyboard_kit.png
[step01]: ./sequence/01_blink.png
[step02]: ./sequence/02_rightpower.png
[step03]: ./sequence/03_usbcable.png
[step04]: ./sequence/04_usbdiodes.png
[step05]: ./sequence/05_usbresistors.png
[step06]: ./sequence/06_firstpullup.png
[step07]: ./sequence/07_rightpullups.png
[step08]: ./sequence/08_leftpower.png
[step09]: ./sequence/09_leftpullups.png
[step10]: ./sequence/10_lastpullup.png
[final]: ./sequence/11_final.png
