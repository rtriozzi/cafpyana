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
          ( ((y> -181.86 + 25) & (y < 134.96 - 25)) & ((z > -894.95 + 30) & (z < 894.95 - 50)) ))

def kLargestRecoShowerIdx(slc):
  '''
    Find the index of the largest reconstructed shower in the slice.
  '''
  electronIdx = -1
  maxNHits = -1

  for i, pfp in enumerate(slc.reco.pfp):

      # use I2 or C, whichever has more hits
      bestPlaneIdx = 1 if pfp.shw.plane[1].nHits > pfp.shw.plane[2].nHits else 2

      if (pfp.shw.plane[bestPlaneIdx].nHits > maxNHits) & (pfp.trackScore <= 0.5) & (pfp.parent_is_primary):
          electronIdx = i
          maxNHits = pfp.shw.plane[bestPlaneIdx].nHits

  return electronIdx