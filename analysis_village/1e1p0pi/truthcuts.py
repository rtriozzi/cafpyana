# io
import os
import sys

# computing
import math
import numpy
import pandas 

# my stuff
import helpers 

def kIsTrueFV(
  df
):   
  '''
    Check if reconstructed slice corresponds to a CC interaction.
  '''
  isFV        = helpers.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

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
  isNu        = df.slc.tmatch.idx >= 0
  isNuE       = abs(df.slc.truth.pdg) == 12
  isFV        = helpers.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

  return isNu & isNuE & isFV

def kIsNuMu(
  df
):   
  '''
    Check if reconstructed slice corresponds to a true muon neutrino in the FV.
  '''
  isNu        = df.slc.tmatch.idx >= 0
  isNuMu      = abs(df.slc.truth.pdg) == 14
  isFV        = helpers.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)

  return isNu & isNuMu & isFV

def kIsCC(
  df
):   
  '''
    Check if reconstructed slice corresponds to a CC interaction.
  '''
  isNu        = df.slc.tmatch.idx >= 0
  isCC        = df.slc.truth.iscc == 1

  return isNu & isCC

def kIsTherePi0(
  df
):   
  '''
    Check if reconstructed slice contains a Pi0 at the truth level.
  '''
  isNu        = df.slc.tmatch.idx >= 0
  hasPi0      = df.slc.truth.prim.pdg.apply(lambda pdgs: any(pdg == 111 for p in pdgs))
  
  return isNu & hasPi0

def kIsSignal(
  df
):   
  '''
    Check if reconstructed slice contains a Pi0 at the truth level.
  '''
  isNu         = df.slc.tmatch.idx >= 0
  isNuE        = abs(df.slc.truth.pdg) == 12
  isCC         = df.slc.truth.iscc == 1
  isFV         = helpers.IsInFV(df.slc.truth.position.x, df.slc.truth.position.y, df.slc.truth.position.z)
  isNueCC      = isNu & isNuE & isCC & isFV
    
  isElectron   = df.slc.truth.ne_200MeV == 1 # primary electron with >200 MeV energy
  isProtons    = df.slc.truth.np_50MeV >= 1  # at least one proton with >50 MeV energy
  isNeutrons   = df.slc.truth.nn_0MeV >= 0   # any number of neutrons
  isPi0        = df.slc.truth.npi0 == 0      # no pi0s
  isPi         = df.slc.truth.npi_30MeV == 0 # no charged pions above 30 MeV (visibility threshold)
  isFinalState = isElectron & isProtons & isNeutrons & isPi0 & isPi

  return isNueCC & isFinalState