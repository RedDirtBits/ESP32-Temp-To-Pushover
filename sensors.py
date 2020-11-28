import machine
import onewire
import ds18x20
import time


def temperature_sensor():

    temp_sense = machine.Pin(12)
    wire = onewire.OneWire(temp_sense)
    sensor = ds18x20.DS18X20(wire)

    sensor_address = sensor.scan().pop()
    sensor.convert_temp()

    time.sleep(1)

    temperature_c = sensor.read_temp(sensor_address)
    temperature_f = (temperature_c * 1.8) + 32

    return temperature_f, temperature_c
