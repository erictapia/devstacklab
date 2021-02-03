from pprint import  pprint

device1_str = ' r3, cisco, catalyst 2960, ios '

# split - delimter passed is used to split the string into a list 
print('='*80)
device1 = device1_str.split(',')
print('device1 using split')
print('    ', device1)
print('='*80)

# strip - removes blank in beginning and end of the string
#  split
device1 = device1_str.strip().split(',')
print('device1 using strip split')
print('    ', device1)
print('='*80)

# replace blanks in the string
# split
device1 = device1_str.replace(' ', '').split(',')
print('device1 using replace split')
print('    ', device1)
print('='*80)

# For loop tokenizes the attributes, strips spaces, and appends to device list
device1 = list()

for attrb in device1_str.split(','):   # tokenize attributes
    device1.append( attrb.strip() )    # remove any spaces in the beginning and end

print('device1 using split and strip with for loop')
print('    ', device1)
print('='*80)

# Strip and split with a list comprehension
device1 = [ attrb.strip() for attrb in device1_str.split(',') ]
print('device1 using strip and split with list comprehension')
print('    ', device1)
print('='*80)

# Ignoring case

model = 'CSR1000V'

print('\n\nIGNORING CASE')
print('='*80)
if model == 'csr1000v':
    print(f'matched: {model}')
else:
    print(f"didn't match: {model}")

print('='*80)
if model.lower() == 'csr1000v':
    print(f'matched using lower(): {model}')
else:
    print(f"didn't match: {model}")

print('='*80)

# Finding substring
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"

index = version.find(expected_version)

if index >= 0:
    print(f'found version: {expected_version} at location {index}')
else:
    print(f'not found: {expected_version}')

print('='*80)

# Separting string components
version_info = version.split(',')
for version_info_part in version_info:
    print(f'version part: {version_info_part.strip()}')

print('='*80)

# Separting string components w/enumeration
version_info = version.split(',')
for part_no, version_info_part in enumerate(version_info):
    print(f'version part {part_no}: {version_info_part.strip()}')

print('='*80)



show_interface_stats = """
GigabitEthernet1
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor      25376    1529598       8242     494554
             Route cache          0          0          0          0
       Distributed cache     496298   60647894     673003  218461079
                   Total     521674   62177492     681245  218955633
GigabitEthernet2
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor         19       1140          0          0
             Route cache          0          0          0          0
       Distributed cache       6077     663304          0          0
                   Total       6096     664444          0          0
Interface GigabitEthernet3 is disabled
Loopback21
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          0          0
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          0          0
Loopback55
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          3        241
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          3        241
Loopback100
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0         43       2806
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0         43       2806
"""

interface_counters = dict()
total_line_offset = 5

sh_int_stats_lines = show_interface_stats.splitlines()

for index, stats_line in enumerate(sh_int_stats_lines):
    if stats_line.find('GigabitEthernet', 0) == 0: # Testing if current line is the interface line
        totals_line = sh_int_stats_lines[index + total_line_offset]  # Scrape totals line
        interface_counters[stats_line] = totals_line.split()[1:] # split and assign list starting on index 1 to end
    
print('\n\n----- Interface Counters -------------------------------------------------------')
pprint(interface_counters)

print('='*80)

show_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.20.48             -   0050.56bb.e99c  ARPA   GigabitEthernet1
Internet  10.10.20.200           14   0050.56bb.8be2  ARPA   GigabitEthernet1
Internet  10.10.20.254            0   0896.ad9e.444c  ARPA   GigabitEthernet1
"""

arp_table = dict()

for arp_line in show_arp.splitlines():
    print( arp_line.split())
    if arp_line.lower().find('internet', 0) == 0:
        arp_table[arp_line[10:25].strip()] = arp_line[38:52]  # Slicing arp line to extract address and hardware addr

print('\n\n----- ARP Table ----------------------------------------------------------------')
pprint(arp_table)

print('='*80)