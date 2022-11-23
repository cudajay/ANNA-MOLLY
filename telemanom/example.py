import sys
print(sys.path)
from telemanom.detector import Detector
import argparse
import sys
import time

parser = argparse.ArgumentParser(description='Parse path to anomaly labels if provided.')
parser.add_argument('-l', '--labels_path', default=None, required=False)
parser.add_argument('-b', '--base_type', default="LSTM", required=False)
parser.add_argument('-p', '--parallel', default=False, required=False)
parser.add_argument('-g', '--generate', default='', required=False)
args = parser.parse_args()
if __name__ == '__main__':
    detector = Detector(labels_path=args.labels_path)
    starttime = time.time()
    if args.parallel:
        detector.run_parallel()
    elif args.generate:
        detector.generate(args.generate)
    else:
        detector.run()
    print("Total time elapsed: ", time.time() -  starttime)
    #detector.run_parallel()
