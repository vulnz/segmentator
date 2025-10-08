import ipaddress
import re
import numpy

def get_ip_from_subnet(ip_subnet):

    ips= ipaddress.ip_network(ip_subnet)
    ip_list=[str(ip) for ip in ips]
    return ip_list


#subnet format is: 1.2.3.0/24, 1.2.3.0/12 , 1.1.1.1/32

filename= "testmask.txt"
with open(filename, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        try:
            subcleaner=get_ip_from_subnet(line)
            print(subcleaner)
            with open("output.txt", "a") as txt_file:
                for line in subcleaner:
                    txt_file.write("".join(line) + "\n")  # works with any number of elements in a line

            #TODO - write to file and clean array
        except:
            print ("error")
            pass
print ("IPS generated from Subnets and placed in generated_subnet")