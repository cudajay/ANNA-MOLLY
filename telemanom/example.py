import sys
print(sys.path)
from detector import Detector
import argparse
import sys

parser = argparse.ArgumentParser(description='Parse path to anomaly labels if provided.')
parser.add_argument('-l', '--labels_path', default=None, required=False)
parser.add_argument('-b', '--base_type', default="LSTM", required=False)
args = parser.parse_args()
if __name__ == '__main__':
    detector = Detector(labels_path=args.labels_path)
    detector.run()