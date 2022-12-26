# A short and sweet script to test communication with a single roboclaw motor controller.
# usage 
#   $ python roboclawtest.py 128

from __future__ import absolute_import
import sys
from os import path
# need to add the roboclaw.py file in the path
sys.path.append(path.join(path.expanduser('~'), 'pi_ws/src/osr_code/ROS/osr/src'))
# pylint: disable=wrong-import-position, import-error
from roboclaw import Roboclaw

if __name__ == "__main__":
    address = int(sys.argv[1])
    roboclaw = Roboclaw("/dev/serial0", 115200)
    roboclaw.Open()
    print(roboclaw.ReadVersion(address))
    print(roboclaw.ReadEncM1(address))
