import fire
from julday import JulianDayNumber

"""
    Returns the Mean Anomaly of a planet at a given time (Julian Day Number)

    Source: http://aa.quae.nl/en/reken/zonpositie.html

    @param m0 constant
    @param m1 constant
    @param jdn julian day number
"""
def planet_mean_anomaly(m0, m1, jdn):
    return (m0 + m1 x (jdn - JulianDayNumber(2000, 1, 1))) % 360


class SunposApp():
    def position(self, year, month, day, lat, lon, planet='Earth'):
        pass
        
        
if __name__ == '__main__':
    fire.Fire(SunposApp)
