# Wiring a Memory Game

![An alarm clock][header]

After reading the guidance below, you should be able to build the circuit, referencing the printed diagram bagged with our kits (shown above).

Note this layout is based on two 170-point mini-breadboards placed next to each other. The chip should be at the centre, straddling two docked breadboards. 

With the chip in this position, you can follow the steps of the [Blink build](../blink/build.html), checking you can flash an LED before adding all the other components.

After completing Blink, it’s best to add the buttons before adding other components, as they route themselves over the top of the buttons. 

The buttons have small black plastic nodules underneath them which can distance them from the breadboard, and these should be removed to get the best contact. You can bend these nodules off with a pair of pliers. Be careful not to cut the pins off the buttons if you use wire cutters! 

Four of the six legs on the buttons need to be bent a little to fit. Towards the outside of the breadboards, the legs need to be flattened a little, making them flush with the sides of the buttons, whilst toward the inside, the legs need to splay out to reach over a gap. 

The two remaining, thinner legs, are attached to the built-in LED. A red painted dot is there as an indicator mark showing which is the negative pin. 

It can be handy to use a probe, such as a cocktail stick or long-nose pliers, to line up the button and LED legs with the proper holes, before pushing the button down into its final seating position. Some find that moving the resistor or green wire along the row, so they share a hole with the LED leg, can improve reliability of contact.

The sketches and libraries needed should be automatically configured and available under File=>Sketchbook=>shrimpingit=>Memory once you've completed the [@ShrimpingIt software instructions](../shrimp/program.html)

## Further Development

Why not try to change the code by Googling for other rtttl tunes which are more personal to you and putting them into your game. You could change the game behaviour altogether, making it into a quiz buzzer which indicates which was the ‘fastest finger first’. Get a set of Arcade buttons and make a housing for your game. For advanced hackers, add an indicator of how many notes you’ve remembered, record the best score into EEPROM and trigger a special behaviour when you’ve beaten your own high score.

