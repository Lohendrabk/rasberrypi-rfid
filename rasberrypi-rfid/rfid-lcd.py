import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
import time
import drivers

# initialize the RFID reader
rfid = SimpleMFRC522()

# initialize the LCD display
display = drivers.Lcd()

try:
    while True:
        # scan for rfid tag
        print('scanning for card')
        id, text = rfid.read()

        # clear the lcd display
        display.lcd_clear()

        # display the rfid tag ID on the LCD
        display.lcd_display_string(str(text), 2)
        display.lcd_display_string(str(id), 1)
        time.sleep(2)

except KeyboardInterrupt:
    print('Cleaaing up!')
    gpio.cleanup()
