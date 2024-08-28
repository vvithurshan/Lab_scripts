import numpy as np
import MDAnalysis as mda 
import MDAnalysis.analysis as ana 
import MDAnalysis.analysis.distances
import sys 

'''
def CalcCutoffMatrix(seq1,seq2):
    cutoff = np.zeros((len(seq1),len(seq2)))
    print (cutoff.shape)
    for i in range(len(seq1)):
        if seq1==seq2:
            for j in range(i,len(seq1)):
                cutoff[i,j] = (siglist[AAlist.index(seq1[i])] + siglist[AAlist.index(seq1[j])])/2.0
                cutoff[j,i] = (siglist[AAlist.index(seq1[i])] + siglist[AAlist.index(seq1[j])])/2.0

        else:
            for j in range(len(seq2)):
                cutoff[i,j] = (siglist[AAlist.index(seq1[i])] + siglist[AAlist.index(seq2[j])])/2.0
    return cutoff 
'''

def CalcCutoffMatrix(seq1,seq2):
    cutoff = np.zeros((len(seq1),len(seq2)))
    print (cutoff.shape)
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            cutoff[i,j] = (siglist[AAlist.index(seq1[i])] + siglist[AAlist.index(seq2[j])])/2.0

    return cutoff

if (len(sys.argv[:])==1):
    print ("Usage: python contacts.py tra/j*.xtc top/*.pdb start stride stop")
    sys.exit()


traj = sys.argv[1]
top = sys.argv[2]
start = int(sys.argv[3])
stride = int(sys.argv[4])
stop = int(sys.argv[5])


global siglist, AAlist 
siglist = np.loadtxt('aminoacids_vdwdiameter.dat',usecols=1)
AAlist = list('ARNDCQEGHILKMFPSTWYVsbatcg')
univ = mda.Universe(top, traj)
natoms = len(univ.atoms)
nchain = len(univ.segments)
#nstep = int((len(univ.trajectory)-start)/stride + 1)
nstep = int((stop-start)/stride + 1)

ncomp = int(input("Please enter number of components in the simulation: "))
chains = np.zeros(ncomp,dtype=int)
res = np.zeros(ncomp,dtype=int)
seq = []
seqname = []
style = "serial"
for i in range(ncomp):
    chains[i] = int(input("Please enter number of chains of component %i: "%(i+1)))
    #seqname.append(input("Please enter name of the component %i: "%(i+1)))
    seqname.append(input("Please enter name of component: "))
    seq.append(open(seqname[i]+'.seq','r').read().strip())
    res[i] = int(len(seq[i]))
#for i in range(ncomp):
#    for j in range(i, ncomp):
for i in range(ncomp):
    for j in range(i, ncomp):
        #fout='1'+seqname[i]+seqname[j]+'contacts'
        countall = np.zeros((nstep, int(res[i]), int(res[j])))
        cutoff = CalcCutoffMatrix(seq[i],seq[j])*1.5
        print (cutoff)
        frame = start
        for ts in univ.trajectory[(start-1):stop:stride]:
#            if (frame%20==0):
            print(frame)
            for k in range(chains[i]):
                if i==j:
                    fout='1'+seqname[i]+seqname[j]+'contacts'
                    for l in range(k+1,chains[j]):
                        moli = univ.atoms.positions[k*res[i]:(k+1)*res[i],:]
                        molj = univ.atoms.positions[l*res[j]:(l+1)*res[j],:]
                        d = ana.distances.distance_array(moli, molj, box=univ.dimensions, backend=style)
                        countall[int((frame-start)/stride)] += (d<=cutoff)
                else: 
                    fout='1'+seqname[i]+seqname[j]+'contacts'
                    for l in range(chains[j]):
                        moli = univ.atoms.positions[k*res[i]:(k+1)*res[i],:]
                        molj = univ.atoms.positions[chains[i]*res[i]+l*res[j]:chains[i]*res[i]+(l+1)*res[j],:]
                        d = ana.distances.distance_array(moli, molj, box=univ.dimensions, backend=style)
                        countall[int((frame-start)/stride)] += (d<=cutoff)
            frame += 1*stride
        np.save(fout, countall)

