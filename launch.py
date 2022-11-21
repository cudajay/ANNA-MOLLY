import sys
import os
import json
import argparse
from multiprocessing import Process
sys.path.append("telemanom/")
sys.path.append("model_utils/")


   

parser = argparse.ArgumentParser(description='Experimenting Interface')
parser.add_argument('-b', '--base_type', default="LSTM", required=False)
parser.add_argument('-p', '--parallel', default=False, required=False)
args = parser.parse_args()
f_path = os.path.join("telemanom", "config.yaml")

if os.path.exists(f_path):
    print("Deleting previous config file....")
    os.remove(f_path)
else:
    print("config not found!")
    
    
print(args)
if args.base_type == "LSTM":
    os.popen("cp lstm_base_config.yaml telemanom/config.yaml")
elif args.base_type == "CNN-1H":
    os.popen("cp cnn-1h_base_config.yaml telemanom/config.yaml")
elif args.base_type == "CNN-MH":
    os.popen("cp cnn-1h_base_config.yaml telemanom/config.yaml")
else:
    print("No proper config found")
    assert(False)
os.chdir('telemanom')
exec(open("example.py").read())