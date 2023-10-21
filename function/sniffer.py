import time
from colorama import Fore
from colorama import Style
import scapy.all
from scapy.layers import http
import psutil
from prettytable import PrettyTable
import subprocess
import re

choice = "Y"
def get_current_mac(interface):
 try:
  output = subprocess.check_output(["ifconfig",interface])
  return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output)).group(0)
 except:
  pass