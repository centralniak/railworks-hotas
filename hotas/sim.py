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


class Class170_171Handler(NotchedHandler):

    notches = [
        (lambda v: v == 0, 0),
        (lambda v: 0 < v <= .16, .20),
        (lambda v: .16 < v <= .32, .30),
        (lambda v: .32 < v <= .48, .38),
        (lambda v: .48 < v < .52, .5),
        (lambda v: .52 <= v < .60, .57),
        (lambda v: .60 <= v < .68, .64),
        (lambda v: .68 <= v < .76, .71),
        (lambda v: .76 <= v < .84, .78),
        (lambda v: .84 <= v < .92, .84),
        (lambda v: .92 <= v < 1, .92),
        (lambda v: v == 1, 1),
    ]


class Class375_377Handler(NotchedHandler):

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


class Class465_466Handler(NotchedHandler):

    notches = [
        (lambda v: v == 0, 0),
        (lambda v: 0 < v <= .16, .1),
        (lambda v: .16 < v <= .32, .2),
        (lambda v: .32 < v <= .48, .33),
        (lambda v: .48 < v < .52, .5),
        (lambda v: .52 <= v < .68, .625),
        (lambda v: .68 <= v < .84, .75),
        (lambda v: .84 <= v < 1, .875),
        (lambda v: v == 1, 1),
    ]
