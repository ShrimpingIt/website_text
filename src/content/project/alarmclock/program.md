# Example Sketches

Visit the [@ShrimpingIt projects repository](https://github.com/ShrimpingIt/projects) to find a sketchbook containing the programs and libraries for all our @ShrimpingIt projects for use with the [Arduino IDE](http://www.arduino.cc/en/Main/Software)  version 1.6.3 or above. Download the repository and visit File=>Preferences to point the IDE to the downloaded 'sketchbook' folder. 

Once you have configured the projects sketchbook, you can get started by uploading the [Clock01HardcodeTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock01HardcodeTime/Clock01HardcodeTime.ino) sketch under File=>Sketchbook=>shrimpingit=>alarmclock=>Clock01HardcodeTime. This sketch is deliberately very simple, and shows how a time (hard coded into the sketch) can be written to the RealTimeClock to prove that it's working.

Next, upload the [Clock02SetTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock02SetTime/Clock02SetTime.ino) sketch under File=>Sketchbook=>shrimpingit=>alarmclock=>Clock02SetTime. This sketch demonstrates how to handle Serial input to set the time interactively. To set the time, launch the Serial Monitor using Tools=>Serial Monitor, or the keyboard shortcut *Ctrl+Shift+M* Choose **Newline** and a speed of **9600 baud** (bits per second) from the dropdown menus. You should then be able to send commands like any of the following...

    19:45  
    2007-04-25
    2007-04-25T19:45:00

Which should respond to show that the time has been reset.

The [Clock03LowPowerSetTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock03LowPowerSetTime/Clock03LowPowerSetTime.ino) sketch is at File=>Sketchbook=>shrimpingit=>alarmclock=>Clock03LowPowerSetTime and offers an example where the ATmega chip is put into an incredibly low power mode between events. It therefore offers a foundation for clock-based behaviours which run from battery for more than a year.

Finally the [Clock04Alarm](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock04Alarm/Clock04Alarm.ino) sketch at File=>Sketchbook=>shrimpingit=>alarmclock=>Clock04Alarm builds on the LowPower sketch to add behaviour which drives the Piezo transducer to play melodies at set times. This is a good foundation for a project which uses special dates and time logic to trigger alerts. For example, why not wake yourself with 'Happy Birthday' on just one day of the year!