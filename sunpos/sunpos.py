import fire
from datetime import datetime
from julday import JulianDayNumber
from constants import MEAN_ANOMALY, TRUE_ANOMALY_COEFF, PERIPHELION, OBLIQUITY, SIDEREAL
from math import sin, cos, tan, asin, atan2, radians, degrees


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

    a = arctan(sin(l) * cos(e), cos(l))
    d = arcsin(sin(l) * sin(e))

    But these values can also be estimated using a table and a simpler formula.

    5 The position of the observer relative to the position of the star
    -------------------------------------------------------------------

    phi (phi) is the northern latitude, lon is the western longitude, and 
    o (theta) is the sidereal time which expresses the rotation angle 
    of the planet relative to the stars.

    We already have the latitude and the longitude.

    The sidereal time is

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
    return (m0 + m1 * (jdn - round(JulianDayNumber(2000, 1, 1).jdn()))) % 360


def true_anomaly(c1, c2, c3, c4, c5, c6, m):
    C = (c1 * sin(radians(m))) + (c2 * sin(radians(2*m))) + (c3 * sin(radians(3*m))) + (c4 * sin(radians(4*m))) + (c5 * sin(radians(5*m))) + (c6 * sin(radians(6*m)))
    # print "C={0}".format(C)
    return m + C

def ecliptic_longitude(v, P):
    return (v + P + 180) % 360

def right_ascension(l, e):
    return degrees(atan2(sin(radians(l)) * cos(radians(e)), cos(radians(l))))

def declination(l, e):
    return degrees(asin(sin(radians(l)) * sin(radians(e))))

"""
    lon_west: longitude in degrees west of the prime meridian; if the place lies
    to the east of the prime meridian then it needs to be negated (i.e. 
    the center of Netherlands is 5.75deg east of the prime meridian so it has
    either 5.75deg E or -5.75deg W longitude.
"""
def sidereal_time(theta0, theta1, J, lon_west):
    J2000 = round(JulianDayNumber(2000, 1, 1).jdn())
    return (theta0 + theta1 * (J - J2000) - lon_west) % 360

"""
    Relative to the observer's horizon (assumes the horizon plane? Meaning that
    if the horizon is obstructed by some geographical features the horizon is
    still assumed to be as if the observer stood at 0m above/below the ground
    with no elevation around)
"""
def celestial_body_pos(theta, a, phi, d):
    H = theta - a
    A = degrees(atan2(sin(radians(H)), cos(radians(H)) * sin(radians(phi)) - tan(radians(d)) * cos(radians(phi))))
    h = degrees(asin(sin(radians(phi)) * sin(radians(d)) + cos(radians(phi)) * cos(radians(d)) * cos(radians(H))))
    return (A, h)

def format_time(hour, minute):
    d = datetime(2000, 1, 1, hour, minute, 0)
    return d.strftime('%I:%M')


class SunposApp():
    def position(self, year, month, day, lat, lon, hour=12, minute=0, planet='Earth'):
        J = round(JulianDayNumber(year, month, day).jdn())
        M = planet_mean_anomaly(MEAN_ANOMALY[planet][0], MEAN_ANOMALY[planet][1], J)
        true_anom = TRUE_ANOMALY_COEFF[planet]
        v = true_anomaly(true_anom[0], true_anom[1], true_anom[2], true_anom[3], true_anom[4], true_anom[5], M)
        l = ecliptic_longitude(v, PERIPHELION[planet])
        a = right_ascension(l, OBLIQUITY[planet])
        d = declination(l, OBLIQUITY[planet])
        phi = lat
        theta = sidereal_time(SIDEREAL[planet][0], SIDEREAL[planet][1], J, lon)
        A, h = celestial_body_pos(theta, a, phi, d)
        """
        print "M={0}".format(M)
        print "v={0}".format(v)
        print "l={0}".format(l)
        print "a={0}".format(a)
        print "d={0}".format(d)
        print "theta={0}".format(theta)
        print "H={0}".format(theta-a)
        print "--------"
        """
        print "{0}UTC on {1}/{2}/{3}".format(format_time(hour, minute), year, month, day)
        print "lat={0}N lon={1}W".format(lat, lon)
        print "azimuth A={0}".format(A)
        print "altitude h={0}".format(h)

        
if __name__ == '__main__':
    fire.Fire(SunposApp)
