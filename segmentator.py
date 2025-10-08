from os import system
import subnet_maker
import socket
import sys
from zipfile import ZipFile
import os

print(r"""
  _________                                    __          __                
 /   _____/ ____   ____   _____   ____   _____/  |______ _/  |_  ___________ 
 \_____  \_/ __ \ / ___\ /     \_/ __ \ /    \   __\__  \\   __\/  _ \_  __ \
 /        \  ___// /_/  >  Y Y  \  ___/|   |  \  |  / __ \|  | (  <_> )  | \/
/_______  /\___  >___  /|__|_|  /\___  >___|  /__| (____  /__|  \____/|__|   
        \/     \/_____/       \/     \/     \/          \/                   
""")

print ("Mass mode by default. Target scanner. Check 19 for single mode.")
print ("----------------------------")

print('0. Extract ips and domains from multiple files and combine. File.zip')
print('1. Count and clean duplicates')
print('2. Validate and count assets')
print('3. Fping enviroment')
print('4. Masscan pinged')
print('5. Convert masscan results to csv')
print('6. Convert masscan results to nmap')
print('7. Run nmap to scan from masscan results')
print ('8 Merge results for nmap scan')
print('9. Visualise the nmap results to html)')
print('10. Get shodan results)')


print ("----------------------------")
print ("Single scan mode. Set target")
print ('19. Scan single url')
print ('20. Scan single api key')
print ('21. Scan single email')
print ("----------------------------")


#todo
#print ('201. Detect technology using wappalyzer' )
#print ('202. Make screenshots of web services' )
#print ('203. Collect titles' )
#print ('204. Run CMSmap')

print ("Massscan scan mode")
print ('205. Run Wpscan mass')
print ('206. Run Nuclei mass')
print ('207.' 'Run SSLscan mass')

print ("----------------------------")
print ("Single scan mode")
print ('208.' 'Run Wapiti single |Web Scanner')
print ('209.' 'Run Nikto single | Web Scanner')
print ('210.' 'Run Amass single | Subdomain sanner')


print ("----------------------------")
print ("Service")
print('100. Cleanup')
print ("----------------------------")




#remove from zip malicious files

#menu
while True:
    key = int(input('Input your choice: '))

    if key == 0:
        from zipfile import ZipFile
        zf = ZipFile('file.zip', 'r')
        zf.extractall('extracted')
        zf.close()



#combine all files in one

        import time, glob, shutil

        outfilename = 'combined.txt'


        with open(outfilename, 'wb') as outfile:

#add new lines for each file

            for filename in glob.glob('extracted/*.*'):
                with open(filename, 'a') as f:
                    f.write('\n')

#combine files
                if filename == outfilename:
                    # don't want to copy the output into the output
                    continue
                with open(filename, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)
        print ("All extracted files combined to combined.txt")
        num_lines = sum(1 for line in open('combined.txt'))
        print ("Amount of extracted valid assets:", num_lines)


#count and clean duplicates
    if key == 1:
            with open('combined.txt') as result:
                uniqlines = set(result.readlines())
                with open('cleaned_from_duplicates.txt', 'w') as rmdup:
                    rmdup.writelines(set(uniqlines))
            print ("Duplicates removed")

            # run ip and domain validator
    if key == 2:
        import ip_grab

        with open('cleaned_from_duplicates.txt') as result:
            uniqlines = set(result.readlines())
            with open('cleaned_from_duplicates_domains.txt', 'w') as rmdup:
                rmdup.writelines(set(uniqlines))

        num_lines = sum(1 for line in open('cleaned_from_duplicates_domains.txt'))
        print ("Amount of extracted valid assets:", num_lines)

    if key == 3:
            system("fping  -a < cleaned_from_duplicates_domains.txt > pingedips.txt") #fping targets from final_list

            file = open("pingedips.txt", "r")
            line_count = 0
            for line in file:
                if line != "\n":
                    line_count += 1
                    print (line)
            file.close()

            print(str(line_count) + ' IPS are alive')

    elif key == 4:

        import socket


        def writerx(a):
            xfile = open("ips_from_domains.txt", "a")
            xfile.write("\n")
            xfile.write(str(a))
            xfile.write("\n")
            xfile.close()


        liner = open("pingedips.txt", "r");

        for a in liner.readlines():
            # print(a)
            cleaned = a.strip()

            # try to get hostname of domain
            try:
                addr1 = socket.gethostbyname(cleaned)
                # print (addr1)
                # print (a)
                writerx(addr1)



            except:
                # print ("Bad domain")
                pass
        system("sudo masscan -iL ips_from_domains.txt --banners --source-port 61000 -p22,443,80,3389,21,8000,8080,27017,27018,20019,9200,3306,445  -oJ masscan_result.json --wait 0")
        system ("sleep 10")
        system("sudo masscan -iL ips_from_domains.txt --banners --source-port 61000 -p22,443,80,3389,21,8000,8080,27017,27018,20019,9200,3306,445  -oX scanRes.xml --wait 2")

    elif key == 5:
            system("python3 masscan_parser.py scanRes.xml -csv masscan_scan.csv > masscan_scan.csv")
            print ("masscan parsing finished, check masscan_scan.csv file")
            # masscan to csv convertor


    elif key == 6:
            system("python3 nmap_mass.py")

    elif key == 7:
            system("while IFS=' ' read -r host ports; do sudo timeout 20 nmap -T4 --min-parallelism 100 -n -vvv $host $ports --open -sC  -oX nmap_results/$host.xml ;done < scans.txt")
            print ("nmap scan finished")
            # nmap run from file


    elif key == 8:
            system("python3 nMapMerge.py -d nmap_results")
            print ("Results merget to one xml file")
            # nmap run from file


#nmap formatter

    elif key == 9:
            system("./nmap-formatter nMap_Merged.xml html > nmap_Results.html")
            print ("See fancy results in html from nmap. nmap_Results.html")
            # nmap run from file




#nmap formatter

    elif key == 10:
            system ("rm -rf shodanresults/resultsshodan.xml")
            system("./smap -iL pingedips.txt -oX shodanresults/resultsshodan.xml")
            print ("Shodan results exported to shodanresults")
            # nmap run from file



#subnet generate based on mask, with domains or with ips only

# mask generate 24 generate ips
    elif key == 101:
        subnet_maker.genmask24()
        print("IPS are generated")

#mask generate 23 generate ips
    elif key == 102:
        subnet_maker.genmask23()
        print("IPS are generated")


# mask generate 24 generate ips no domains
    elif key == 103:
        subnet_maker.genmaskipsonly24()
        print("IPS are generated")

# mask generate 23 generate ips no domains
    elif key == 104:
        subnet_maker.genmask23()
        print("IPS are generated")

        # mask generate 24 generate ips no domains
    elif key == 105:
        subnet_maker.genmask24()
      
      
      # wpscan json
    elif key == 205:
        system("./wpscan.sh")
        print("Wpscan. See results at wpscanresults direcotry")

  
# nuklei json
    elif key == 206:
        system("./nuclei --list pingedips.txt -json -o nuclei.json")
        print("Nuclei scan Results are at nuclei.json")



# mask generate 23 generate ips no domains
    elif key == 207:
        system("sslscan --targets=pingedips.txt --timeout=5 --xml=sslscan.xml")
        print("Sslscan scan resulsts are at sslscan.xml")


#single scan mode
    elif key == 19:
        target = input("Enter url: ")
        print(target +" Set as target")  



#single scan mode
    elif key == 20:
        apikey = input("Enter apikey: ")
        print(apikey +" Set as target")  



# scan wapiti
    elif key == 208:
        system("sudo wapiti -u "+target+" -f xml  -o "+directory+"/wapitiscanresults/results.xml")
        print("Wapiti scan resulsts are at wapitiscanresults/results.xml")
        
# scan nikto
    elif key == 209:
        print ("sudo nikto -h "+target+" -o "+directory+"/niktoscanresults/results.xml")
        system("sudo nikto -h "+target+" -o "+directory+"/niktoscanresults/results.xml")
        print("Nikto scan resulsts are at /niktoscanresults/results.xml")
        
        
# scan amass
    elif key == 210:
        system ("sudo "+directory+"/amass enum -passive -d "+target+" -src > "+directory+"/amassresults/results.txt")

        print("Amass scan results are at /amassresults/results.txt")
        system ("cat "+directory+"/amassresults/results.txt")
                        

    
#remove trash        
    elif key == 100:
        import os
        import shutil
        from pathlib import Path

        if key == 100:
            base_dir = Path(__file__).parent  # folder where script is located

            # Folders
            nmap_results = base_dir / "nmap_results"
            extracted = base_dir / "extracted"

            # Clean nmap_results
            if nmap_results.exists():
                for f in nmap_results.iterdir():
                    f.unlink() if f.is_file() else shutil.rmtree(f)
                print("Nmap results cleaned")

            # Remove txt/json/xml/html in root folder
            for ext in ("*.txt", "*.json", "*.xml", "*.html",".csv"):
                for f in base_dir.glob(ext):
                    f.unlink()
            print("All txt/json/xml/html files removed")

            # Remove extracted XML
            if extracted.exists():
                for f in extracted.glob("*.xml"):
                    f.unlink()
                print("Extracted XML files deleted")

            print("Cleanup complete.")

