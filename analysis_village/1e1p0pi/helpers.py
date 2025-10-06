import os
import sys

import math
import numpy
import pandas 

def IsInFV(
  x, y, z
):
  '''
    Check if 3D coordinate is within FV.
  '''
  return (( ((x < -61.94 - 25) & (x > -358.49 + 25)) | ((x >  61.94 + 25) & (x <  358.49 - 25)) ) &
          ( ((y> -181.86 + 25) & (y < 134.96 - 25)) & ((z > -894.95 + 30) & (z < 894.95 - 50)) )) # cm