import MDAnalysis as mda
import sys
import os

if len(sys.argv) == 1:
    print(f'python3 {sys.argv[0]} pdb_file')
    os.exit()

u = mda.Universe(sys.argv[1])
dna_seq = [residue.resname for residue in u.residues if residue.resname in ['ADE', 'GUA', 'THY', 'CYT']]

seq_dict = {
    'ADE' : 'a',
    'THY' : 't',
    'GUA' : 'g',
    'CYT' : 'c'
}
with open('dna_seq.txt', 'w') as f:
    for seq in dna_seq:
        f.write('b')
        f.write(seq_dict[seq])

f.close()
