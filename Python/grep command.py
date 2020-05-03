import argparse

parser=argparse.ArgumentParser(description='grep command')

parser.add_argument('word',type=str,help='word to be searched')
parser.add_argument('file2',type=argparse.FileType('r'))
args=parser.parse_args()
with args.file2 as file1:
    mylist=file1.readlines()
for item in mylist:
    mylist2=item.split()
    for initem in mylist2:
        if args.word == initem:
            print(item)
