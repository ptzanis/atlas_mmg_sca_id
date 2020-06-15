export PYTHONPATH=PyUAF/:$PYTHONPATH
export LD_LIBRARY_PATH=PyUAF/:$LD_LIBRARY_PATH
SCRIPT=client.py
/usr/bin/python $SCRIPT -sector $1

