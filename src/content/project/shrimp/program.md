# Programming Shrimps: Configuring your computer

<section>
<img src="arduinoweb.png" style="margin:1%;height:200px"/><img src="arduinoide.png" style="margin:1%;height:200px"/><img src="projectsgithub.png" style="margin:1%;height:200px"/>
</section>

The following configuration steps are needed before uploading your first example sketch (program) to a @ShrimpingIt circuit...

* Download our Sketches (example Shrimp programs)
* Install the USB Module
* Install the Arduino IDE
* Select our Sketches and USB Module in the Arduino IDE

Detailed steps are shown below. Once you have completed these steps, you should be able to select and upload our example sketches found under ***shrimpingit*** in the Arduino IDE's Sketchbook menu. 

## Download Our Sketches

Visit the [@ShrimpingIt projects repository](https://github.com/ShrimpingIt/projects) to find a folder containing the programs and libraries for all our @ShrimpingIt projects, intended for the [Arduino IDE](http://www.arduino.cc/en/Main/Software)  version 1.6.3 or above. You should be able to click on the Zip button to download a snapshot of the repository and unpack it to a location of your choice.

## Install Drivers for the CP2102 UART

After installing new drivers, it is a good idea to restart your machine to ensure everything works. Drivers are available for the CP2102 for...

* [Mac OS 10.4 and above](http://shrimping.it/drivers/cp2102/macos/10.4-10.9_newer_untested/Mac_OSX_VCP_Driver.zip)
* [Windows 8](http://shrimping.it/drivers/cp2102/windows/windows-8-silabs/CP210x_VCP_Windows.zip) [Windows XP, Vista, 7](http://shrimping.it/drivers/cp2102/windows/xp-vista-win7-silabs/CP210x_VCP_Win_XP_S2K3_Vista_7.exe)

Linux distributions include built-in CP2102 drivers, although Linux user accounts may need 'dialout' or 'serial' permissions to access the device. 

If your machine is running an old or specialist operating system, then browse [http://shrimping.it/drivers](http://shrimping.it/drivers) or the [Silabs driver page](https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx).

## Install the Arduino IDE

We use an unmodified Arduino IDE to upload programs to the Shrimp. Instructions for installing the Arduino IDE are available for...

* [Linux](http://playground.arduino.cc/Learning/Linux)
* [Mac OS](http://arduino.cc/en/Guide/MacOSX)
* [Windows](http://arduino.cc/en/Guide/Windows)

## Configure our Sketches and Serial Module

Click on *File=>Preferences* in the menu of the Arduino IDE, and select the downloaded 'sketchbook' folder as your Arduino Sketchbook.

A new port should appear in the Arduino IDE under *Tools=>Serial Ports* a short while after you plug in the CP2102, and it should disappear when you remove it. Click on that port to select it. A tick should appear next to the port to indicate that the Arduino IDE will use it for uploading and serial monitoring

A Shrimp is binary- and pin-compatible with an Arduino Uno. Click on 'Arduino Uno' under *Tools=>Boards* in the Arduino IDE. A dot should appear next to 'Arduino Uno' to show the right configuration is selected.

## Choose and Upload a Sketch

To run any of the sketches on your Shrimp you need to find it under *File=>Sketchbook=>shrimpingit* and click on it. Once the code appears in the editor you can click on *File=>Upload* or *CTRL+U* or click the 'Right Arrow' symbol in the top menu bar to send it to your Shrimp.

Eventually it should report 'Done Uploading' **without any red error text** appearing at the bottom. If Red error text is appearing, there's something wrong with the installation of your USB module or you have made an error in your circuit.