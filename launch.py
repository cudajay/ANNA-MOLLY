import sys
import os
import json
import argparse
from multiprocessing import Process
sys.path.append("telemanom/")
sys.path.append("model_utils/")


   

#parser = argparse.ArgumentParser(description='Experimenting Interface')
#parser.add_argument('-b', '--base_type', default="LSTM", required=False)
#args = parser.parse_args()
f_path = os.path.join("telemanom", "config.yaml")
if os.path.exists(f_path):
    print("Deleting previous config file....")
    os.remove(f_path)
else:
    print("config not found!")
    
if "LSTM" == "LSTM":
    os.popen("cp lstm_base_config.yaml telemanom/config.yaml")
    os.chdir('telemanom')
    exec(open("example.py").read())