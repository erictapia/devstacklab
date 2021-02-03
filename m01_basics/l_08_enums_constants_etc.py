from util.create_utils import create_devices
from util.vendor import Vendor, VendorEnumInt, VendorEnumStr

devices = create_devices()

# Device Dict
# device['vendor']  = vendor
# device['os']      = os
# device['version'] = version
# device['name']    = f'{site}.{dist_frame}.{vendor}.{os}.{suffix}'
# device['ip']      = ip
for device in devices:
    if Vendor.CISCO == device['vendor']:
        print(f'\n{VendorEnumStr.CISCO.value} : {device}')
    
    if VendorEnumStr.JUNIPER.value == device['vendor']:
        print(f'\n{VendorEnumStr.JUNIPER.value}: {device}')
