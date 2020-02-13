import time


class MyProfiler:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("DEBUG: foo took {:.4f} seconds, no error".format(time.time() - self.start))

    def elapsed(self):
        return "{:.4f}".format(time.time() - self.start)


with MyProfiler("foo") as c:
    time.sleep(0.5)
    print("Elapsed:", c.elapsed())
    time.sleep(0.5)

print("OK")
