## Density calculation
```python 
python gsd_mc_density_calculation.py ../prod.gsd index.indx 500 1000 2000 1 1 ang   // bin start stop stride
```

## Contact map for Protein-DNA system
### Things to be done
  1. GSD to lammpstrj which does not have the coordinates of rigid bodies (GSD_2_DUMP.py).
  2. Get the PDB file without any rigid bodies (PDB_no_rigid.py)
  3. Get the protein and DNA sequence.
  4. Get npy array for prot-prot, prot-DNA, and DNA-DNA (contacts.py)
  5. Plot them.


## DSSP
source /project/klab-biophysics/software/codes/spack/share/spack/setup-env.sh

export DSSP=/cluster/medbow/project/klab-biophysics/software/codes/spack/opt/spack/linux-rhel9-zen4/gcc-13.2.0/dssp-3.1.4-umoikl6hxkc524sh5u5uh6qmvbe2aa6j/bin/mkdssp

gmx_mpi do_dssp -f topol.tpr.trr -s topol.tpr -sc

ptmetad_0 folder only
