import jdcal

class JulianDayNumber():
    def __init__(self, year, month, day, hour = 12, minute = 0):
        self.d = sum(jdcal.gcal2jd(year, month, day))
        self.h = hour
        self.m = minute
    def jdn(self):
        return self.d

