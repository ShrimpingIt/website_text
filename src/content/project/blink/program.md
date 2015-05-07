# Programming Blink

Uploading and running <a href="http://www.arduino.cc/en/Tutorial/Blink" target="_blank">Blink</a> on the circuit you have built will verify that all the parts on the board are working and connected correctly. Blink turns on an LED on for one second, then off for one second, and repeats forever.

You may see the LED flash once or twice as the circuit is powered up, and each time the serial connection is reset by the IDE when reprogramming the Shrimp. This is normal. However, if you successfully upload the Blink behaviour, you should see a distinctive, periodic flashing which never stops.

Below is the code in the Blink sketch (the comments after **//** on each line are intended for learners and ignored by the machine). It's a good idea to try changing the delay value from 1000 milliseconds to some other number, making Blink flash faster and slower to prove that the upload of your edited code has succeeded.

```
int led = 13; //store 13 under the name 'led'

void setup() {
  pinMode(led, OUTPUT); // initialize digital pin 13 as an output.
}

void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

The Blink sketch is written in C, but it is compiled to bytes of machine code by Arduino's integrated development environment (IDE), which are sent over the serial UART to the ATmega chip. The chip will store the program and run it when rebooted (the ATmega reboot happens automatically during upload).


Once you have completed the wiring steps in the [Blink build](build.html), you should follow [the configuration guide](../shrimp/program.html) to set up your computer for Shrimp development. It will guide you through installing the Arduino IDE, the drivers for the CP2102 UART and getting the @ShrimpingIt example sketches for our projects (Arduino programs are called sketches).