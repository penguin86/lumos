from math import log

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
class EVCalculator:
    # K is the reflected-light meter calibration constant (unit: cd s/m2 ISO)
    # (https://en.wikipedia.org/wiki/Light_meter#Calibration_constants)
    K = 12.5    # TODO: Add to settings?

    def luxToEV(lux: float) -> float:
        # Wikipedia (https://en.wikipedia.org/wiki/Exposure_value#EV_as_a_measure_of_luminance_and_illuminance)
        # says E = 2.5 * (2^EV), so the inverse is EV = ln(2*E/5)/ln(2)
        return log(2*lux/5, 2)


