# Wiring a Memory Game

![An alarm clock][header]

This guide provides details for learners to wire, program and configure a @ShrimpingIt Memory Game project, inspired by [M.B. Games Simon](http://en.wikipedia.org/wiki/Simon_%28game%29). For general orientation, see the Memory Game [project page](./index.html). The completed build should replicate the image shown on the left.

For convenience, [pre-bagged kits](../../kit/memory.html) are available to order from @ShrimpingIt online. If you do not wish to buy from us, [information is provided](../../kit/memory.html#bom) for you to source commodity parts direct from electronics wholesalers.

## Getting started

![Blink Layout][step00]

Before embarking on the Memory Game, you should have **successfully completed the [Blink build](../blink/build.html)**. Uploading the Blink program to the Blink layout proves that the foundations for the Memory Game layout are correct.

However, the Blink build for the Memory Game doesn't use a single 400 point breadboard. Instead, the ATmega chip is inserted at the centre of two docked 170 point breadboards, straddling them as shown. The breadboards have lugs which allow one of the boards to slide in and lock next to the other.

Once they are docked together, use the centre area to follow the [Blink](../blink/build.html) instructions. Once you have demonstrated you can [upload code](../blink/program.html) to the circuit, you can continue the Memory Game build.

***Dock two 170 point breadboards together.***
***Complete the [Blink build](../blink/build.html) placing the circuit at the centre of the breadboards as shown***
***Make sure you can [upload 'Blink'](../blink/program.html) to the circuit***

## Remove surplus parts

![Blink components to remove][step01]

After you've tested Blink and proven you can upload code, you can remove the Blink LED and resistor as these are not used in the final circuit, and it will be easier to wire the circuit with them out of the way.

***Take out the 'Blink' LED and Resistor***

## Move 9-pin header

![Moving 9 pin header][step02]

The 9-pin header uses an area on the left breadboard where we would like to add some backlit buttons.

Since the five holes in each row are equivalent (they are connected together inside the breadboard), we can move the header across to give us more room, without affecting the circuit.

It will avoid errors and save you time later if you leave the UART ribbon cable wiring intact following your Blink testing.

***Move the 9-pin programming header across by two columns, placing its first pin in h2 and its last pin in h10***

## Buttons

![Backlit Buttons][step03]

Remove the small black plastic nodules underneath the buttons to get the best contact. You can bend these nodules off with a pair of pliers. Be careful not to damage the pins  if you use wire cutters! 

The four thick legs are linked to the switch mechanism (the two thin legs connect to the lights inside). Those four legs need to be bent to fit. Away from the ATmega chip, the legs need to be flattened so they run down the side of the button. Nearer the chip, the legs need to splay out to reach over a gap, then have a right-angle bend into the board. 

As you slide in the button use long-nose pliers or a cocktail stick to ensure the LED legs slide in straight to the hole without bending. Straighten them again if necessary. Only push the button in to its final seating position when all pins are visibly aligned with the right holes.

***Remove the black plastic nodules from the base of each backlit button and bend the switch legs to match diagram***
***Guide Buttons' switch pins and LED pins gently into alignment with the holes shown in the diagram, then push down firmly ***

## Current-limiting Resistors

![100 Ohm Series Resistors][step04]

The light-emitting diodes (LEDs) inside the backlit buttons are very small and are not able to handle high voltages, even for a moment. You must be careful not to attach them to any 5V pin or they will receive too much current, overheat and fail. For this reason, we'll be adding a 100 Ohm current-limiting resistor, so that our 5V pins can safely light up the buttons.

The resistors connect from a software-controllable pin in between the button legs, and connect to the positive side of the LEDs. The positive is the side of the LEDs *without* a red dot. The resistor wire must be inserted in the same row as the LED leg, but inserting it actually in the same hole can make contact more reliable.

***Attach four 100 Ohm resistors from f7->e4, g14->e17 on the left breadboard, and d7->f4, d14->f17 on the right breadboard***

## Button Ground Wires

![Ground wires][step05]

When a voltage is applied through the resistor on the other side of the LED, the current has to flow somewhere. Each of the LEDs will need a ground connection to the row containing its negative pin. A red painted dot is there as an indicator mark showing which pin is negative. 

To achieve this, we'll connect the two neighbouring rows containg LED ground pins to each other, then connect them both back to a nearby ground rail.

***Add green wires from c10->c11 on the left breadboard and h10->h11 on the right breadboard, connecting the LED ground pins together***
***Add green wires from d11->f10 and g11->e9 to connect the LED ground pins to a ground rail***  

## Piezo Circuit

![Piezo Circuit][step06]

Melodies will play a part in our game, meaning we need to attach an audio output. 

A piezo transducer should be attached with one pin in row 1 and another pin in row 2. Piezos can have slightly different pin separations and can require some force to insert. Take a look from the side to check where the pins are actually entering the breadboard.

The orange wire connects the system to a [PWM](../../topic/pwm.html) capable pin.  Our library will generate different tones according to melodies specified in the Arduino code, using RTTTL (Ring Tone Text Transfer Language  - a format originally used by old mobile phones).

A resistor will complete the circuit, providing a connection back to ground, but also helping to limit the current used by the Piezo. This restricts the volume and helps to maintain the stability of the circuit's power supply when the melodies are playing. 

***Insert the Piezo transducer with one pin in row 1 and another in row 2 (as illustrated)***
***Add an orange wire from d12->a2***
***Add a 100 Ohm resistor from d12->a2***

## Rewiring the header

![Wire colors to attach to the header][step07]

If your USB UART module is not currently wired in place, the color-coded circles on the 9-pin header in this diagram indicates the proper connections to make. 

Refer to the [Blink build](../blink/build.html) for more details of the wiring colors for your UART module.

## Upload code

![Finished circuit][step08]

The sketches and libraries needed should be automatically configured and available under File=>Sketchbook=>shrimpingit=>Memory once you've completed the [@ShrimpingIt software instructions](../shrimp/program.html). Take a look at the [Memory Game programming page](program.html) for more details of the different software behaviours your Memory Game can perform.

[header]: kit.png
[step00]: ./sequence/00_blink.png
[step01]: ./sequence/01_blink_remove.png
[step02]: ./sequence/02_move_header.png
[step03]: ./sequence/03_buttons.png
[step04]: ./sequence/04_button_resistors.png
[step05]: ./sequence/05_button_grounds.png
[step06]: ./sequence/06_piezo_circuit.png
[step07]: ./sequence/07_uart_key.png
[step08]: ./sequence/08_finished.png


