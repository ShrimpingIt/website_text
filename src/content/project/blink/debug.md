# Debugging Blink

First, check that the circuit is exactly as shown in the <a href="build.html#step11" target="blank">last frame of the Blink build</a>. Click on the image shown if you need it to be bigger to read the numbers and follow the wires.

## Problems programming


#### The programming sequence

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

* b) The laptop seems to be talking to a USB module, but it isn't the right one
	- see the troubleshooting steps for a) above. If more than one new ports appear, try each one in turn

*   but there is something wrong in the serial circuit, for example...
    - send and receive wires are swapped or not attached
    - 100nF Reset Capacitor or 10kOhm pull-up resistor are missing or miswired
    - 
* 
	- You

