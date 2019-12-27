# OS Project - Memory Management
#OS_CA_2_96243075
import sys


def report():
    print("------------------------------------------")
    print("Page Fault rate: {0.2f}".format((pf_count/count)))
    print("TLB Hit rate: {0.2f}".format((tlb_count/count)))


def convert_logical_to_physical(address):
    pass


''' Read file given from Argv
print(sys.argv)
file = open(sys.argv[1], "rt")
'''
try:
    file = open("addresses.txt", "rt")
except FileNotFoundError:
    print("File Not Found in current directory")


count = 0
tlb_count = 0
pf_count = 0
for line in file:
    count += 1
    print(convert_logical_to_physical(line))
report()
