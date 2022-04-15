#SmartWatchOS 40.8
#TIME
Day = 1
Hours = 12
Minutes = 0
Seconds = 0
#APP
ThermometerT = 0
CompassStill = 0
CompassDATA = 0
SecondsT = 0
Wall = 0
#SYSTEM
Brightness = 255
BrightnessSAVING = 20
AODDATA = 5
AODSAVING = 0
AOD = 5
AODNOSAVING = 0
Volume = 105
Start()
def OS():
    Limiter()
    Buttons()
    Application()
basic.forever(OS)
def TimeEngine():
    def onIn_background():
        global Day
    global Hours
    global Minutes
    global Seconds
    if Seconds >= 60:
        global Seconds
        global Minutes
        Seconds += -60
        Minutes += +1
        AODON()
    if Minutes >= 60:
        global Minutes
        global Hours
        Minutes = 2
        Hours += +1
    if Hours >= 24:
        global Hours
        global Day
        Day += +1
        Hours = 0
    global Seconds
    Seconds += +1
    pause(1000)
    control.in_background(onIn_background)
basic.forever(TimeEngine)
def Application():
    if Wall == 0:
        AODButtons()
        Watch()
    elif Wall == -1:
        DigitalWatch()
    elif Wall == 1:
        Calendar()
    elif Wall == 2:
        SETBrightness()
    elif Wall == 3:
        SETVolume()
    elif Wall == 4:
        Battary_saving()
    elif Wall == 5:
        flash()
        Buttons_LOCK()
    elif Wall == 6:
        Compass()
    elif Wall == 7:
        Thermometer()
    elif Wall == 8:
        AODOFF()
        Watch_settings()
    elif Wall == 9:
        SecondsTT()
def Battary_saving():
    Driver()
    global BrightnessSAVING
    global AODSAVING
    global Brightness
    global AODDATA
    global AODNOSAVING
    basic.show_leds("""
    . . # . . 
    . # . # . 
    . # . # . 
    . # . # . 
    . # # # . 
    """)
    if input.pin_is_pressed(TouchPin.P2):
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        Brightness = BrightnessSAVING
        AOD = AODSAVING
        music.stop_all_sounds()
        pause(200)
    elif input.pin_is_pressed(TouchPin.P1):
        music.ring_tone(Note.C5)
        pause(70)
        Brightness = 255
        AOD = AODNOSAVING
        music.stop_all_sounds()
        pause(200)
def Thermometer():
    global ThermometerT
    ThermometerT = input.temperature()
    basic.show_leds("""
    # . . . .
    # . . . .
    # # # # .
    # . . . .
    . # # # .
    """)
    if input.pin_is_pressed(TouchPin.P2):
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        basic.show_number(ThermometerT)
        pause(200)
    elif input.pin_is_pressed(TouchPin.P1):
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        pause(200)
def Compass():
    global CompassDATA
    global CompassStill
    CompassDATA = input.compass_heading()
    if input.pin_is_pressed(TouchPin.P1):
        global CompassStill
        CompassStill += -1
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        pause(100)
    elif input.pin_is_pressed(TouchPin.P2):
        global CompassStill
        CompassStill += +1
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        pause(100)
    if CompassStill == 0:
        CompassStandart()
    elif CompassStill == 1:
        CompassLetters()
    elif CompassStill == 2:
        CompassDegrees()
def CompassDegrees():
    basic.show_number(CompassDATA)
def CompassLetters():
    if CompassDATA < 22:
        basic.show_string("N")
    elif CompassDATA < 112:
        basic.show_string("E")
    elif CompassDATA < 202:
        basic.show_string("S")
    elif CompassDATA < 292:
        basic.show_string("W")
def CompassStandart():
    Driver()
    global CompassDATA
    if CompassDATA < 22:
        basic.show_arrow(ArrowNames.NORTH)
    elif CompassDATA < 68:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    elif CompassDATA < 112:
        basic.show_arrow(ArrowNames.WEST)
    elif CompassDATA < 157:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif CompassDATA < 202:
        basic.show_arrow(ArrowNames.SOUTH)
    elif CompassDATA < 247:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif CompassDATA < 292:
        basic.show_arrow(ArrowNames.EAST)
    elif CompassDATA < 337:
        basic.show_arrow(ArrowNames.NORTH_EAST)
def AODON():
    global AODDATA
    global AOD
    AODDATA = AOD
def AODOFF():
    global AODDATA
    global Brightness
    AODDATA = Brightness
def AODButtons():
    global AODDATA
    global AOD
    global Brightness
    if input.pin_is_pressed(TouchPin.P1):
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        AODOFF()
    elif input.pin_is_pressed(TouchPin.P2):
        music.ring_tone(Note.C5)
        pause(70)
        music.stop_all_sounds()
        AODOFF()
def Watch_settings():
    Watch()
    pause(200)
    basic.clear_screen()
    pause(100)
    if input.pin_is_pressed(TouchPin.P1):
        global Hours
        global Seconds
        Hours += +1
        Seconds = 0
        music.play_tone(Note.A,100)
    elif input.pin_is_pressed(TouchPin.P2):
        global Minutes
        global Seconds
        Minutes += +1
        Seconds = 0
        music.play_tone(Note.B,100)
def SETVolume():
    Driver()
    if Volume >= 204:
        basic.show_leds("""
        . # . # .
        # . . . #
        # . . . #
        . # . # .
        # # # # #
        """)
    elif Volume >= 153:
        basic.show_leds("""
        . # . # .
        # . . . #
        # . . . #
        . # . # .
        # # # # .
        """)
    elif Volume >= 102:
        basic.show_leds("""
        . # . # .
        # . . . #
        # . . . #
        . # . # .
        # # # . .
        """)
    elif Volume >= 51:
        basic.show_leds("""
        . # . # .
        # . . . #
        # . . . #
        . # . # .
        # # . . .
        """)
    elif Volume <= 50:
        basic.show_leds("""
        . # . # .
        # . . . #
        # . . . #
        . # . # .
        # . . . .
        """)
    elif Volume <= 1:
        basic.show_leds("""
        # # . # .
        # # . . #
        # . # . #
        . # . # .
        . . . . .
        """)
    if input.pin_is_pressed(TouchPin.P1):
        global Volume
        Volume += -30
        music.play_tone(Note.A,50)
    if input.pin_is_pressed(TouchPin.P2):
        global Volume
        Volume += +30
        music.play_tone(Note.B,50)
def flash():
    led.set_brightness(255)
    basic.show_leds("""
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    """)
def SecondsTT():
    Driver()
    global SecondsT
    basic.pause(1000)
    SecondsT += 1
    if SecondsT % 2 == 0:
        led.plot(0, 0)
        led.plot(4, 0)
        led.plot(4, 4)
        led.plot(0, 4)
    else:
        basic.clear_screen()
        basic.show_number(SecondsT)
        basic.clear_screen()
    if input.pin_is_pressed(TouchPin.P2):
        music.play_tone(Note.A,100)
        SecondsT = 0
    if input.pin_is_pressed(TouchPin.P1):
        music.play_tone(Note.A,100)
        music.play_tone(Note.C5,100)
        music.play_tone(Note.E,100)
def SETBrightness():
    Driver()
    if Brightness >= 204:
        basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . . . . .
        # # # # #
        """)
    elif Brightness >= 153:
        basic.show_leds("""
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        # # # # .
        """)
    elif Brightness >= 102:
        basic.show_leds("""
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        # # # . .
        """)
    elif Brightness >= 51:
        basic.show_leds("""
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        # # . . .
        """)
    elif Brightness <= 50:
        basic.show_leds("""
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        # . . . .
        """)
    if input.pin_is_pressed(TouchPin.P1):
        global Brightness
        Brightness += -30
        music.play_tone(Note.A,70)
    if input.pin_is_pressed(TouchPin.P2):
        global Brightness
        Brightness += +30
        music.play_tone(Note.B,70)
def Calendar():
    Driver()
    global Day
    global Brightness
    led.set_brightness(Brightness)
    if input.pin_is_pressed(TouchPin.P1):
        global Day
        Day += -1
        music.play_tone(Note.A,70)
    elif input.pin_is_pressed(TouchPin.P2):
        global Day
        Day += +1
        music.play_tone(Note.B,70)
    if Day == 1:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        . # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
    elif Day == 2:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # . # # #
        . . . # #
        . . . . .
        . . . . .
        """)
    elif Day == 3:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # # . # #
        . . . # #
        . . . . .
        . . . . .
        """)
    elif Day == 4:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # # # . #
        . . . # #
        . . . . .
        . . . . .
        """)
    elif Day == 5:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # # # # .
        . . . # #
        . . . . .
        . . . . .
        """)
    elif Day == 6:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . . #
        . . . . .
        . . . . .
        """)
    elif Day == 7:
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # #
        . . . . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        # # # # #
        . . . # .
        . . . . .
        . . . . .
        """)
def DigitalWatch():
    Driver()
    global Wall
    music.ring_tone(Note.C)
    pause(50)
    music.stop_all_sounds()
    basic.show_string(Hours + ":" + Minutes)
    music.ring_tone(Note.C)
    pause(50)
    music.stop_all_sounds()
    Wall = 0
def Driver():
    led.set_brightness(Brightness)
    music.set_volume(Volume)
    radio.set_frequency_band(83)
    radio.set_transmit_power(7)
    music.stop_all_sounds()

def Limiter():
    global Wall
    global Day
    global CompassStill
    if Wall >= 10:
        global Wall
        Wall = 9
        music.ring_tone(Note.C5)
        pause(70)
        music.ring_tone(Note.A)
        pause(70)
        music.ring_tone(Note.F)
        pause(70)
        music.stop_all_sounds()
        pause(70)
    if Day == 8:
        global Day
        Day = 1
    elif Day == 0:
        global Day
        Day = 7
    if CompassStill == -1:
        global CompassStill
        CompassStill = 0
        music.ring_tone(Note.C5)
        pause(70)
        music.ring_tone(Note.A)
        pause(70)
        music.ring_tone(Note.F)
        pause(70)
        music.stop_all_sounds()
        pause(70)
    elif CompassStill == 3:
        global CompassStill
        CompassStill = 2
        music.ring_tone(Note.C5)
        pause(70)
        music.ring_tone(Note.A)
        pause(70)
        music.ring_tone(Note.F)
        pause(70)
        music.stop_all_sounds()
        pause(70)
    if Volume <= -1:
        global Volume
        Volume = 0
        music.play_tone(Note.C5, 100)
    if Volume >= 257:
        global Volume
        Volume = 255
        music.play_tone(Note.C5,100)
    if Brightness < 20:
        global Brightness
        Brightness = 20
        music.play_tone(Note.C5, 100)
    if Brightness >= 256:
        global Brightness
        Brightness = 255
        music.play_tone(Note.C5,100)

def Buttons_LOCK():
    if input.pin_is_pressed(TouchPin.P1):
        music.ring_tone(Note.C5)
        pause(70)
        music.ring_tone(Note.A)
        pause(70)
        music.ring_tone(Note.F)
        pause(70)
        music.stop_all_sounds()
    elif input.pin_is_pressed(TouchPin.P2):
        music.ring_tone(Note.C5)
        pause(70)
        music.ring_tone(Note.A)
        pause(70)
        music.ring_tone(Note.F)
        pause(70)
        music.stop_all_sounds()
def Buttons():
    if input.button_is_pressed(Button.B):
        global Wall
        Wall += +1
        music.ring_tone(Note.B)
        pause(100)
        music.stop_all_sounds()
        pause(100)
    if input.button_is_pressed(Button.AB):
        global Wall
        Wall = 1
        music.ring_tone(Note.C5)
        pause(100)
        music.stop_all_sounds()
        pause(1000)
    if input.button_is_pressed(Button.A):
        global Wall
        Wall += -1
        music.ring_tone(Note.A)
        pause(100)
        music.stop_all_sounds()
        pause(100)
def Start():
    AODON()
    Driver()
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    """)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # . . .
    """)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # . .
    """)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # .
    """)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    """)
    music.play_tone(Note.C5,90)
    music.play_tone(Note.A,90)
    music.play_tone(Note.D,90)
    music.play_tone(Note.F,90)
    music.play_tone(Note.D,90)
    music.play_tone(Note.C5,90)
    input.calibrate_compass()
def Watch():
    global Hours
    global Minutes
    global Brightness
    basic.clear_screen()
    led.plot(2, 2)
    led.set_brightness(AODDATA)
    #Hours
    if Hours == 0:
        led.plot(2, 1)
    elif Hours == 1 or Hours == 2:
        led.plot(3, 1)
    elif Hours == 3:
        led.plot(3, 2)
    elif Hours == 4 or Hours == 5:
        led.plot(3, 3)
    elif Hours == 6:
        led.plot(2, 3)
    elif Hours == 7 or Hours == 8:
        led.plot(1, 3)
    elif Hours == 9:
        led.plot(1, 2)
    elif Hours == 10 or Hours == 11:
        led.plot(1, 1)
    elif Hours == 12:
        led.plot(2, 1)
    elif Hours == 13 or Hours == 14:
        led.plot(3, 1)
    elif Hours == 15:
        led.plot(3, 2)
    elif Hours == 16 or Hours == 17:
        led.plot(3, 3)
    elif Hours == 18:
        led.plot(2, 3)
    elif Hours == 19 or Hours == 20:
        led.plot(1, 3)
    elif Hours == 21:
        led.plot(1, 2)
    elif Hours == 22 or Hours == 23:
        led.plot(1, 1)
    elif Hours == 24:
        led.plot(2, 1)
    #Minutes
    if Minutes == 59 or Minutes < 3:
        led.plot(2, 0)
    elif Minutes >= 3 and Minutes < 5:
        led.plot(3, 0)
    elif Minutes >= 5 and Minutes < 11:
        led.plot(4, 0)
    elif Minutes >= 11 and Minutes < 14:
        led.plot(4, 1)
    elif Minutes >= 14 and Minutes < 18:
        led.plot(4, 2)
    elif Minutes >=18  and Minutes < 20:
        led.plot(4, 3)
    elif Minutes >= 20 and Minutes < 26:
        led.plot(4, 4)
    elif Minutes >= 26 and Minutes < 29:
        led.plot(3, 4)
    elif Minutes >= 29 and Minutes < 33:
        led.plot(2, 4)
    elif Minutes >= 33 and Minutes < 35:
        led.plot(1, 4)
    elif Minutes >= 35 and Minutes < 41:
        led.plot(0, 4)
    elif Minutes >= 41 and Minutes < 44:
        led.plot(0, 3)
    elif Minutes >= 44 and Minutes < 47:
        led.plot(0, 2)
    elif Minutes >= 47 and Minutes < 49:
        led.plot(0, 1)
    elif Minutes >= 49 and Minutes < 55:
        led.plot(0, 0)
    elif Minutes >= 55 and Minutes < 59:
        led.plot(1, 0)
