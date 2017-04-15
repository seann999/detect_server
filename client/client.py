
from streamer.webcamstreamer import WebcamStream
import cv2
import time
import requests
import sys

def send(image):
    cv2.imwrite("image.png", image)

    r = requests.post(sys.argv[1], files={'image': open("image.png", "rb")})
    print(r.text)

if __name__ == "__main__":
    print("ip", sys.argv[1])

    stream = WebcamStream()
    stream.start_stream_threads()

    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

    while (True):
        if stream.image is not None:
            cv2.imshow("frame", stream.image)
            k = cv2.waitKey(1)

            if k == 27:  # esc
                break

            send(stream.image)
            time.sleep(1)
        else:
            print("%i: no frame data" % time.time())
            time.sleep(1)

    cv2.destroyAllWindows()
