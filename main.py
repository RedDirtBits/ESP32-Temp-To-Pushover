# This is your main script.
import time
import push_notify
import sensors
import machine

from boot import NetworkConnection

# Connect to WiFi
NetworkConnection().wifi_connect()

# Get temperature from sensor and send results as message to Pushover
push_notify.push_notification('Current Office Temperature: {}F / {}C.'.format(
    sensors.temperature_sensor()[0], sensors.temperature_sensor()[1]))

# Disconnect from WiFi
NetworkConnection().wifi_disconnect()

# Start a simple sleep cycle to provide time to reset or upload/update
# code while in development
# time.sleep(10)

# machine.deepsleep(10000)
