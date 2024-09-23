import os
from pypylon import pylon
import cv2



import warnings
warnings.filterwarnings('ignore')



    # delete all files in directory: images/partno1/pred/*.*
# os.system('del /S /Q .\\images\\partno1\\sample\\*.*')
device_info = {}
device_info['2676017D53E2'] = 'E' # 24990690
device_info['2676017E15AE'] = 'S' # 25040302
device_info['2676017E189A'] = 'N' # 25041050
device_info['2676017D0FF9'] = 'W' # 24973305
instance = pylon.TlFactory.GetInstance()

# Get all the available devices
devices = instance.EnumerateDevices()

for loop in range (100, 120):

    print('\n\npress any key -----------')    
    char = input("Enter a character: ")


    for i, device in enumerate(device_info):
        

        str1 = 'NG_image/NG_' + device_info[device] +  '-' + str(loop).zfill(4) + '.bmp'
        print(str1)
        
        
        # 創建相機對象
        # camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        # print(f'Create camera {i}')
        camera = pylon.InstantCamera(instance.CreateDevice(devices[i]))
        guid = camera.GetDeviceInfo().GetDeviceGUID()
        # print(f'Create guid {guid} = position: {device_info[guid]}')
        # 打開相機
        camera.Open()
    
        # 調整相機曝光時間
        camera.ExposureAuto.SetValue('Off')
        camera.ExposureTime.SetValue(200000)
    
        # 拍照存檔
        camera.StartGrabbing()
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            # Access the image data
            image = grabResult.Array
            img_path = str1
            cv2.imwrite(img_path, image)
            # print(img_path)
        grabResult.Release()
        camera.StopGrabbing()
    

