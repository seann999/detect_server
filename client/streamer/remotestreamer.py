import urllib.request

import cv2
import numpy as np

from streamer.streamer import Streamer

from streamer.streamdisplay import StreamDisplay

stream_url = None


class RemoteStream(Streamer):
    def start_stream(self, url='http://192.168.1.13:8080/video'):
        print("starting stream...")

        stream = urllib.request.urlopen(url)
        bytes = b''

        while True:
            bytes += stream.read(1024)
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes[a:b + 2]
                bytes = bytes[b + 2:]
                self.image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)


if __name__ == "__main__":
    display = StreamDisplay(RemoteStream())
