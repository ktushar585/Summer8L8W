 import argparse

parser=argparse.ArgumentParser(prog="cat",description="implement cat command",epilog="Hope you liked it")

parser.add_argument('file1',type=argparse.FileType('r'),nargs=2)
args=parser.parse_args()
with args.file1[0] as file:
    print (file.read())
with args.file1[1] as file:
    print (file.read())
