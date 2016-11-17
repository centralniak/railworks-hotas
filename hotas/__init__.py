from pywinusb import hid
import raildriver

from hotas import sim
from hotas import usb


sim_handlers = {
    'RSC.KentHighSpeed': sim.Class375Handler,
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

        self.usb = usb.Hotas
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
            self.sim = sim_handlers.get('.'.join(loco_name[:2]), sim.BaseHandler)(self.raildriver)
        else:
            self.running = False
            self.sim = None

    def input_handler(self, raw_input):
        if not self.running:
            return
        value = self.usb.handle_raw(raw_input)
        self.sim.handle(value)


if __name__ == '__main__':
    Hotas().main()
