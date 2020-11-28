# ESP32 Temperature To Pushover

A simple setup to read the temperature in a room then send to Pushover for Android

# Purpose

This is just a simple project to help develop python coding skills and github work flow.

An ESP-WROOM-32 Microcontroller is being used with Micropython to read an external temperature sensor which simply reads room temperature. The result of which is then composed into a message to be used with Pushover notification service for Android. The microcontroller will, based on timing set in `main.py`, periodically connect to the local WiFi network and send a message to Pushover containing the current room temperature and then disconnect from WiFi and wait for the next cycle.

Methods are also being explored to minimize current consumption to experiment with the device being solely run on battery power. Without using _deepsleep_ current consumption is around 50mA at idle (no network). With the WiFi radio on and connected to the local network, consumption can be as high as 120mA. [DigiKey](https://www.digikey.ch/en/resources/conversion-calculators/conversion-calculator-battery-life) has a calculator that can be used to work out what the approximate run time might be.

I hope, to someday, look back on this little project and its associated code and laugh at how terrible it was, but so much fun learning and experimenting. It is also my hope that if you should read this and have any suggestions that you would reach out to me and pass them along.

I am _comfortable_ writing this code as opposed to when I first started studying Python and was completely _deer in the headlights_ at trying to learn without seeming like a complete bafoon. I might still be that, but I have at least learned a thing or two, but much, so much more to learn yet enjoying the journey of it all.
