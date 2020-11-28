# This is script that run when device boot up or wake from sleep.

import esp
import network
import time
import env

from machine import Pin

esp.osdebug(None)

led_green = Pin(4, Pin.OUT)
led_red = Pin(14, Pin.OUT)

led_green.value(0)
led_red.value(0)


class NetworkConnection:

    wlan = network.WLAN(network.STA_IF)

    def wifi_connect(self):

        count = 3

        print('Attempting to connect to WiFi...')

        while not self.wlan.isconnected() and count > 0:

            led_red.value(1)

            self.wlan.active(True)
            # self.wlan.connect('ArticleTwo', 'totalsunlightsilentnoise')
            self.wlan.connect(
                env.credentials['ssid'], env.credentials['wifi_passwd'])
            time.sleep(3)
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

        self.wlan.disconnect()
        self.wlan.active(False)

        led_green.value(0)
        led_red.value(1)

        print('Disconnected from WiFi...')

        return self.wlan.isconnected()

    def connection_status(self):

        network_conn = self.wlan.isconnected()
        return network_conn
