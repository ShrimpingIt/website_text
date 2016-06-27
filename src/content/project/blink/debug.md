# Debugging Blink

## Wiring

First, check that the circuit is exactly as shown in the <a href="build.html#step11" target="blank">last frame of the Blink build</a>. Click on the image shown if you need it to be bigger to read the numbers and follow the wires.

Some learners do not follow the [step-by-step instructions](./build.html) at all, (they just look at the diagram). They will miss out on important features which are less-obvious in the diagram. 

Other learners skip the detail of the steps (in particular the bold text of each step cannot be overlooked).

In the most extreme case, learners ignore all of the wiring in favour of shoving components into the board at random. This will not work.

It is worth touring a workshop to sanity-check the position of the first few components to guide learners that it matters which row a component is inserted into, in case they were daydreaming through [meet your breadboard](http://start.shrimping.it/project/blink/build.html#step2).

### Common Errors

The following wiring errors will cause the Upload step to fail with 'not responding', just as if no Shrimp was attached at all...

* Chip is upside down (see [inserting the chip](http://start.shrimping.it/project/blink/build.html#step3))
* Chip wasn't pushed down flush and is not connected to be breadboard (see [inserting the chip](http://start.shrimping.it/project/blink/build.html#step3))
* The wrongly colored resistor is inserted as a pull-up (see [adding the pull-up resistor](http://start.shrimping.it/project/blink/build.html#step5) and [adding the current-limiting resistor](http://start.shrimping.it/project/blink/build.html#step10))
* The wrongly numbered 'reset' capacitor is inserted (see [adding the reset capacitor](http://start.shrimping.it/project/blink/build.html#step11))
* The UART is wired without attaching the correctly labelled pins to the correct pins (see [wiring the UART](http://start.shrimping.it/project/blink/build.html#step11))
* Any variation from the <a href="build.html#step11" target="blank">last frame of the Blink build</a> could prevent the circuit from working, so check again.

If upload works, and the LED still doesn't blink...

* The LED is in backwards (see [adding the LED](http://start.shrimping.it/project/blink/build.html#step9))

On the plus-side, every circuit we have debugged comes back to life when it is wired properly. The components are very robust. One exception is wiring an LED directly to the battery or USB power wires. That will blow them up, but LEDs are cheap!

## Programming

#### Debugging the programming sequence

A Shrimp (or any Arduino-Uno-compatible circuit) is re-programmed as follows...

* **The Shrimp's reset pin is set to 0V, then back to 5V, rebooting the chip** 
	- the USB module's Brown Wire (DTR) sends a 0V pulse through a capacitor to *chip pin 1*
	- when the 0V signal ends, the 10k pull-up resistor restores *chip pin 1* to 5V
* **The chip monitors the 'Serial' connection to receive and acknowledge a new program** 
	- the USB module appears as a 'Serial Port' on your laptop. On the Shrimp chip, *pin 2* receives data, and *pin 3* sends data back
* **If the Shrimp receives...** 
	- **...a new program**, it
        - acknowledges using the Serial link
        - stores the program
        - it runs the program
	- **...no new program**, it
		- runs the previously stored program

##### Types of failure

This programming sequence can fail in a number of ways. 

* a) Example error: ***Serial port [SOMETHING] not found. Did you select the right one from the Tools => Serial Port menu***. In this case, the Serial Port location ticked under *Tools => Serial Ports* does not select the correct USB module
	- Check which Serial Port disappears and reappears in the *Tools => Serial Ports* menu when you unplug and replug the USB module in your laptop, (close and reopen the *Tools=>Serial Ports* menu to refresh it after each step).
	- The USB module is not plugged in to the laptop (this happens more often than you'd think)

* b) The laptop seems to be talking to some USB module, but it isn't the right one (especially on Mac which has lots of spurious Serial devices)
	- see the troubleshooting steps for a) above. If two new ports appear, try each one in turn