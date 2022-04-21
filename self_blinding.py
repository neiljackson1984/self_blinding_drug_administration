import time
import sys

from barcap.barcode import BarcodeCapture



def main():    
    # Default camera index
    camera_index = 0

    # # Camera selection routine
    # try:
    #     from barcap.device_list import select_camera, camera_list

    #     # Get camera list
    #     dev_list = camera_list()

    #     # Select a camera
    #     camera_index = select_camera(len(dev_list))
    # except Exception as e:
    #     print('Unable to run camera selection routine!: ' + str(e))

    # Start capture
    # print(f'camera_index: {camera_index}')
    capture = BarcodeCapture(camera=camera_index)
    capture.start()

    # Run capture loop
    while capture.is_alive():
        if capture.new:
            # Debugging
            print(f'output: {capture.output}')

            # Debugging
            time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(capture.last_epoch))
            print(f'last capture: {time_stamp}')
            localNow = time.time()
            print('capture.last_epoch: ' + str(capture.last_epoch))
            print('localNow: ' + str(localNow))
            sys.stdout.flush()
            # # Stop capture on the first output reading
            # capture.stop()
            # break

        time.sleep(0.1)



def generateLabels(pathOfOutputPdfFile,  envelopeSerialNumbers):
    #  pathOfOutputPdfFile is a string
    # envelope serial numbers is list of serial numbers (integers)
    pass



#it is necessary to put the actions of our script within the following "main test"
# because the barcode capture module uses the multiprocessing library to create a subprocess.
# On Windows, when the multiprocessing module creates a subprocess, it imports (i.e. executes) 
# this script in order to initialize variables, and if our actions are not protected 
# by a main test, then the import process will attempt to create another subprocess ad infinitum.
if __name__ == '__main__':
    main()