import cv2
from streamdisplay import StreamDisplay
from streamer import Streamer


class WebcamStream(Streamer):
    def start_stream(self, size=(640, 480)):
        print("starting stream...")

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            self.image = frame


if __name__ == "__main__":
    stream = WebcamStream()
    stream.start_stream_threads()
    display = StreamDisplay(stream)
