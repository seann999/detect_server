import threading

class Streamer:
    def __init__(self):
        self.image = None

    def start_stream(self):
        pass

    def start_stream_threads(self, url=None):
        if url is None:
            threading._start_new_thread(self.start_stream, ())
        else:
            threading._start_new_thread(self.start_stream, (url,))