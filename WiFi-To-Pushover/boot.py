# This is script that run when device boot up or wake from sleep.

import esp
import network
import utime
import env

from machine import Pin

# Turn off debugging
esp.osdebug(None)

# Set up the LED's.
# THIS IS FOR DEV ONLY.  REMOVE WHEN FINALIZED
led_green = Pin(4, Pin.OUT)
led_red = Pin(14, Pin.OUT)

led_green.value(0)
led_red.value(0)


class NetworkConnection:

    """
     Class for establishing the WiFi network connection
    """

    wlan = network.WLAN(network.STA_IF)

    def wifi_connect(self):
        """
         Connects to WiFi.  Will attempt three times to connect.  Uses the LEDs for visual
         indication of network connection status.  RED when disconnected, GREEN when connected.
        """

        count = 3

        print('Attempting to connect to WiFi...')

        while not self.wlan.isconnected() and count > 0:

            led_red.value(1)

            self.wlan.active(True)
            self.wlan.connect(
                env.credentials['ssid'], env.credentials['wifi_passwd'])
            utime.sleep(3)
            count -= 1

        if self.wlan.isconnected():

            led_green.value(1)
            led_red.value(0)

            print('Successfully Connected to Wifi. IP Address: {}'.format(
                self.wlan.ifconfig()[0]))

        else:

            led_green.value(0)
            led_red.value(1)

            print('Unable to connect to Wifi')

    def wifi_disconnect(self):
        """
         Function to disconnect from WiFi
        """

        self.wlan.disconnect()
        self.wlan.active(False)

        led_green.value(0)
        led_red.value(1)

        print('Disconnected from WiFi...')

        return self.wlan.isconnected()

    def connection_status(self):
        """
         Function to get network connection status

        Returns:
            Bool: True for connected, False otherwise
        """

        network_conn = self.wlan.isconnected()
        return network_conn
