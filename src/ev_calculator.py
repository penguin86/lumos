from math import log

class EVCalculator:

    def luxToEV(lux: float) -> float:
        # Wikipedia (https://en.wikipedia.org/wiki/Exposure_value#EV_as_a_measure_of_luminance_and_illuminance)
        # says E = 2.5 * (2^EV), so the inverse is EV = ln(2*E/5)/ln(2)
        return log(2*lux/5, 2)

