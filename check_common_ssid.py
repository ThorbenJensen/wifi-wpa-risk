"""Check if nearby wifi SSIDs have common names."""

import os
import re

# Read file of common SSIDs.
folder = os.path.dirname(os.path.realpath(__file__))
common_file = os.path.join(folder, 'common_ssids.txt')
with open(common_file) as f:
    common_ssids = f.read().splitlines()

# Get SSIDs of wifi hotsplots nearby.
bash_command = "nmcli dev wifi list"
scan = os.popen(bash_command).read()

# Extract SSIDs from bash return value.
split = scan.split('\n')
split = split[1:]


def get_ssid(string):
    """Get SSID from line of nwcli result."""
    search = re.search(' ([\S]+) ', string, re.IGNORECASE)
    if search:
        return search.group(1)
    return None


ssid_list = [get_ssid(i) for i in split if get_ssid(i) is not None]

# Check if SSIDs nearby are in list of common names. Report to user.
print("Checking if any of the following SSIDs is in common_list.")
print(ssid_list)
print()

matches = []
for ssid in ssid_list:
    if ssid in common_ssids:
        matches.append(ssid)

if len(matches):
    print("Some SSIDs have common name. Risky!")
    print(matches)
else:
    print("No SSID has common name.")
