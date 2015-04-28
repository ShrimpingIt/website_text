<section>
<img src="arduinoweb.png" style="margin:1%;height:200px"/><img src="arduinoide.png" style="margin:1%;height:200px"/><img src="projectsgithub.png" style="margin:1%;height:200px"/>
</section>

To upload code to a Shrimp you must complete the following steps, described in more detail below...

* Install the latest Arduino IDE from [arduino.cc](http://www.arduino.cc/en/main/Software)
* Install drivers for the UART module from [shrimping.it](http://shrimping.it/drivers/) (not needed on Linux)
* Install our [example 'Sketches'](https://github.com/ShrimpingIt/projects) (programs) in your Arduino IDE 'sketchbook' folder 

## Installing the Arduino IDE

We use an unmodified Arduino IDE to upload programs to the Shrimp (it thinks it's an Arduino Uno).

Instructions for installing the Arduino IDE are available for 

* [Linux](http://playground.arduino.cc/Learning/Linux)
* [Mac](http://arduino.cc/en/Guide/MacOSX)
* [Windows](http://arduino.cc/en/Guide/Windows)

## Installing Drivers for the CP2102 UART

Drivers are available for the CP2102 for

* [Mac](http://arduino.cc/en/Guide/MacOSX)
* [Windows](http://arduino.cc/en/Guide/Windows)

...and they are built in to the kernel on all mainstream Linux distributions. 

If your machine is running an unusual OS (old or specialist), then browse [http://shrimping.it/drivers](http://shrimping.it/drivers) or the [Silabs driver page](https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx). If you're running a Linux kernel which doesn't include the CP210x drivers, you're enough of a hacker to solve this problem yourself :)

## Installing Example Sketches

Visit the [@ShrimpingIt projects repository](https://github.com/ShrimpingIt/projects) to find a folder containing the programs and libraries for all our @ShrimpingIt projects for use with the [Arduino IDE](http://www.arduino.cc/en/Main/Software)  version 1.6.3 or above.

Download and unzip the repository and configure your computer by navigating to *File=>Preferences* in the menu of the Arduino IDE, selecting the downloaded 'sketchbook' folder as your Arduino Sketchbook.

To run each of the programs on your Shrimp you need to open it from its location under *File=>Sketchbook=>shrimpingit*, then click on *File=>Upload* or *CTRL+U* or click the 'Right Arrow' symbol in the top menu bar.

Eventually it should report 'Done Uploading' **without any red error text** appearing at the bottom. If Red error text is appearing, there's something wrong with your circuit or the configuration of your USB module.

