from operator import itemgetter

from util import CONST
from util import create_devices
from util import print_devices_tabulated


def run() -> None:

    devices = create_devices(CONST.TOTAL_DEVICES, CONST.TOTAL_SUBNETS)

    # Printed devices as a table
    key = itemgetter('vendor', 'os', 'version')
    print_devices_tabulated(devices, key)
    

if __name__ == '__main__':
    run()