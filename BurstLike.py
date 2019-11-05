from UFFO_Burst_func import *
import sys, os
import glob

infiles = sorted(glob.glob("*.txt"))
#print sorted(infiles)

#CopyTo4Dig(sys.argv[1], sys.argv[2])

#readTXT(sys.argv[1])

BurstLike(infiles)
