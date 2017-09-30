from check50 import *


class SumDemo(Checks):

    @check()
    def exists(self):
        """sum.c exists."""
        self.require("sum.c")

    @check("exists")
    def compiles(self):
        """sum.c compiles"""
        self.spawn("clang -std=c11 -o sum sum.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """40 + 2 is 42"""
        self.spawn("./sum").stdin("40").stdin("2").stdout("42").exit(0)
