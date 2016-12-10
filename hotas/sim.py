class BaseHandler:

    control_name = 'ThrottleAndBrake'
    previous_value = None
    raildriver = None

    def __init__(self, raildriver):
        self.raildriver = raildriver

    def handle(self, value):
        if value != self.previous_value:
            print(id(self), 'Setting value', value)
            self.raildriver.set_controller_value(self.control_name, value)
        self.previous_value = value


class NotchedHandler(BaseHandler):

    notches = []

    def handle(self, value):
        for comparator, notch in self.notches:
            if comparator(value):
                super(NotchedHandler, self).handle(notch)


class Class222Handler(BaseHandler):
    pass


class Class375Handler(NotchedHandler):

    notches = [
        (lambda v: v == 0, 0),
        (lambda v: 0 < v <= .16, .07),
        (lambda v: .16 < v <= .32, .15),
        (lambda v: .32 < v <= .48, .31),
        (lambda v: .48 < v < .52, .5),
        (lambda v: .52 <= v < .68, .64),
        (lambda v: .68 <= v < .84, .7),
        (lambda v: .84 <= v < 1, .86),
        (lambda v: v == 1, 1),
    ]
