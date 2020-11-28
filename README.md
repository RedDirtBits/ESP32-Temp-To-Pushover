# ESP32 Temperature To Pushover

A simple setup to read the temperature in a room then send to Pushover for Android

# Purpose

This is just a simple project to help develop python coding skills and github work flow.

An ESP-WROOM-32 Microcontroller is being used with Micropython to read an external temperature sensor which simply reads room temperature. The result of which is then composed into a message to be used with Pushover notification service for Android. The microcontroller will, based on timing set in `main.py`, periodically connect to the local WiFi network and send a message to Pushover containing the current room temperature and then disconnect from WiFi and wait for the next cycle.

Methods are also being explored to minimize current consumption to experiment with the device being solely run on battery power. Without using _deepsleep_ current consumption is around 50mA at idle (no network). With the WiFi radio on and connected to the local network, consumption can be as high as 120mA. [DigiKey](https://www.digikey.ch/en/resources/conversion-calculators/conversion-calculator-battery-life) has a calculator that can be used to work out what the approximate run time might be.
