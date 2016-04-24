# Examples for the Persistence of Vision (POV) Circuit

The POV programming examples help learners approach the basics of the <a href="https://www.arduino.cc/en/Reference/HomePage" target="_blank">Arduino language</a> which runs on [the Shrimp](../shrimp/index.html), with immediate results visible on their POV circuit.

Alternatively skip straight to the high impact demonstrators to push the limits of your [Persistence of Vision circuit](build.html) and to wow friends and family.

* Arduino language examples
    * [Using ***true and false*** to control 8 lights](#hardcoded)
    * [Storing a pattern in the ***8 bits of a byte***](#stored)
    * [Traversing the byte pattern with a ***while loop***](#while)
    * [Writing a ***function*** to traverse the pattern](#function)

* High-impact demonstrators
    * [Painting a ***smiley face*** in the air](#smiley)
    * [Painting the ***Arduino&trade; logo*** in the air](#logo)
    * [Painting ***your text*** in the air](#text)

# Installing the examples

You can upload the programs described below to your circuit once you have completed the [Programming Shrimps instructions](../shrimp/program.html) to install the relevant software on your laptop. 

Once properly installed, the sketches described appear in the File=>Sketchbook=>shrimpingit=>pov menu. All the examples below run on the same circuit, which you can construct following the [build instructions](./build.html)

<a id="hardcoded" ></a>

## Using ***true and false*** to control 8 lights

To begin, let's control the 8 LEDs to produce a static pattern by running the [Pov01PatternFixed](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov01PatternFixed/Pov01PatternFixed.ino) sketch.

The key part of the code is shown below, which controls eight digital output pins (pins which can be *on* or *off*) by 'writing' a value of <code class="cpp">true</code> or <code class="cpp">false</code>. 
```cpp
//turn on selected LEDs
digitalWrite(9,  true );
digitalWrite(10, false); 
digitalWrite(11, true ); 
digitalWrite(12, false); 
digitalWrite(A1, true ); 
digitalWrite(A2, false); 
digitalWrite(A3, true ); 
digitalWrite(A4, false); 
```
In the default pattern, every *odd* light is illuminated, and every *even* light is extinguished. Try changing some of the true or false values to prove you can turn different lights on and off. 

<a id="stored" ></a>

## Storing a pattern in the ***8 bits of a byte***

The next sketch called  [Pov02PatternStored](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov02PatternStored/Pov02PatternStored.ino) shows how to produce the same pattern, but by reading bits from a byte instead. 


```cpp
byte pattern = 0b10101010;
```

The byte called <code>pattern</code> contains either a *one* or a *zero* in each of its eight positions to determine whether each light is *on* or *off*, (the prefix <code>0b</code> tells us that the byte is written in binary, as a series of *bits*). Try changing the 1s and 0s (a byte has to have exactly eight of them) and uploading to prove you can turn different lights on or off.

Instead of the hard-coded <code>true</code> or <code>false</code> value for each LED in the last sketch, a calculation like <code>pattern & 0b00000001</code> is used to inspect a single bit at a time.

```cpp
//check which 'bits' are set in the byte called 'pattern'
digitalWrite(9,    (pattern & 0b00000001) != 0);
digitalWrite(10,   (pattern & 0b00000010) != 0); 
digitalWrite(11,   (pattern & 0b00000100) != 0); 
digitalWrite(12,   (pattern & 0b00001000) != 0); 
digitalWrite(A1,   (pattern & 0b00010000) != 0); 
digitalWrite(A2,   (pattern & 0b00100000) != 0); 
digitalWrite(A3,   (pattern & 0b01000000) != 0); 
digitalWrite(A4,   (pattern & 0b10000000) != 0); 
```

In the calculation, we are using the [bitwise &](https://www.arduino.cc/en/Reference/BitwiseAnd) operator. It creates a new byte (sequence of eight bits) from two other bytes. 

In this case, it takes the two bytes <code>pattern</code> ***AND*** <code>0b00000001</code>, passing on a <code>1</code> bit only where ***BOTH*** <code>pattern</code> ***AND*** <code>0b00000001</code> have a <code>1</code>. So if ***either*** of them has a <code>0</code>bit in some location, the resulting byte will have a <code>0</code> bit there.

The byte <code>0b00000001</code> has zeroes in *all but one* location, so if <code>pattern</code> has a 0 bit at that spot, the result of the [bitwise &](https://www.arduino.cc/en/Reference/BitwiseAnd) will be <code>0x00000000</code>, (the byte representing the number zero).

The expression <code>!= 0</code> means ["not equal to"](https://www.arduino.cc/en/Reference/If) zero.  The calculation <code>(pattern & 0b00000001) != 0</code> is therefore <code>true</code> ***if and only if*** the first bit of <code>pattern</code> is a 1.

Each bit is examined in turn, the first bit <code>0b00000001</code>, then the second bit <code>0b00000010</code>, then the third bit <code>0b00000100</code> and so on until all eight LEDs have been set to either *on* or *off". 

<a id="while" ></a>

## Traversing the byte pattern with a ***while loop***

In [Pov03PatternWhile](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov03PatternWhile/Pov03PatternWhile.ino), instead of having separate lines of code for every LED, we use a ***while loop***.

The key parts of this code are shown below. To avoid writing the instructions eight times, a single set of instructions is executed eight times with parameters that change each time.

The steps shown run one after the other. However, note the indented steps inside the while loop are repeated ***while*** the bitCounter is ***less than 8***.


```cpp
int pinNumbers[] = { 9,10,11,12,A1,A2,A3,A4 };
```

```cpp
bitCounter = 0;
bitValue = 0b00000001;
while(bitCounter < 8){
    digitalWrite(pinNumbers[bitCounter], (pattern & bitValue) != 0);
    bitValue = bitValue * 2;
    bitCounter = bitCounter + 1;
}
```

A <code>pinNumbers</code> array contains the pin numbers to control. Array values are retrieved using a *subscript* in square brackets, for example <code>pinNumbers[0]</code> gets the first entry, (the stored value *9*), or pinNumbers[7] the eighth and last entry, (the stored value *A4*).

Note, in programming, counting up to eight begins with 0 and finishes with 7!

To begin, the <code>bitCounter</code> is assigned the value zero. We use bitCounter as a *subscript* to retrieve the next pin from the <code>pinNumbers</code> array like <code>pinNumbers[bitCounter]</code>. The LED is turned on or off with the <code>digitalWrite</code> instruction using the same calculation as before, but with a <code>bitValue</code> that changes. After updating the LED <code>bitCounter = bitCounter + 1</code> increases the bitCounter. This ensures a different bit (and a different LED) is processed the next time round. This means the bitCounter will be *0* then *1* then, *2,3,4,5,6,7* before escaping the while loop.

The variable <code>bitValue</code> is initially assigned the value 1. After we have turned on or off the LED, the instruction <code>bitValue = bitValue \* 2</code> multiplies <code>bitValue</code> by two. This means the bitValue will adopt the value 1 then 2 then 4,8,16 and so on. This is equivalent to the binary series *0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000* etc. visible in the [stored pattern example](#stored).

<a id="function" ></a>

## Writing a ***function*** to traverse the pattern

In [Pov04PatternFunction](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov04PatternFunction/Pov04PatternFunction.ino), we remove the duplication in the routine called <code>loop</code>. We put the lighting steps in their own routine, called <code>setLights</code>.

```cpp
void setLights(byte pattern){
  bitCounter = 0;
  bitValue = 1;
  while(bitCounter < totalBits){
    digitalWrite(pinNumbers[bitCounter], (pattern & bitValue) != 0);  
    bitCounter = bitCounter + 1;
    bitValue = bitValue * 2;
  }
}
```

Then in the simplified <code>loop</code> routine, we trigger the <code>setLights</code> steps twice.


```cpp
void loop() {
  setLights(pattern);
  delay(1);
  setLights(empty);
  delay(2);
}
```

<a id="smiley" ></a>

## Painting a ***smiley face*** in the air

Previously we were visiting a sequence of bits, and setting the lights to a given pattern. Now we go 'up a level' by doing the same thing for a ***sequence of patterns***. If we upload [Pov05SequenceSmiley](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov05SequenceSmiley/Pov05SequenceSmiley.ino) and attach a battery pack, then ***waving it in the air should paint a smiley face***.

The key parts of this code are shown below. The byte array called <code class="cpp">patternSequence</code> contains a series of bytes which map to vertical columns making up a smiley face.

```cpp
byte patternSequence[] = {
  0b00111100,
  0b01001110,
  0b11011011,
  0b11011111,
  0b11011111,
  0b11011011,
  0b01001110,
  0b00111100
};
```

If you inspect the 1s and 0s in the byte array, you can see the image below, tipped to the right (each byte is a vertical column, starting from the left side)...

![Smiley Face](http://shrimping.it/blog/wp-content/uploads/2012/11/smilie_binary-250x300.png)

<a id="logo" ></a>

## Painting the ***Arduino&trade; logo*** in the air

Just for fun, we do the same thing with a different pattern - [the Arduino Logo](https://upload.wikimedia.org/wikipedia/commons/8/87/Arduino_Logo.svg) with our sketch [Pov06SequenceArduino](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov06SequenceArduino/Pov06SequenceArduino.ino). Of course this is best done with Blue LEDs!

```cpp
byte patternSequence[] = {
  0b00111000,
  0b01000100,
  0b10010010,
  0b10010010,
  0b10010010,
  0b01000100,
  0b00101000,
  0b00010000,
  0b00101000,
  0b01000100,
  0b10010010,
  0b10111010,
  0b10010010,
  0b01000100,
  0b00111000
};
```

This sketch should cause the image below to be painted in the air...

![Arduino Logo](./photos/arduino_logo_480.png)

<a id="text" ></a>

## Painting ***your text*** in the air

Our last demonstration sketch is the best.  [Pov07PaintText](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov07PaintText/Pov07PaintText.ino) incorporates the 8-bit font from a Commodore 64 into an Arduino sketch, so learners can paint their choice of text in the air. 

In our example code, we have replaced the original font's $ symbol with the smiley face sequence, showing how to combine your own icons with text messages.

```cpp
String message ="HACK $";
```

Try looking for the above fragment of code (try CTRL+F to find the word 'message'). 

Then change HACK to show the text you prefer. Be careful to keep the keyword <code>String</code>, the <code>=</code> symbol, quote marks and semi-colon in place otherwise a compiler error will be reported. 

If you get really stuck after making code changes, try mashing CTRL+Z (undo) or just delete everything and copy paste the [original code](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/pov/Pov07PaintText/Pov07PaintText.ino) back in place.


![Illusion effect](./show.jpg)

# Exploring our examples

All the code examples for the [POV circuit](build.html) can be browsed on the web at [https://github.com/ShrimpingIt/projects/tree/master/sketchbook/shrimpingit/pov](https://github.com/ShrimpingIt/projects/tree/master/sketchbook/shrimpingit/pov)

If you want to install our sketches to upload them to your own [@ShrimpingIt kits](../../index.html#kit), follow [these instructions](http://start.shrimping.it/project/shrimp/program.html) to configure your computer.

# Future developments

Why not add a tilt-switch to 'reverse the polarity' so the circuit can tell whether it is moving from left-to-right or from right-to-left?

Attach a [soldered version](../../kit/stripboard.html) of the circuit securely to a bicycle wheel or wind turbine, or as a [Dance Messenger](http://www.instructables.com/id/Dance-Messenger/) attached to your shoe to paint text as you move.