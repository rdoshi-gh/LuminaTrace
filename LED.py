#test
from gpiozero import LED, DigitalInputDevice
import time

input_pin = DigitalInputDevice(23)  # GPIO pin 17 (change as needed)


class Led:
    def __init__(self, r, g, t, l):
        self.red = r
        self.green = g
        self.time = t
        self.location = l
    def getRed(self):
        return self.red
    def getGreen(self):
        return self.green
    def getTime(self):
        return self.time
    def getLocation(self):
        return self.location

def testLED(color):
    isWorking = False
    color.on()
    time.sleep(2)
    for i in range(3):
        ## 1 input is low. 0 input is high
        if input_pin.is_active:
            #Time between each sensor data collection
            time.sleep(0.5)
        else:
            isWorking = True
            break
    color.off()
    #time between each LED color test
    time.sleep(3)

    return isWorking
    
    

green = LED(17)
red = LED(27)

LEDStrip = []
brokenCounter = 0
start_time = 0

numLED = int(input("How many LEDs will we be detecting? Enter integer values only: "))
start = input("When sensor is above the first LED, type Y for scan: ")

locationLED = 0


if(start == "Y"):
    #give Juan time to setup sensor
    time.sleep(6)
    start_time = time.time()
    while numLED > 0:
        greenWorking = testLED(green)
        print(f'Green: {greenWorking}')
        redWorking = testLED(red)
        print(f'Red: {redWorking}\n')

        if not greenWorking or not redWorking:
            brokenCounter += 1

        end_time = time.time()
        delta_time = end_time - start_time

        l = Led(redWorking, greenWorking, delta_time, locationLED)
        LEDStrip.append(l)
    
        numLED -= 1
        locationLED += 1

        #time.sleep(6)

counter = 1
for led in LEDStrip:
    print(f'LED {counter} -->\nRed: {led.getRed()}\nGreen: {led.getGreen()}\nTime detected: {led.getTime():.3f}\nLocation on strip: {led.getLocation()}\n\n\n')
    counter += 1

print(f"Total broken LEDs: {brokenCounter}")