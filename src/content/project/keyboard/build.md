# About this Guide

![Conductive Keyboard Kit cover][header]

This guide provides details for learners to wire, program and configure a @ShrimpingIt conductive keyboard.

For orientation, see the [Conductive Keyboard](../keyboard/index.html) project page.

For convenience, [pre-bagged kits](../../kit/keyboard.html) are available to order from @ShrimpingIt online. If you do not wish to buy from us, [information is provided](../../kit/keyboard.html#bom) for you to source commodity parts direct from electronics wholesalers.

## Getting started

![Blink Layout][step00]

Before embarking on the Conductive Keyboard, you should have **successfully completed the [Blink build](../blink/index.html)**. This build uses the Blink circuit as its starting point. 

## Surplus parts

![Remove Blink parts][step01]

You can remove the Blink LED and resistor as these are not used in the circuit, and it will be easier to wire the circuit with them out of the way.

## Move 9-pin header

![Moving 9 pin header][step02]

The 9-pin header uses an area where we would like to add some pull-up resistors later in the build.

Since the five holes in each row are equivalent (they are connected together inside the breadboard), we can move the header across to give us more room, without affecting the circuit.

Although the coloured UART ribbon cable is not shown, it will avoid errors and save you time later if you leave the wiring intact following your Blink testing.

***Move the 9-pin programming header across by two columns, placing its first pin in h2 and its last pin in h10***

## Right Power Rails 

![Connecting power rails][step03]

The power rails on the right must be connected to +5V and 0V, the same as the ATMEGA's power pins. These will be used to provide the +5V signal for the Right-hand [Pull-ups](../topic/pullup.html) which are so fundamental to the behaviour of a [MakeyMakey](http://makeymakey.com/). 

The right-hand power rails will also be a convenient place to connect the +5V and 0V wires when the project is running as a USB keyboard from the hacked USB cable we'll attach later.

***Attach a Green wire from J9 horizontally and slightly down to the -ive (Blue) power rail on the right***
***Attach a Red wire from J11 horizontally and slightly up to the +ive (Red) power rail on the right*** 

## USB cable

![Hacked USB Cable][step04]

When complete, our system will emulate a USB 1.1 keyboard. A USB 1.1 cable is made up of four wires with a standard color code. 

Two wires provide power +5V (Red) and 0V (Black), connected to the power rails. The other two are Data+ (or D+, Green) and Data- (or D-, White), for sending data back and forth between the host (laptop) and the peripheral device (keyboard). We'll attach these to free rows above the ATMEGA chip for later connections to be made.

@ShrimpingIt [bagged kits](../../kit/keyboard.html) contain a Male type A plug cut from a generic USB cable, with crimped male header pins guaranteeing breadboard connectivity. However, you can use any USB cable chopped in half, soldering pins on the end, or sliding all the strands of each wire carefully into a breadboard hole before jamming in a male header pin to hold it in place and in contact.

***Attach Data+ Green wire to J1***
***Attach Data- White wire to J2***
***Attach +5V to the second hole in the right hand +ive power rail***
***Attach 0V to the second hole in the right hand -ive power rail***

## Regulating Zener Diodes 

![USB Signalling Zener Diodes][step05]

The Data+ (Green USB) and Data- (White USB) signals accept a maximum of 3.6V. We can use Zeners to guarantee this. Essentially, any voltage above 3.6V is allowed to bleed away through the Zener.

Zener diodes are tiny red and black cylinders on a silver wire. A diode operates like a water valve, allowing current to flow freely in one direction, but resisting it in the other direction. However, a Zener is a special kind of diode, like a leaky water valve. Zeners normally resist current flowing backwards, but they 'break down' (make a [short circuit](../../topic/shortcircuit.html)), when the reverse pressure (voltage) applied exceeds a certain threshold. 

***Attach the two small Zener diodes from h9->h2 and i9->i1 making sure the black ends connect to the green and white USB wires***

## USB 1.1 resistors

![USB Resistors][step06]

We'll generate signals in software to make the ATmega's pin 4 and pin 6 behave like D+ and D- of a USB 1.1 keyboard, but the signal from the ATmega is at 5V when it should be at 3.6V to be conformant to the standard.

The Zener diodes effectively 'short-circuit' anything above 3.6V feeding it directly to ground (0V). Using 68Ohm resistors to connect to D+ and D- wires limits the flow of current allowed through this short-circuit from our signalling ATmega, and dissipates exactly 1.4V of our 5V signal as heat before it gets to the USB wires.

The 2.2kOhm resistor is a [pullup](../topic/pullup.html) resistor. The presence of this resistor (and the strength of its pull) can be detected by the laptop when you connect the conductive keyboard, and it indicates that the laptop should try to connect at USB 1.1 'full speed' which is just 12.1 Mega bits-per-second. Note, on some USB hubs, this will limit ALL USB connections to be the speed of the slowest device.

Each of the colored bands corresponds with a single figure number in the resistor code. Resistor codes begin at the end opposite the gold (quality) stripe. The 68Ohm resistors have Blue, Grey, Black for a code sequence 6, 8, 0. The first two figures of the resistance in Ohms are 6 and 8, and this should be followed by no extra zeroes, in other words 68() or 68Ohms. The 2.2 kOhm resistors have Red, Red, Red for a code sequence 2, 2, 2. The first two figures are 2 and 2, and this should be followed by two extra zeroes, in other words 22(00) or 2,200 Ohms. There are 1000 Ohms in a kiloOhm so that's the same as 2.2 kOhms.

***Connect a 68Ohm resistor from d6 to f1***
***Connect a 68Ohm resistor from d8 to f2***
***Connect a 2.2KOhm resistor from g2 to the right hand +ive (Red) power rail, just below the red USB wire***

## Run Hello World

![Circuit for Hello world][step06a]

Now the USB circuit is complete, it should be able to connect to a computer as a USB device. So we'll upload a behaviour which makes it pretend to be a USB keyboard, and type some text automatically.

To test this, navigate to File=>Sketchbook=>shrimpingit=>Keyboard=>[Keyboard00HelloWorld](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/keyboard/Keyboard00HelloWorld/Keyboard00HelloWorld.ino) to load some new code (this assumes you've already configured your software when [testing Blink](http://start.shrimping.it/project/blink/build.html#step12)).

After the code opens in the Arduino IDE, choose File=>Upload to upload the code. It should report 'Done Uploading' and no red error text should be visible in the bottom panel.

Now open a new Sketch in the Arduino IDE and place your cursor inside. We're just going to use this as a scratchpad to see the typing which our hacked keyboard will generate.

Once you plug in the hacked USB cable, it should appear as a keyboard and begin typing the text 'hello world'. You could already use this circuit for a practical joke [like this](http://imakeprojects.com/Projects/haunted-usb-cable/) (use a long timer before typing) or to log into your computer automatically by typing your username and password. We're not going to stop here, though.

***Load the [Keyboard00HelloWorld](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/keyboard/Keyboard00HelloWorld/Keyboard00HelloWorld.ino) program from File=>Sketchbook=>shrimpingit=>Keyboard***
***Launch a text editor***
***Plug in the Hacked USB cable, it should appear as a keyboard and start typing***

## First Pull-up

![Pullup Resistor #1][step07]

Next we're going to attach a series of [pull-up](../../topic/pullup.html) resistors which are so strong that a human body is relatively *much* more conductive. 

When we're not touching a pad on the conductive keyboard, the only connection to the ATMEGA's top-right pin will be a 20 MegaOhm resistor pulling it to nearly +5V. This +5V signal is an indication to the ATMEGA that we're *not* touching the pad.

When we touch a pad on the conductive keyboard, our bodies provide the connection to 0V (Ground). Because our body's has a lower-resistance connection to ground than the 20MegaOhm connection to 5V, our body can pull down the ATMEGA's sensing pin to nearly 0V. This 0V connection made through our body is an indication to the ATMEGA that we *are* touching the pad.

The 20 MegaOhm resistors have Red Black, Blue for a code sequence 2, 0, 6. The first two figures are 2 and 0, and this should be followed by six extra zeroes, in other words 20(000000) Ohms. There are 1000000 Ohms in a MegaOhm so that's the same as 20 MegaOhms.

***Connect a 20MegaOhm resistor between j3 and the next free hole on the right-hand +ive (Red) power rail***

## Test conductive sensing

![Wiring yourself][step08]

Now we are ready to add some wires to make a conductive keyboard.

***Upload the [Keyboard01Single](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/keyboard/Keyboard01Single/Keyboard01Single.ino) program from File=>Sketchbook=>shrimpingit=>Keyboard***
***Load a Text Editor***
***Attach the Hacked USB cable as a Keyboard***
***Attach a jumper wire or crocodile clip to g2***
***Attach a jumper wire or crocodile clip to a ground rail***
***Try touching both at once, making a human circuit. A '1' character should be typed***
***Prove other ways that current can be detected, for example through...***
* ***fruit***
* ***a glass of water***
* ***conductive graphite drawn on paper with a pencil***
* ***tin foil***
* ***lots of people holding hands***

## More Right Hand Pullups

![Pullup Resistors #2 to #15][step09]

We can have multiple different wires which can be monitored independently. In this way, you can create a Banana Piano with up to 16 keys!

Let's start by wiring the extra pull-ups on the right hand side.

***Connect 20MegaOhm resistors from j4,j5,j6,j7,j8,j12,j13,j14,j15,j16 to the next free holes on the right-hand +ive (Red) power rail***

## Left Pullups

![Connecting Left Power Rails][step10]

There are just eleven inputs available on the right hand side of the ATmega, so we'll use the left-hand side to give us another five. 

We activate the left-hand +ive power rails by attaching a +5V connection for the left-hand pullup resistors we will need. As good practice, we're also wiring the ground rail at the same time, even though we're not using it yet. 

Now the power rail is active, we can add the extra five 20MegaOhm [pull-up](../../topic/pullup.html) resistors.

***Attach a Green wire from the Right Hand -ive (Blue) power rail to the Left Hand -ive (Blue) power rail ***
***Attach a Red wire from the Right Hand +ive (Blue) power rail to the Left Hand +ive (Blue) power rail ***
***Attach 20MegaOhm resistors from j16,j15,j14,j13 to the nearest holes on the Left-hand +ive (Red) power rail***
***Attach a 20MegaOhm resistor from A7 to the nearest hole on the Left-hand +ive (Red) power rail*** 

[header]: ./kit.png
[step00]: ./sequence/00_blink.png
[step01]: ./sequence/01_blink_remove.png
[step02]: ./sequence/02_move_header.png
[step03]: ./sequence/03_right_power.png
[step04]: ./sequence/04_usb_cable.png
[step05]: ./sequence/05_usb_diodes.png
[step06]: ./sequence/06_usb_resistors.png
[step06a]: ./sequence/06a_hello_world.png
[step07]: ./sequence/07_first_pullup.png
[step08]: ./sequence/08_first_test.png
[step09]: ./sequence/09_right_pullups.png
[step10]: ./sequence/10_left_pullups.png
[final]: ./sequence/11_final.png
[final_header]: ./sequence/12_final_headers.png
