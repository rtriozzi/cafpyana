import os
import sys

import math
import numpy
import pandas 

import CC1eNp0pi_Helpers as helper

ELECTRON_ENERGYCUT = 0.2

def kVertexInFV(
  df
):   
  '''
    Check if reconstructed vertex is within fiducial volume.
  '''
  return helper.IsInFV(df.slc.vertex.x, df.slc.vertex.y, df.slc.vertex.z)

def kNotClearCosmic(
  df
):   
  '''
    Check that the reconstructed slices is not tagged as a clear cosmic by Pandora.
  '''
  return ~df.slc.is_clear_cosmic

def kFlashMatch(
  df
):   
  '''
    Check that the slice is matched to an in-time flash.
  '''
  return (df.slc.barycenterFM.deltaZ >= 0) & (df.slc.barycenterFM.deltaZ <= 100) & (df.slc.barycenterFM.flashTime >= 0) & (df.slc.barycenterFM.flashTime <= 10)

def kLargestRecoShower_EnergyCut(
  df
):
  '''
    Identify the electron and cut on the calorimetric energy.
  '''
  idx = helper.kLargestRecoShowerIdx(df.slc)
  return df.slc.reco.pfp[idx].shw.plane[2].energy > ELECTRON_ENERGYCUT