import os
import sys

import math
import numpy
import pandas 

import CC1eNp0pi_Helpers as helper

def kIsTrueFV(
  df
):   
  '''
    Check if reconstructed slice corresponds to a CC interaction.
  '''
  isFV        = helper.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

  return isFV

def kIsNu(
  df
):   
  '''
    Check if reconstructed slice corresponds to a true neutrino.
  '''
  isNu        = df.slc.tmatch.idx >= 0

  return isNu
  
def kIsNuE(
  df
):   
  '''
    Check if reconstructed slice corresponds to a true electron neutrino in the FV.
  '''
  # isNeutrino  = df.slc.truth.index >= 0
  isNuE       = abs(df.slc.truth.pdg) == 12
  isFV        = helper.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

  return isNuE & isFV

def kIsNuMu(
  df
):   
  '''
    Check if reconstructed slice corresponds to a true muon neutrino in the FV.
  '''
  # isNeutrino  = df.slc.truth.index >= 0
  isNuMu      = abs(df.slc.truth.pdg) == 14
  isFV        = helper.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

  return isNuMu & isFV

def kIsCC(
  df
):   
  '''
    Check if reconstructed slice corresponds to a CC interaction.
  '''
  isCC        = df.slc.truth.iscc == 1

  return isCC

def kIsTherePi0(
  df
):   
  '''
    Check if reconstructed slice contains a Pi0 at the truth level.
  '''
  hasPi0      = df.slc.truth.prim.pdg.apply(lambda pdgs: any(pdg == 111 for p in pdgs))
  
  return hasPi0