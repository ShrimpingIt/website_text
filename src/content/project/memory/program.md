# Programming the Memory Game

The Memory Game is provided with two example behaviours to get you started. 

## Basic Circuit Testing

Once you have [configured your computer](../shrimp/program.html) for uploading @ShrimpingIt sketches, you can get started with the [Memory01BabyGame](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/memory/Memory01BabyGame/Memory01BabyGame.ino) sketch you will find under *File=>Sketchbook=>shrimpingit=>memory=>Memory01BabyGame*.

This is a simple behaviour which was designed for a toddler to play with, where a single light is illuminated at a time. 

Pushing the glowing button triggers a noise, then switches on a different light.

## Melody Game

Next, try loading the demonstration memory game behaviour at 
[Memory02MelodyGame](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/memory/Memory02MelodyGame/Memory02MelodyGame.ino) sketch you will find under *File=>Sketchbook=>shrimpingit=>memory=>Memory02MelodyGame*.

This plays a sequence of lights (with the accompanying notes), challenging you to respond, playing back the same melody sequence on the backlit buttons. Every time you complete the sequence correctly, it plays a slightly longer melody until your brain can't stand it!

## Further Development

Why not try to change the code by Googling for other [rtttl](http://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language) tunes which are more personal to you and putting them into your game. 

You could change the game behaviour altogether, making it into a quiz buzzer which indicates which was the ‘fastest finger first’. 

To pimp your game, get a set of Arcade buttons and embed them in a laser-cut housing.

For advanced hackers, add an indicator of how many notes you’ve remembered, record the best score into EEPROM and trigger a special behaviour when you’ve beaten your own high score!