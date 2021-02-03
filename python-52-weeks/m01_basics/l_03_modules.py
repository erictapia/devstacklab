from operator import itemgetter

from util.create_utils import CONST
from util.create_utils import create_devices
from util.create_utils import print_devices_tabulated


def run() -> None:

    devices = create_devices(CONST.TOTAL_DEVICES, CONST.TOTAL_SUBNETS)

    # Printed devices as a table
    key = itemgetter('vendor', 'os', 'version')
    print_devices_tabulated(devices, key)
    

if __name__ == '__main__':
    run()