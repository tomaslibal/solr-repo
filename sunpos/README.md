Finds the azimuth `A` and the altitude above/below the horizon `h` of the Sun on planets of our solar system for a specified time.

Usage

```
python sunpos.py position YEAR MONTH DAY LAT LON_W [HOUR] [MINUTE]
```

- The time is in UTC
- `LON_W` is the western longitude. If the location is east from the prime meridian, then negate its value to get the western longitude.

Supports

3. Earth

<!--
1. Mercury
2. Venus

4. Mars
5. Jupiter
6. Saturn
7. Uranus
8. Neptun
-->

Questions

- Does the altitude `h` refer to the center of the Sun's disc?
