from itertools import chain, imap
import fire

def flatmap(fun, lst):
    return chain.from_iterable(imap(fun ,lst))

compass = (0, 360)
dirs = (
        ('S', 'South', 0),
        ('SW', 'South-West', 45),
        ('W', 'West', 90),
        ('NW', 'North-West', 135),
        ('N', 'North', 180),
        ('NE', 'North-East', 225),
        ('E', 'East', 270),
        ('SE', 'South-East', 315)
        )
simple_dirs = (
        dirs[0],
        dirs[2],
        dirs[4],
        dirs[6]
        )

imp = map(lambda coord: coord[2], dirs)
simple_imp = map(lambda coord: coord[2], simple_dirs)
maxd = 45
simple_maxd = 90

angle = 221.10

class Azimuth2d():

    simple = True

    def quadrant(self, angle):
        rem = angle % 360
        if rem >= 0 and rem <= 90:
            return 0
        if rem > 90 and rem <= 180:
            return 1
        if rem > 180 and rem <= 270:
            return 2
        return 3

    def dr(self, quadrant, df):
        if quadrant == 0:
            if df < 0:
                return 'south of'
            else:
                return 'west of'
        if quadrant == 1:
            if df < 0:
                return 'west of'
            else:
                return 'north of'
        if quadrant == 2:
            if df < 0:
                return 'north of'
            else:
                return 'east of'
        if quadrant == 3:
            if df < 0:
                return 'east of'
            else:
                return 'south of'

    def azimuth(self, angle):
        smallest = (360, dirs[0])
        directions = dirs
        md = maxd
        imps = imp
        if self.simple:
            directions = simple_dirs
            md = simple_maxd
            imps = simple_imp
        for p in directions:
            adif = abs(p[2] - angle)
            if adif < md and adif < abs(smallest[0]):
                df = angle - p[2]
                smallest = (df, p)

        # dir
        if smallest[0] not in imps:
            q = self.quadrant(angle)
            dr = self.dr(q, smallest[0])
            print str(abs(smallest[0])) + 'deg ' + dr + ' ' + smallest[1][0]
        else:
            print smallest[1][0]

if __name__ == '__main__':
    fire.Fire(Azimuth2d)
