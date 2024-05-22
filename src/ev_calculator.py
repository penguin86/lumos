from math import log, sqrt

'''
This class does all the required math. It is based on the Wikipedia page
https://en.wikipedia.org/wiki/Exposure_value
(N^2)/t = L*S/K
where:
    N is the relative aperture (f-number)
    t is the exposure time ("shutter speed") in seconds
    L is the average scene luminance
    S is the ISO arithmetic speed
    K is the reflected-light meter calibration constant
'''

# K is the reflected-light meter calibration constant (unit: cd s/m2 ISO)
# (https://en.wikipedia.org/wiki/Light_meter#Calibration_constants)
K = 12.5

class EVCalculator:

    DEFAULT_ISO_SPEED = 100

    APERTURE_VALUES = {
        1/32: "f/ 32",
        1/22: "f/ 22",
        1/16: "f/ 16",
        1/11: "f/ 11",
        1/8: "f/ 8",
        1/5.6: "f/ 5.6",
        1/4: "f/ 4",
        1/2.8: "f/ 2.8",
        1/2: "f/ 2",
        1/1.4: "f/ 1.4"
    }

    SHUTTER_SPEED_VALUES = {
        1/4000: "1/4000",
        1/2000: "1/2000",
        1/1000: "1/1000",
        1/500: "1/500",
        1/250: "1/250",
        1/125: "1/125",
        1/60: "1/60",
        1/30: "1/30",
        1/15: "1/15",
        1/8: "1/8",
        1/4: "1/4",
        1/2: "1/2",
        1: "1 sec",
        2: "2 sec",
        4: "4 sec",
        8: "8 sec",
        15: "15 sec",
        30: "30 sec"
    }

    def luxToEV(lux: float) -> float:
        # Wikipedia (https://en.wikipedia.org/wiki/Light_meter#Exposure_equations)
        # says E = 2.5 * (2^EV), so the inverse is EV = ln(2*E/5)/ln(2)
        return log(2*lux/5, 2)

    def calcShutterSpeed(isoSpeed: int, lux: float, aperture: float):
        result = (aperture*aperture*K)/(lux*isoSpeed)
        print("aperture: {}, K: {}, lux: {}, isoSpeed: {}, result: {}".format(aperture, K, lux, isoSpeed, result))
        return result

    def calcAperture(isoSpeed: int, lux: float, shutterSpeed: float):
        # shutterSpeed is in seconds
        return sqrt(lux*isoSpeed*shutterSpeed/K)


    def toNearestStr(valueToRound: float, roundingValues: dict[float,str]) -> [str, bool]:
        # Rounds to the nearest value in the provided ORDERED dict.
        # The dict is expected to have a float value as key and the corresponding human readable string value as value
        # Returns the string value and a boolean set to true if the value was in the list range.

        roundingNumericValues = list(roundingValues.keys())
        roundingStringValues = list(roundingValues.values())

        first = roundingNumericValues[0]
        last = roundingNumericValues[-1]

        if valueToRound < first / 1.5:
            # More than half stop below minimum value!
            return [roundingStringValues[0], False]
        if valueToRound > last * 1.5:
            # More than half stop above maximum value!
            return [roundingStringValues[-1], False]

        # Note: range(roundingValues - 1) to exclude last element
        for i in range(len(roundingNumericValues) - 1):
            value = float(roundingNumericValues[i])
            nextValue = float(roundingNumericValues[i + 1])
            limit = (value + nextValue) / 2
            if valueToRound <= limit:
                return [roundingStringValues[i], True]
        return [roundingStringValues[-1], True]




