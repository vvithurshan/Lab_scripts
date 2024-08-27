import MDAnalysis as mda
import sys


num_args = len(sys.argv)
if num_args < 3:
  print('Usage')
  print(f'python3 {sys.argv[0]} input.pdb output.pdb')
  sys.exit()
u = mda.Universe(sys.argv[1])
u.atoms.write(sys.argv[2])
