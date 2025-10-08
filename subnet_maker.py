import os
from os import system
import sys
import ipaddress

#TODO integrate to menu
#generate 24 subnet from all ips and domains


def genmask24():
    with open("ips_from_domains.txt", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    filename= "ips_from_domains.txt"
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            system("python2 IPGenerator.py "+ line+"/24 >>generated_subnet.txt")
            print(line)
    print ("Under 24 subnet generated IPS and domains are placed to generated_subnet.txt")
    dupremover()


def genmask23():
    with open("ips_from_domains.txt", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    filename= "ips_from_domains.txt"
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            system("python2 IPGenerator.py "+ line+"/23 >>generated_subnet.txt")
            print(line)
    print ("Under 23 subnet generated IPS and domains are placed to generated_subnet.txt")
    dupremover()


# ips only 24 subnet
def genmaskipsonly24():
    with open("ips_from_domains.txt", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    filename= "pingedips.txt"
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            system("python2 IPGenerator.py "+ line+"/24 >>generated_subnet.txt")
            print(line)
    print ("Under 24 subnet generated IPS only are placed to generated_subnet.txt")
    dupremover()

# ips only 23 subnet
def genmaskipsonly23():
    with open("ips_from_domains.txt", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    filename= "pingedips.txt"
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            system("python2 IPGenerator.py "+ line+"/23 >>generated_subnet.txt")
            print(line)
    print ("Under 23 subnet generated IPS only are placed to generated_subnet.txt")
    dupremover()



#remove duplicates in subnets
def dupremover():

    file = open("generated_subnet.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print ("Amount of generated ips is without domains:",line_count)

    print("Delete duplicate")

    with open('generated_subnet.txt') as result:
        uniqlines = set(result.readlines())
        with open('generated_subnet.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

    num_lines = sum(1 for line in open('generated_subnet.txt'))
    print("Amount of extracted valid assets:", num_lines)
