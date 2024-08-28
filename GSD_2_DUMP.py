import numpy as np
import gsd.hoomd
import sys
import os

input_path = os.path.abspath(sys.argv[1])

os.makedirs('dumpTraj', exist_ok = True)

os.chdir('dumpTraj')

traj = gsd.hoomd.open(input_path)
#traj = gsd.hoomd.open("../converted.gsd")
timesteps = np.array([s.configuration.step for s in traj], dtype=np.int64)
interval_tsteps = traj[1].configuration.step - traj[0].configuration.step
num_rigid_bodies = int(input('How many rigid bodies are there in your system? '))
for frames in np.arange(1000,len(traj),50):
    if (frames%50==0):
       print(frames)

    s = traj[int(frames)]
    f= open('dump.traj.'+str(int(frames*interval_tsteps)),'w')

    f.write('ITEM: TIMESTEP\n')
    f.write('%d \n' % s.configuration.step)
    f.write('ITEM: NUMBER OF ATOMS \n')
    f.write('%d \n' % (s.particles.N-num_rigid_bodies))
    f.write('ITEM: BOX BOUNDS pp pp pp \n')
    f.write('%f %f \n' % (-s.configuration.box[0]/2, s.configuration.box[0]/2))
    f.write('%f %f \n' % (-s.configuration.box[1]/2, s.configuration.box[1]/2))
    f.write('%f %f \n' % (-s.configuration.box[2]/2, s.configuration.box[2]/2))
    #f.write('ITEM: ATOMS id mol type q mass x y z ix iy iz \n')
    f.write('ITEM: ATOMS id type x y z ix iy iz \n')
    for i in np.arange(num_rigid_bodies,s.particles.N):
        #f.write('%d %d %d %.8f %.8f %.8f %.8f %.8f %d %d %d \n' % (i+1, 1, int(s.particles.types[0]), s.particles.charge[i], s.particles.mass[i], s.particles.position[i,:][0], s.particles.position[i,:][1], s.particles.position[i,:][2], s.particles.image[i,:][0], s.particles.image[i,:][1], s.particles.image[i,:][2])) 
        f.write('%d %d %.8f %.8f %.8f %d %d %d \n' % (i+1, int(s.particles.types[s.particles.typeid[i]]), s.particles.position[i,:][0], s.particles.position[i,:][1], s.particles.position[i,:][2], s.particles.image[i,:][0], s.particles.image[i,:][1], s.particles.image[i,:][2]))

    f.close()


#os.system("rm -rf dump.traj.0")
os.system("ls -v dump.traj.* | xargs cat > dump.lammpsdump && rm -rf dump.traj.*")
os.system("cp dump.lammpsdump ../ && cd ../ && rm -rf dumpTraj")
