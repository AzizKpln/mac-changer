import subprocess
import optparse 
import re
import os
import random
def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface Here \n\n")
    parser.add_option("-m","--mac_address",dest="mac_address",help="Mac Address Here  \n\n")
    parser.add_option("-o","--original_mac",dest="interface",help="Interface Here \n\n")
    
    parser.add_option("-r","--random",dest="interface_random",help="Interface Here")
    (options,arguments)=parser.parse_args()
    return options
def mac_changer(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])
    print("[+]Your Mac Address Changed To:"+mac_address)    
def old_mac_address(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    old_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if old_mac:
        return "[+]Your old mac address:"+str(old_mac.group(0))
    else:
        return "[-]Something Went Wrong"
def change_back(interface):
    dsmeg_results=subprocess.check_output(["dmesg"])
    change_original=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(dsmeg_results))
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",str(change_original.group(0))])
    subprocess.call(["ifconfig",interface,"up"])  
    return "[+]Your Original Mac Address:{}\n[+]Your Mac Address Changed To:{}".format(str(change_original.group(0)),str(change_original.group(0)))
def random_mac(interface_random):
    list3=list()
    list4=list()
    for i in range(0,6):
        list1=["a","b","c","d","e","f"]
        number_random=random.randint(0,9)
        letter_random=random.choice(list1)
        list3.append(number_random)
        list4.append(letter_random)
    random_mac_address=str(list3[0])+str(list4[0])+":"+str(list3[1])+str(list4[1])+":"+str(list3[2])+str(list4[2])+":"+str(list3[3])+str(list4[3])+":"+str(list3[4])+str(list4[4])+":"+str(list3[5])+str(list4[5])
    subprocess.call(["ifconfig",interface_random,"down"])
    subprocess.call(["ifconfig",interface_random,"hw","ether",random_mac_address])
    subprocess.call(["ifconfig",interface_random,"up"])  
    subprocess.check_output(["ifconfig",interface_random,"hw","ether",random_mac_address])
    print("[+]Random Mac Address:{}".format(random_mac_address))
    
        
options=get_arguments()
print("*"*40)
print("Thank You For Using This Program.\n")
print("Use The '-h' or '--help' Parameter To Get Help \v--Aziz Kaplan")
print("*"*40)
if options.interface and options.mac_address:
    print(old_mac_address(options.interface))
    mac_changer(options.interface,options.mac_address)
elif options.interface_random:
    print(old_mac_address(options.interface_random))
    try:
        random_mac(options.interface_random)
    except:
        subprocess.call(["python3","mac-changer.py","-r","{}".format(options.interface_random)])           
        
        
            
elif options.interface:
    print(old_mac_address(options.interface))
    print(change_back(options.interface))

    


