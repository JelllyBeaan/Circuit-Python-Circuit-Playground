import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
x = 10
i = 0
colorsfill = [230,200,20,30,160,255,140,70,90,220]
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2)

while True:  # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
   
    pixels[i]=(0, 255, 0)
    pixels[i+1]= (200, 0, 200)
    time.sleep(0.5)
    pixels.fill((colorsfill[i], 200, 200))
    time.sleep(0.5)
    if i >= 8 :
        i = -1
        print ("reset")
    i += 1
    
