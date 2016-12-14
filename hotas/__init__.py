import re

from pywinusb import hid
import raildriver
import toolz

from hotas import sim
from hotas import usb


sim_handlers = {
    'RSC\.KentHighSpeed': sim.Class375Handler,

    'Thomson\.Class170Pack01': sim.Class170_171Handler,
}


class Hotas:

    hid = None

    raildriver = None
    raildriver_listener = None

    running = False

    sim = None
    usb = None

    def main(self):
        self.raildriver = raildriver.RailDriver()
        self.raildriver_listener = raildriver.events.Listener(self.raildriver, interval=0.1)
        self.raildriver_listener.on_loconame_change(self.bind_loco)
        self.raildriver_listener.start()
        self.bind_loco()

        self.usb = usb.ThrustmasterTFlightHotasX
        self.hid = hid.HidDeviceFilter(product_id=0xb108, vendor_id=0x044f).get_devices()[0]
        self.hid.open()
        self.hid.set_raw_data_handler(self.input_handler)

        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.hid.close()
        except Exception:
            self.hid.close()
            raise

    def bind_loco(self):
        loco_name = self.raildriver.get_loco_name()
        if loco_name is not None:
            self.running = True

            sim_handler_matches = toolz.dicttoolz.keyfilter(
                lambda k: re.compile('^{}'.format(k)).search('{}.{}.{}'.format(*loco_name)) is not None, sim_handlers)
            sim_handler_class = list(sim_handler_matches.values())[0] if sim_handler_matches else sim.BaseHandler

            self.sim = sim_handler_class(self.raildriver)
        else:
            self.running = False
            self.sim = None

    def input_handler(self, raw_input):
        if not self.running:
            return
        value = self.usb.handle_raw(raw_input)
        self.sim.handle(value)


def __main__():
    Hotas().main()


if __name__ == '__main__':
    __main__()
