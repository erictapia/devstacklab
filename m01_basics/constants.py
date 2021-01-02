# Defining Constants
DISTRIBUTION_FRAMES = ['MDF', 'IDF1', 'IDF2', 'IDF3', 'IDF4']
SITES = ['LACA', 'DATX', 'NYNY']

# 'vendor': { 'os': [versions] }
VENDORS = {
    'Cisco': {
        'ios': ['15.8(3)'],
        'iosxe': ['16.11.01b', '16.12.3', '17.02.01r'],
        'iosxr': ['6.3.1', '6.6.2'],
        'nxos': ['7.3.0', '9.2.3'],
        'asav': ['9.12.2']
    },
    'Juniper': {
        'junos': ['19.4R1.10', '18.3.R1.9', '18.2R1.9', '18.1R3-S5', '18.1R2']
    },
    'Arista': {
        'eos': ['4.23.6M', '4.24.3M', '4.25.1F']
    }
}

TOTAL_DEVICES = 10