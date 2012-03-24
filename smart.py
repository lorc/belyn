import threading
import usb.core
import sys

CMD_NOP=0x80
CMD_TURN_OFF=0x81
CMD_TURN_ON=0x82
CMD_NEXT_STATE=0x83

class NoDevFoundError(Exception):
    pass

def get_interface():
    dev = usb.core.find(idVendor=0x0925, idProduct=0x9002)
    if not dev:
        raise NoDevFoundError()

    dev.set_configuration()
    cfg = dev[0]
    intf = cfg[(0,0)]
    return intf

def write_cmd(intf, cmd):
    if not intf:
        intf = get_interface()
    intf[1].write(chr(cmd))
    ret = intf[0].read(1,3000)
    return ret.tostring()

def turn_off(intf=None):
    write_cmd(intf, CMD_TURN_OFF)

def turn_on(intf=None):
    write_cmd(intf, CMD_TURN_ON)

def next_state(intf=None):
    write_cmd(intf, CMD_NEXT_STATE)

def set_state(state, intf=None):
    write_cmd(intf, state)

def get_state(intf=None):
    return ord(write_cmd(intf,CMD_NOP))

def main():
    intf = get_interface()
    print "current state: %X"%get_state(intf)
    if len(sys.argv) < 2:
        next_state(intf)
    else:
        if sys.argv[1] == "next":
            next_state(intf)
        elif sys.argv[1] == "on":
            turn_on(intf)
        elif sys.argv[1] == "off":
            turn_off(intf)
        elif sys.argv[1] == "set":
            set_state(int(sys.argv[2]),intf)
    print "new state: %X"%get_state(intf)

if __name__ == "__main__":
    main()
