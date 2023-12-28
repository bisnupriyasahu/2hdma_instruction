import FWCore.ParameterSet.Config as cms

# externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
#                                      args = cms.vstring('/hdfs/store/user/ms/gridPacks_2HDM/monoH_gridpacks/ggProduction/2HDMa_gg_sinp_0p35_tanb_0p5_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
#                                      nEvents = cms.untracked.uint32(5000),
#                                      numberOfParameters = cms.uint32(1),
#                                      outputFile = cms.string('cmsgrid_final.lhe'),
#                                      scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
#                                  )
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/monoHiggs/2HDMa/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_150_MH2_200_MHC_200_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
                                     nEvents = cms.untracked.uint32(5000),
                                     numberOfParameters = cms.uint32(1),
                                     outputFile = cms.string('cmsgrid_final.lhe'),
                                     scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
                                 )

# Link to cards:
# https://github.com/cms-sw/genproductions/tree/4e6dda7ecc882f106135d5a33c602f53bc4843a9/bin/MadGraph5_aMCatNLO/cards/production/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/Zprime_A0h_A0chichi_MZp600_MA0300
pythia8PSweightsSettingsBlock = cms.PSet(
    pythia8PSweightsSettings = cms.vstring(
        'UncertaintyBands:doVariations = on',
# 3 sets of variations for ISR&FSR up/down
# Reduced sqrt(2)/(1/sqrt(2)), Default 2/0.5 and Conservative 4/0.25 variations
# 32 decorrelated variations of muR and non-singular terms (cNS) for each branching type
        'UncertaintyBands:List = {\
isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,\
isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,\
isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,\
fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,\
fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,\
fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,\
fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,\
fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,\
fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,\
fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,\
fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,\
fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,\
fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,\
fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,\
fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,\
fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,\
fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,\
fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,\
fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,\
isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,\
isr_G2GG_muR_up isr:G2GG:muRfac=2.0,\
isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,\
isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,\
isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,\
isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,\
isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,\
isr_X2XG_muR_up isr:X2XG:muRfac=2.0,\
isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,\
isr_G2GG_cNS_up isr:G2GG:cNS=2.0,\
isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,\
isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,\
isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,\
isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,\
isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,\
isr_X2XG_cNS_up isr:X2XG:cNS=2.0}',
        
        'UncertaintyBands:nFlavQ = 4', # define X=bottom/top in X2XG variations
        'UncertaintyBands:MPIshowers = on',
        'UncertaintyBands:overSampleFSR = 10.0',
        'UncertaintyBands:overSampleISR = 10.0',
        'UncertaintyBands:FSRpTmin2Fac = 20',
        'UncertaintyBands:ISRpTmin2Fac = 1'
        )
)

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
#from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
#from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CP5SettingsBlock,
                             pythia8PSweightsSettingsBlock,
                             processParameters = cms.vstring(
                                 'SLHA:useDecayTable = off',  # Use pythia8s own decay mode instead of decays defined in LH accord
                                 '25:m0 = 125.0',
                                 '25:onMode = off',
                                 '25:onIfMatch = 15 -15'
                            ),
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                                         'pythia8CP5Settings',
                                                         'pythia8PSweightsSettings',
                                                         'processParameters'
                                                     )
                         )
                     )

ProductionFilterSequence = cms.Sequence(generator)


# Link to generator fragment:
# https://raw.githubusercontent.com/cms-sw/genproductions/a910901267ec5e724fec5a81c853082c89d58a16/python/ThirteenTeV/monoHiggs/pythia8_hadronizer_nomatching_Htautau_cff.py
