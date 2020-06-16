#!/usr/bin/python

import time
import datetime
import dcs_opc_ua
from pyuaf.util             import opcuastatuscodes, DateTime
import re
import sys
import argparse
import os 

parser = argparse.ArgumentParser(description='Production of SCA ID per Micromegas sector')

parser.add_argument("-sector", "--sector", type=str, 
   help="Insert Sector side and number  e.g. A12,C01,..")
args = vars(parser.parse_args())

#if not(re.compile("(A|C)(0[1-9]|1[0-6])").match(args['sector'])):
#	print("********   Wrong Sector ID | Please provide a valid sector ID: A01-16 or C01-16   ******** ")
#	sys.exit()

dcs_opc_ua.connect()

boardListFile = open('boards_list.txt','r')
prefix='.id'

sector=args['sector'] 

if not os.path.exists('../'+sector):
    os.makedirs('../'+sector)
    
mmfe8File=open('../'+sector+'/MMFE8_SCA_ID_'+sector+'.txt',"w+")
l1ddcFile=open('../'+sector+'/L1DDC_SCA_ID_'+sector+'.txt',"w+")
addcFile=open('../'+sector+'/ADDC_SCA_ID_'+sector+'.txt',"w+")

numberOfBoards=str(len(open('boards_list.txt').readlines()))

print "---> Looping over the "+numberOfBoards+" boards of Micromegas Sector "+sector

for i,board in enumerate(boardListFile):
    boardName=board.strip()
    board=board.strip()+prefix
    opcua_addr = dcs_opc_ua.addr(board)
    value = dcs_opc_ua.read ([opcua_addr])
    if(re.compile("MMFE8").match(board)):
       mmfe8File.write(boardName+' '+str(value.targets[0].data)+"\n")
    if(re.compile("ADDC").match(board)):
       addcFile.write(boardName+' '+str(value.targets[0].data)+"\n")
    if(re.compile("L1DDC").match(board)):
       l1ddcFile.write(boardName+' '+str(value.targets[0].data)+"\n")
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %d%%" % ('='*int(101*i/160), 101*i/160))
    sys.stdout.flush()
    time.sleep(0.01)

boardListFile.close()
mmfe8File.close()
addcFile.close()
l1ddcFile.close()

print "\n"
print "** The SCA ID files for MMFE8, L1DDC and ADDC boards are ready! Have fun!"


