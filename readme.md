  _________                                    __          __                
 /   _____/ ____   ____   _____   ____   _____/  |______ _/  |_  ___________ 
 \_____  \_/ __ \ / ___\ /     \_/ __ \ /    \   __\__  \\   __\/  _ \_  __ \
 /        \  ___// /_/  >  Y Y  \  ___/|   |  \  |  / __ \|  | (  <_> )  | \/
/_______  /\___  >___  /|__|_|  /\___  >___|  /__| (____  /__|  \____/|__|   
        \/     \/_____/       \/     \/     \/          \/                   


Quick features

Extract & combine files from file.zip (option 0).

Deduplicate & validate lists (options 1 / 2).

Ping live hosts with fping (option 3).

Masscan fast discovery + Nmap follow-up (options 4, 7).

Convert/merge and generate HTML visualization (options 5, 8, 9).

Batch web/tools: Nuclei, WPSCan, SSLScan, Wapiti, Nikto, Amass.

Cleanup routine to remove generated files (option 100).


> python3 segmentator.py
Input your choice: 0    # extract+combine
Input your choice: 1    # remove duplicates
Input your choice: 3    # fping -> pingedips.txt
Input your choice: 4    # masscan using ips_from_domains.txt
Input your choice: 5    # convert masscan -> csv
Input your choice: 7    # run nmap from scans.txt
Input your choice: 9    # generate HTML report



**Requirements:
**Parrot or Kali security os with preinstalled toools:
fping, nmap, nuclei, masscan.

**Running:
**pip install -r requirements
python segmentator.py
