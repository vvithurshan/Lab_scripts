import MDAnalysis as mda
import numpy as np
import sys

u = mda.Universe(sys.argv[1], sys.argv[2])

n_atoms = len(u.atoms)
n_frames = len(u.trajectory)

positions = np.zeros((n_frames, n_atoms, 3))
print(positions.shape)

for i, ts in enumerate(u.trajectory):
    if i % 50 == 0:
        print(i)
    positions[i] = u.atoms.positions

print("Positions array shape: ", positions.shape)
np.save('positions_all_frames.npy', positions)
#positions = np.load('positions.npy')

def calculate_msd(positions, n_steps, n_particles):
    """
    Calculate the mean squared displacement (MSD) from a trajectory.

    :param positions: numpy array of shape (n_steps, n_particles, 3)
                      containing the positions of particles at each time step.
    :return: msd: numpy array containing the MSD as a function of time.
    """
#    n_steps, n_particles, _ = positions.shape
    msd = np.zeros(n_steps)

    # Loop over all time origins
    for t0 in range(n_steps):
        if t0 % 5 == 0:
            print(t0)
        # Displacements for each particle at each time step
        displacements = positions[t0:] - positions[t0]
        squared_displacements = np.sum(displacements**2, axis=2)  # Sum over x, y, z
        mean_squared_displacements = np.mean(squared_displacements, axis=1)  # Mean over particles
        msd[:n_steps-t0] += mean_squared_displacements

    # Normalize by the number of time origins
    for t0 in range(n_steps):
        msd[t0] /= (n_steps - t0)

    return msd


def calculate_msd2(positions, n_steps, n_particles):
    """
    Calculate the mean squared displacement (MSD) from a trajectory.

    :param positions: numpy array of shape (n_steps, n_particles, 3)
                      containing the positions of particles at each time step.
    :return: msd: numpy array containing the MSD as a function of time.
    """
#    n_steps, n_particles, _ = positions.shape
#    msd = np.zeros(n_steps)

    # Displacements for each particle at each time step
    displacements = positions - positions[0]
    squared_displacements = np.sum(displacements**2, axis=2)  # Sum over x, y, z
    msd = np.mean(squared_displacements, axis = 1)

    print('returning msd')
    return msd


msd = calculate_msd2(positions, n_frames, n_atoms)

np.save('msd_all_frames.npy', msd)
