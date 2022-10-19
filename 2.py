#from picamera import PiCamera
#from picamera.array import PiRGBArray
from time import sleep
import cv2


def main():
    label_dict = {}
    with open('models/ssd_mobilenet/labels.txt','r') as f:
        for l in f:
            arr = l.strip().split(':')
            label_dict[int(arr[0])] = arr[1].strip()

    model = cv2.dnn.readNetFromTensorflow(
                'models/ssd_mobilenet/frozen_inference_graph.pb',
                'models/ssd_mobilenet/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    vid = cv2.VideoCapture(0)

    resolution = (100, 100)
    cols, rows = resolution

    vid.set(3, cols)  # set Width
    vid.set(4, rows)  # set Height

    #raw_capture = PiRGBArray(camera, size=resolution)
    sleep(1) # let camera warm up

    color = (23, 230, 210)

    while(True):
        ret, image = vid.read()

        model.setInput(cv2.dnn.blobFromImage(image, size=resolution, swapRB=True, crop=False))
        net_out = model.forward()

        for detection in net_out[0,0,:,:]:
            score = float(detection[2])
            if score > 0.5: 
                label = int(detection[1])
                label_str = label_dict.get(label, 'unknown')
                print(label_str)

                left = detection[3] * cols
                top = detection[4] * rows
                right = detection[5] * cols
                bottom = detection[6] * rows
                cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), color, thickness=2)
                cv2.putText(image, label_str, (int(left) + 3, int(bottom) - 3), cv2.FONT_HERSHEY_SIMPLEX, 
                            1.0, color)
        
        cv2.imshow('press Q to exit', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
