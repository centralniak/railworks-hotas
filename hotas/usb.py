class ThrustmasterTFlightHotasX:
    """
    Thrustmaster T-Flight Hotas X
    https://goo.gl/hgGdwJ
    """

    @staticmethod
    def handle_raw(raw_input):
        raw_value = raw_input[8]
        zero_to_one_value = round(raw_value / float(255), 2)
        return zero_to_one_value
