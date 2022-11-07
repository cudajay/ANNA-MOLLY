import sys
print(sys.path)
from telemanom.detector import Detector
import argparse
import sys
import time

parser = argparse.ArgumentParser(description='Parse path to anomaly labels if provided.')
parser.add_argument('-l', '--labels_path', default=None, required=False)
parser.add_argument('-b', '--base_type', default="LSTM", required=False)
args = parser.parse_args()
if __name__ == '__main__':
    detector = Detector(labels_path=args.labels_path)
    starttime = time.time()
    detector.run_parallel()
    print("Total time elapsed: ", time.time() -  starttime)
    #detector.run_parallel()
