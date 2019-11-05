import numpy as np
import matplotlib.pyplot as plt
import glob
import string
import os, sys
# Read txt file of UFFO-p SMT data
def readTXT(infileName):
	infile = np.loadtxt(infileName, dtype=int, delimiter=',')
	#print infile[0]
	return infile

def CopyTo4Dig(indir, outdir):
	infiles = glob.glob('%s/*.*' % indir)
	for infile in infiles:
		infile = infile.split('/')[-1]
		ext=infile.split('.')[-1]
		header = string.join(infile.split('.')[0].split('_')[:-1], "_")
		dig = int(infile.split('.')[0].split('_')[-1])
		new = ("%s_%04d" % (header, dig))
		#print new
		print ('cp %s %s/%s/%s.%s' % \
			(indir, infile, outdir, new, ext))
		
		os.system('cp %s/%s %s/%s.%s' % \
			(indir, infile, outdir, new, ext))

# BurstLike analysis
def BurstLike(infiles):
	# output data
	nOfHit = []
	#nOfHit_avg = 0
	#nOfHit_std = 0
	nOfHit_std = []


	for infile in infiles:
		smtEvt = readTXT(infile)
		print infile, "..."
		nOfHit.append(np.sum(smtEvt))
	nOfHit = np.array(nOfHit)


	nOfHit_std = (nOfHit - np.mean(nOfHit))/np.std(nOfHit)

	plt.plot(nOfHit_std)
	plt.savefig("nOfHit_std.pdf")
	#plt.show()

	checkList = []

	for i in range(len(nOfHit_std)-1):
		if nOfHit_std[i] > 1:
			if ((nOfHit_std[i] - nOfHit_std[i-1]) > 1) &\
			   ((nOfHit_std[i] - nOfHit_std[i+1]) > 1):
				print ("%dth frame need to check" % i)
				checkList.append(i)

	for j in checkList:
		fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize = (15, 5))

		img1 = readTXT(infiles[j-1])
		ax1.imshow(img1)

		img2 = readTXT(infiles[j])
		ax2.imshow(img2)

		img3 = readTXT(infiles[j+1])
		ax3.imshow(img3)

		#plt.show()
		plt.savefig("%04d.pdf" % j)
