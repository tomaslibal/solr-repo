import fire
from julday import JulianDayNumber
from constants import MEAN_ANOMALY, TRUE_ANOMALY_COEFF, PERIPHELION, OBLIQUITY
from math import sin, atan2


"""
    Process
    =======

    Assumes: Earth, Singapore (1.367deg N lat, 103.8deg E lon), 
    J = 12pm Jan 1, 2017.

    1 The mean anomaly
    ------------------

    The mean anomaly M is calculated as below

    M = (M0 + M1 * (J - J2000)) mod 360
    
    M0 = 357.5291
    M1 = 0.98560028
    J2000 = 2451545
    J = 2457754.5

    2 True anomaly from the mean anomaly
    ------------------------------------

    v (nu) is the true anomaly which would be same as the mean anomaly if the
    orbit were a perfect circle.

    v = M + C

    C approx C1 * sin(M) + C2 * sin(2M) + C3 * sin (3M) + C4 * sin(4M) + C5 * sin(5M) + C6 * sin(6M)

    3 Ecliptic longitude and the obliquity of the ecliptic
    ------------------------------------------------------

    P (Capital pi) is the periphelion of the planet and is provided as 
    a constant.

    The obliquity of the equator of the planet e (epsilon) is also provided
    as a constant.

    Both constants are in degrees.

    P_earth = 102.9373
    e_earth = 23.4393

    The ecliptic represents the plane on which the satellite orbits the start
    and the ecliptical longitude l (lambda) is the position along the orbit.

    This position can be seen from the star as

    l = v + P

    And for the planet it is exactly opposite so we can just add 180deg

    l = v + P + 180deg

    4 The Equatorial coordinates
    ----------------------------

    These coordinates are the right ascension a (alpha) and the declination
    d (delta).

    a = arctan(sin(l) * cos(e), cos l)
    d = arcsin(sin(l) * sin(e))

    But these values can also be estimated using a table and a simpler formula.

    5 The position of the observer relative to the position of the star
    -------------------------------------------------------------------

    phi (phi) is the northern latitude, lon is the western longitude, and 
    o (theta) is the sidereal time which expresses the rotation angle 
    of the planet relative to the stars.

    We already have the latitude and the longitude.

    o = (o0 + o1 * (J - J2000) - l) mod 360

    For Earth:
    o0 = 280.1470
    o1 = 360.9856235

    Finally, we can find the position of the star using the azimuth A and 
    the altitude h (respective to the horizon of the observer). Azimuth is 
    measured from south to west.

    The hour angle H (angular time (sidereal) since the star passed through 
    the meridian)

    H = o - a

    The altitude is given by

    h = arcsin(sin(phi) * sin(delta) + cos(phi) * cos(delta) * cos(H))

    And the azimuth is

    A = arctan(sin(H), cos(H) * sin(phi) - tan(delta) * cos(phi))

"""

"""
    Returns the Mean Anomaly of a planet at a given time (Julian Day Number)

    Source: http://aa.quae.nl/en/reken/zonpositie.html

    @param m0 constant
    @param m1 constant
    @param jdn julian day number
"""
def planet_mean_anomaly(m0, m1, jdn):
    return (m0 + m1 * (jdn - JulianDayNumber(2000, 1, 1).jdn())) % 360


def true_anomaly(c1, c2, c3, c4, c5, c6, m):
    return c1 * sin(m) + c2 * sin(2*m) + c3 * sin(3*m) + c4 * sin(4*m) + c5 * sin(5*m) + c6 * sin(6*m)

class SunposApp():
    def position(self, year, month, day, lat, lon, planet='Earth'):
        J = JulianDayNumber(2017, 1, 1).jdn()
        M = planet_mean_anomaly(MEAN_ANOMALY[planet][0], MEAN_ANOMALY[planet][1], J)
        true_anom = TRUE_ANOMALY_COEFF[planet]
        v = true_anomaly(true_anom[0], true_anom[1], true_anom[2], true_anom[3], true_anom[4], true_anom[5], M)
        
        
if __name__ == '__main__':
    fire.Fire(SunposApp)
