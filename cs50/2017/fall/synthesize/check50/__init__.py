from check50 import *

class Synthesize(Checks):
    @check()
    def exists(self):
        """synthesize.c exists"""
        self.require("synthesize.c")
        self.add("transcribe.py", "songs") # we'll probably want to make this byte code

    @check("exists")
    def compiles(self):
        """synthesize compiles"""
        self.spawn("make synthesize").exit(0)

    @check("compiles")
    def happy_bday(self):
        """synthesizes happy birthday correctly"""
        self.spawn("./synthesize song.wav < songs/bday.txt").exit(0)
        # We could maybe give better feedback than this but this will highlight which notes they got wrong
        # Would be cool if we could overload how Mismatch gets formatted
        self.spawn("./transcribe song.wav").stdout(File("songs/bday.txt")).exit()

