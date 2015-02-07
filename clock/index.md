Real Time Clock
===============

# Overview

This project gives learners a starting point for learners inventing their own clock project.

It employs a Real Time Clock chip which incorporates a precise quartz-controlled time signal, as well as a battery-backup system, so that the time doesn't need to be reset every time the clock is unplugged.

The default time display relies on a set of 24 LEDs organised in two lines of 12, intended to be continually illuminated by a permanent power supply (not a battery). 

These LEDs are employed in two distinct regimes to present the time of day as...

* a proportional display
    - a row with one lit LED for every hour 
    - another row with one lit LED for every 5 minutes.
    - examples `*_*_*_*_*_*_` is 6 hours, `**___*___**_` is 5 hours
    - examples `*_*_*_*_*_*_` is 30 minutes, `**___*___**_` is 25 minutes


* a word clock display
    - leds are placed behind paper lightboxes with words printed 
    - words are selectively illuminated to present the time in English
    - examples; "It's five minutes to ten", "It's a quarter past three"

# Learning Points

This project shows how to use peripheral Integrated Circuits (ICs) as part of a @ShrimpingIt layout, and demonstrates a number of distinct digital communication protocols. It provides a natural foundation for D&T activities around developing time display mechanisms or product housings. It also provides a jumping off point for programming activities focused on different LED lighting behaviours for time display such as altering which lights are visible for easy identification of the hour, creating a word clock with different logic (e.g. translated from english to french), different tunes played on the hour, menu interactions to set the time or alarms.

All @ShrimpingIt projects use the Arduino-compatible ATMEGA328 chip as the controller of the digital device. The two extra ICs wired into this project demonstrated how other specialist external chips can communicate back and forth to perform their part.

The following chips are used.

* *ATMEGA328P-PU*
	- Performs the role of 'brain' controlling the device 
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

