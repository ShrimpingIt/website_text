Could create an educational circuit where there is no Shrimp at all, but just three buttons, one for clock, one for data, one for latch, and could manually tick through the Shift Register, getting feedback of your comprehension of the system.

The default time display relies on a set of 24 LEDs organised in two lines of 12, a display which is quite power-hungry, and therefore intended to be continually illuminated by a permanent power supply (not a battery).

These LEDs are employed in two distinct regimes to present the time of day as...

* a word clock display
 - leds are placed behind printed words
 - words are selectively illuminated to present the time in English
 - examples; "It's five minutes to ten", "It's a quarter past three"

* a proportional display
 - a row with one lit LED for every hour 
   - examples `* * * * * * ` is 6 hours, `**   *   ** ` is 5 hours
 - another row with one lit LED for every 5 minutes.
   - examples `* * * * * * ` is 30 minutes, `**   *   ** ` is 25 minutes

The build provides a jumping off point for programming activities focused on different LED lighting behaviours for time display such as altering which lights are visible for easy identification of the hour, creating a word clock with different logic (e.g. translated from english to french), different tunes played on the hour, menu interactions to set the time or alarms. It also provides a natural foundation for D&T activities around developing time display mechanisms or product housings. 

All @ShrimpingIt projects use the Arduino-compatible ATMEGA328 chip as the controller of the digital device. The two extra ICs wired into this project demonstrated how other specialist external chips can communicate back and forth to perform their part.

The following chips are used.

* *ATMEGA328P-PU*
	- Performs the role of the 'brain' controlling the device 
	- an Arduino-compatible microcontroller
	- Used in all the @ShrimpingIt projects
	- **receives initial time setting from a laptop (via Serial UART communication)**
* *Real Time Clock Chip*
	- performs the role of pendulum - the tick in the clock
	- precisely regulated Quartz clock maintains accurate time signal
	- battery backup subcircuit allows time to be retained even when unplugged
	- **sends timestamps and receives them from the ATMEGA328 (via I2C communication)**
* *LED driver chip*
	- can light a large number of LEDs (more than the ATMEGA)
	- can handle high-powered LEDs (more than the ATMEGA)
	- regulates the current to each LED (eliminating the need for resistors)
	- described as a 'Shift Register'
	- **receives LED on and off commands from the ATMEGA (a clocked signal)**


