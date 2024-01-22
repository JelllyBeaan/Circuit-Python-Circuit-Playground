import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
x = 10
i = 0
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2)

while True:  # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
   
    pixels[i]=(255, 0, 0)
    time.sleep(0.5)
    pixels.fill((255, 255, 255))
    time.sleep(0.5)
    if i >= 9 :
        i = -1
        print ("reset")
    i += 1
