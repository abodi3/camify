import emailSender
from picamera import PiCamera
from gpiozero import MotionSensor



        
pir = MotionSensor(4) #monstion sensor connected to gpio 4

pir.wait_for_motion() #waiting to detect motion

print("Motion Detected")


        
    
camera = PiCamera() #camera object created and rotated
camera.rotation = 180


    
image = camera.capture('/home/pi/webapp/static/selfie.jpg') #image capture
            

filetoSend = "/home/pi/webapp/static/selfie.jpg" #path of image set to filetoSend


send = emailSender.notify(filetoSend) #use emailSender's method notify to send email

