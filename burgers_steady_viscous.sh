#! /bin/bash
#
python3 burgers_steady_viscous.py > burgers_steady_viscous.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit
fi
#
echo "Normal end of execution."
