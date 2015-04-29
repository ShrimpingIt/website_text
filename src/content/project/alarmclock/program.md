# Example Sketches

You will be able to upload the programs described below to your [Alarm Clock](index.html) once you have completed [these instructions](../shrimp/program.html) to install the relevant software on your laptop.

## Prove Clock Chip is properly configured 

Once you have configured the projects sketchbook, you can get started with the [Clock01HardcodeTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock01HardcodeTime/Clock01HardcodeTime.ino) sketch under *File=>Sketchbook=>shrimpingit=>alarmclock=>Clock01HardcodeTime*. This sketch is deliberately very simple, and shows how a time (hard coded into the sketch) can be written to the RealTimeClock to prove that it's working.

However, this program will always set the same hard-coded time, so you need to...

## Upload a program to set the time interactively 

Next, load the [Clock02SetTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock02SetTime/Clock02SetTime.ino) sketch under *File=>Sketchbook=>shrimpingit=>alarmclock=>Clock02SetTime*. This sketch demonstrates how to send and receive text commands over the [Serial](../../topic/serial.html) interface, to set the time interactively. After uploading, launch the Serial Monitor using *Tools=>Serial Monitor*, or the keyboard shortcut *Ctrl+Shift+M*.

Choose **Newline** and a speed of **9600 baud** (bits per second) from the dropdown menus. You should then be able to send commands like any of the following...

    19:45  
    2007-04-25
    2007-04-25T19:45:00

Which should send back the new time, showing that the RealTime Clock chip has been set according to your command.

## Use the ATmega chip's Power-saving features

The [Clock03LowPowerSetTime](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock03LowPowerSetTime/Clock03LowPowerSetTime.ino) sketch is at *File=>Sketchbook=>shrimpingit=>alarmclock=>Clock03LowPowerSetTime* and offers an example where the ATmega chip is put into an incredibly low power mode between events. It therefore offers a foundation for clock-based behaviours which run from battery for more than a year.

## Upload an 'Alarm Clock' behaviour

Finally the [Clock04Alarm](https://github.com/ShrimpingIt/projects/blob/master/sketchbook/shrimpingit/alarmclock/Clock04Alarm/Clock04Alarm.ino) sketch at *File=>Sketchbook=>shrimpingit=>alarmclock=>Clock04Alarm* builds on the LowPower sketch to add behaviour which drives the Piezo transducer to play melodies at set times. 

Take a look at the code to find the ```int alarmHour``` and ```int alarmMinute``` values. Then set the clock time to match. You should immediately hear the melody of 'Wake me up before you go,go' by Wham. After proving that it works, you can use it as your alarm clock.

This is a good foundation for a project which uses special dates and time logic to trigger alerts. Currently the alarm goes off for a minute each day, but you could change the logic for your preference, for example adding a snooze behaviour which detects a button push, or setting yourself a puzzle you have to solve. You could wake yourself with 'Happy Birthday' on just one day of the year, or Jingle Bells in the advent up to Christmas!

## Related @ShrimpingIt Projects

If you're interested in clock designs, you might like the [LED Clock](../ledclock/) or [LCD Clock](../lcdclock/) projects, which build on the Alarmclock project, and add a time display.