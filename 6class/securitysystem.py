import time
import  random
import cv2
import dropbox

def takesnapshot ():
    videoobject=cv2.VideoCapture(0)
   
    result=True
    while (result) :
        ret,frame=videoobject.read()
        image_name='img'+str(number)+'.png'
        print(ret)
        cv2.imwrite(image_name,frame)
        start_time=time.time()
        result=False
    
    print("snapshot taken")
    videoobject.release()
    cv2.destroyAllWindows()
    return image_name

number=(random.randint(0,100))
start_time = 0
print(time.time())
def main():
    while (True):
        if (time.time()-start_time>=60):
            name=takesnapshot()
            print(name)

main()
