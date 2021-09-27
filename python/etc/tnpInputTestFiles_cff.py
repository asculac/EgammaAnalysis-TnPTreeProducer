import FWCore.ParameterSet.Config as cms

# Some miniAOD testfiles, about 1000 events copied to our eos storage
# (not running directly on datasets because they get moved around all the time and xrootd sucks)
filesMiniAOD_2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIAutumn18MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018A-17Sep2018-v2.root'),
}

filesMiniAOD_2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIFall17MiniAODv2-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017B-31Mar2018-v1.root'),
}

filesMiniAOD_2016 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer16MiniAODv3-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016B-17Jul2018_ver2-v1.root'),
}


# Some miniAOD UL testfiles, which are available now and hopefully don't get deleted too soon
filesMiniAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('/store/mc/RunIISummer20UL18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/260000/0071F930-6376-7A48-89F1-74E189BD3BFC.root'),
    'data' : cms.untracked.vstring('/store/data/Run2018A/EGamma/MINIAOD/12Nov2019_UL2018-v2/70000/EE793B27-C1ED-8F4B-A62B-F71617523537.root'),
}

filesMiniAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('/store/mc/RunIISummer20UL17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9_ext1-v1/40001/FF0B076A-AFB5-BE44-BE60-09DB7EB55881.root'),
    #'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017.root'),
}
filesMiniAOD_UL2016preVFP = {
    'mc' :   cms.untracked.vstring('/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/005A0B41-E01E-AC40-99FD-BB2D643BC8B9.root'),
    #'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('/store/data/Run2016B/SingleElectron/MINIAOD/21Feb2020_ver1_UL2016_HIPM-v1/60000/00238AF0-F14F-9342-B657-9CD09B277BC7.root'),
}
filesMiniAOD_UL2016postVFP = {
    'mc' :   cms.untracked.vstring('/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/002C4C40-22FD-B946-BAB6-ABC759082930.root'),
    #'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('/store/data/Run2016F/SingleElectron/MINIAOD/21Feb2020_UL2016-v1/230000/03B2CD37-F55B-B740-A435-D7C280B89FA4.root'),
}

# AOD UL testfiles
filesAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018-AOD.root'),
}

filesAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017-AOD.root'),
}
