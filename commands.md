## Density calculation
```python 
python gsd_mc_density_calculation.py ../prod.gsd index.indx 500 1000 2000 1 1 ang   // bin start stop stride
```

## Contact map for Protein-DNA system
### Things to be done
  1. GSD to lammpstrj which does not have the coordinates of rigid bodies (GSD_2_DUMP.py).
  2. Get the PDB file without any rigid bodies (PDB_no_rigid.py)
  3. Get the protein and DNA sequence.
  4. Get npy array for prot-prot, prot-DNA, and DNA-DNA.
  5. Plot them.

     
