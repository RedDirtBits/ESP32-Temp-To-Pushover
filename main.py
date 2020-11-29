# This is your main script.
import utime
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

utime.sleep(10)

# This deepsleep is for only 10s.  The deepsleep time is in microseconds.  Therefore
# to calculate deepsleep time, multiple the time in seconds you want to wait for the
# next cycle by 1000.  For example, 15 minutes would be 900 seconds.  A 15 minute
# deepsleep would be 900 x 1000 or 90000.

# Deep sleep for 30s
machine.deepsleep(30000)
