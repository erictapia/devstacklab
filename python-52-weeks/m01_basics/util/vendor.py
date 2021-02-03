from enum import Enum

# Use class name and class variable
#       Vendor.CISCO
class Vendor:
    CISCO   = 'Cisco'
    JUNIPER = 'Juniper'
    ARISTA  = 'Arista'


# Use class and enum, which has 'name' and 'value' attributes
#       Vendor.CISCO.name or Vendor.CISCO.value
class VendorEnumInt(Enum):
    CISCO   = 1
    JUNIPER = 2
    ARISTA  = 3


# Use class and enum, which has 'name' and 'value' attributes
#       Vendor.CISCO.name or Vendor.CISCO.value
class VendorEnumStr(Enum):
    CISCO   = 'Cisco'
    JUNIPER = 'Juniper'
    ARISTA  = 'Arista'