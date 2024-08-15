import sys
import os
import MDAnalysis as mda

with open(sys.argv[1], 'r') as infile, open('corrected.pdb', 'w') as outfile:
    for line in infile:
        if line.startswith(('CRYST1', 'TITTLE', 'REMARK', 'HEADER')):
            outfile.write(line)
        else:
            new_line = line[0:16] + ' ' + line[17:]
            outfile.write(new_line)
