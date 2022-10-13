import sys
import os

import argparse
from multiprocessing import Process
sys.path.append("telemanom/")
from telemanom import *

#parser = argparse.ArgumentParser(description='Experimenting Interface')
#parser.add_argument('-b', '--base_type', default="LSTM", required=False)
#args = parser.parse_args()

if "LSTM" == "LSTM":
    os.popen("cp lstm_base_config.yaml telemanom/config.yaml")
    print(os.getcwd())
    os.chdir('telemanom')
    exec(open("example.py").read())