export PYTHONPATH=/afs/cern.ch/user/p/ptzanis/public/PyUAF:$PYTHONPATH
export LD_LIBRARY_PATH=/afs/cern.ch/user/p/ptzanis/public/PyUAF:$LD_LIBRARY_PATH
SCRIPT=client.py
echo $1
/usr/bin/python $SCRIPT -sector $1

