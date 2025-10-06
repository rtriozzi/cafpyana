# io
import os
import sys

# computing
import math
import numpy
import pandas 

# my stuff
import helpers 

# global cuts
ELECTRON_ENERGY_CUT  = 0.2 # GeV
ELECTRON_DEDX_CUT    = 3.5 # MeV/cm
ELECTRON_ANGLE_CUT   = 10 # deg.
ELECTRON_CONVGAP_CUT = 5 # cm

def kCRTPMTVeto(
  df
):
  '''
    Reject events that don't have a contained in-time flash.
  '''
  return  df.crtpmt_veto == False
    
def kVertexInFV(
  df
):   
  '''
    Check if reconstructed vertex is within fiducial volume.
  '''
  return helpers.IsInFV(df.slc.vertex.x, df.slc.vertex.y, df.slc.vertex.z)

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
  return (df.slc.barycenterFM.deltaZ >= 0) & (df.slc.barycenterFM.deltaZ <= 100) & (df.slc.barycenterFM.flashTime >= 0) & (df.slc.barycenterFM.flashTime <= 10) # cm, us

def kTrigFlashMatch(
  df
):   
  '''
    Check that the slice is matched to an in-time flash.
  '''
  return (df.slc.barycenterFM.deltaZ_Trigger >= 0) & (df.slc.barycenterFM.deltaZ_Trigger <= 100) # cm
    
def kLargestRecoShower_EnergyCut(
  df
):
  '''
    Identify the electron and cut on the calorimetric energy.
  '''
  return df.electron_candidate.pfp.shw.plane.I2.energy > ELECTRON_ENERGY_CUT

def kLargestRecoShower_dEdxCut(
  df
):
  '''
    Identify the electron and cut on the calorimetric energy.
  '''
  return df.electron_candidate.pfp.shw.plane.I2.dEdx < ELECTRON_DEDX_CUT


def kLargestRecoShower_OpenAngleCut(
  df
):
  '''
    Identify the electron and cut on the calorimetric energy.
  '''
  return 180. * df.electron_candidate.pfp.shw.open_angle / math.pi < ELECTRON_ANGLE_CUT

def kLargestRecoShower_ConvGapCut(
  df
):
  '''
    Identify the electron and cut on the calorimetric energy.
  '''
  return df.electron_candidate.pfp.shw.conversion_gap < ELECTRON_CONVGAP_CUT