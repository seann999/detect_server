import cv2
import time

class StreamDisplay:
    def __init__(self, streamer):
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

        while (True):
            if streamer.image is not None:
                cv2.imshow("frame", streamer.image)
                k = cv2.waitKey(1)

                if k == 27: #esc
                    break
            else:
                print("%i: no frame data" % time.time())

        cv2.destroyAllWindows()