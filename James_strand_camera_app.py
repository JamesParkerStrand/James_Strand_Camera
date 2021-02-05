from guizero import App, PushButton, Combo, Slider, Text, TextBox
from picamera import PiCamera
from datetime import datetime
from fractions import Fraction
    
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.image_denoise = False
camera.video_denoise = False

app = App("James Strand Camera App", height=880, width=1000)

app.font = "DejaVuSerifCondensed"

def preview():
    camera.start_preview(fullscreen=False, window = (50,150, 1280, 960))
def stop_preview():
    camera.stop_preview()    
def shutter():      
    date = datetime.now()
    camera.image_denoise = False
    camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpeg')
def longexposure():
    if longexpslide.value == 0:
        camera.framerate = 30
        camera.exposure_mode = 'auto'
        camera.shutter_speed = 0
        camera.sensor_mode=1
    if longexpslide.value == 1:
        camera.framerate = Fraction(1, 1)
        camera.shutter_speed = 1000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 2:
        camera.framerate = Fraction(1, 2)
        camera.shutter_speed = 2000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 3:
        camera.framerate = Fraction(1, 3)
        camera.shutter_speed = 3000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 4:
        camera.framerate = Fraction(1, 4)
        camera.shutter_speed = 4000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 5:
        camera.framerate = Fraction(1, 5)
        camera.shutter_speed = 5000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 6:
        camera.framerate = Fraction(1, 6)
        camera.shutter_speed = 6000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 7:
        camera.framerate = Fraction(1, 7)
        camera.shutter_speed = 7000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 8:
        camera.framerate = Fraction(1, 8)
        camera.shutter_speed = 8000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 9:
        camera.framerate = Fraction(1, 9)
        camera.shutter_speed = 9000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
    if longexpslide.value == 10:
        camera.framerate = Fraction(1, 10)
        camera.shutter_speed = 10000000
        camera.exposure_mode = 'off'
        date = datetime.now()
        camera.capture('/home/pi/Pictures/' + str(date) + '-image.jpg')
def record():
    date = datetime.now()
    camera.video_denoise = False
    camera.start_recording('/home/pi/Videos/' + str(date) + '-video.h264')
def stoprecording():
    camera.stop_recording()
def sizes(selected_value):
    if selected_value == "instagram size":
        camera.resolution = (500, 500)
    if selected_value == "normal 1080p":
        camera.resolution = (1920, 1080)
    if selected_value == "vga":
        camera.resolution = (640, 480)
def effects(selected_value):
    if selected_value == "none":
        camera.image_effect = 'none'
    if selected_value == "filter1":
        camera.image_effect = 'cartoon'
    if selected_value == "filter2":
        camera.image_effect = 'negative'
def metering(selected_value):
    if selected_value == "Average":
        camera.meter_mode = 'average'
    if selected_value == "Spot":
        camera.meter_mode = 'spot'
    if selected_value == "Backlit":
        camera.meter_mode = 'backlit'
    if selected_value == "Matrix":
        camera.meter_mode = 'matrix'
def isochange():
    camera.iso = isochanger.value
def shutterspeed():
    camera.shutter_speed = shutterspeed.value
def test():
    print(test.value)
def exposure():
    camera.exposure_compensation = expcomp.value
def exposurereset():
    expcomp.value = 0
    
test = TextBox(app, command=test, text="this is a pushbutton test")

Preview = PushButton(app, command=preview, text="preview")

Preview.font = "Times New Roman"

Preview.text_color = "Red"

Preview.height = "10"

Preview.text_size = "15"
    
StopPreview = PushButton(app, command=stop_preview, text="stop preview")
    
shutter = PushButton(app, command=shutter, text="shutter")

longexposurebutton = PushButton(app, command=longexposure, text="long exposure shutter")

longexpslide = Slider(app, start=0, end=10, width=400)

longexpteller = Text(app, text="long exposure slider")

record = PushButton(app, command=record, text="record")

StopRecording = PushButton(app, command=stoprecording, text="stop recording")

sizes = Combo(app, options=["normal 1080p", "instagram size", "vga"], command=sizes)

effects = Combo(app, options=["none", "filter1", "filter2"], command=effects)

effects.text_color = "Blue"

effects.font = "Helvetica"

effects.text_size = "20"

effects.bg = "Yellow"

isochanger = Slider(app, command=isochange, start=0, end=62000, width=1500)

isoteller = Text(app, text="Iso speed (Note:Leave on 0 for automatic!)",)

shutterspeed = Slider(app, command=shutterspeed, start=0, end=50000, width=1000)

shutterspeedteller = Text(app, text="shutter speed (Note:Leave on 0 for automatic!)")

expcomp = Slider(app, start=-25, end=25, command=exposure)

expcompteller = Text(app, text="exposure compensation")

expreset = PushButton(app, text="reset exposure compensation", command=exposurereset)

meteringteller = Text(app, text="Metering Modes")

metermodes = Combo(app, options=["Average", "Spot", "Backlit", "Matrix"], command=metering)

app.display()
