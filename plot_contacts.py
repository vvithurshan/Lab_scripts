# Author: Roshan M Regy
# EmailID: roshanm.regy@tamu.edu
import numpy as np 
import matplotlib.pyplot as plt 
import argparse
from matplotlib.colors import LinearSegmentedColormap

axd = plt.figure(figsize=[3,3],dpi=300).subplot_mosaic(
        """
        bAd
        .c.
        """,
        gridspec_kw = {
            "height_ratios": [3,1],
            "width_ratios" : [1,3,0.1],
            },
        )
parser = argparse.ArgumentParser()
parser.add_argument("-npy", type=str, required=True,help="numpy contact file")
parser.add_argument("-title",type=str, required=True,help="Title of plot")
parser.add_argument("-out",type=str,required=True,help="Name of output file")
args = parser.parse_args()

data = np.load(args.npy)
title = args.title
filename = args.out
tmean = data.mean(axis=0)
print (tmean.shape)
tickskip = 50
mainxticklocs = np.arange(0.5,tmean.shape[1]+0.5,int(tickskip/5))
sidexticklocs = np.arange(0.5,tmean.shape[1]+0.5,int(tickskip/5))
sidexticks = range(1,tmean.shape[1]+1,int(tickskip/5))
mainyticklocs = range(0,tmean.shape[0],tickskip)
sideyticklocs = np.arange(0.5,tmean.shape[0]+0.5,tickskip)
sideyticks = range(1,tmean.shape[0]+1,tickskip)

# custom color scheme
cvals = [0, 5, 10, 15, 20, 25]
colors = ['red', 'orangered', 'mediumblue', 'blue', 'gold', 'white']
norm = plt.Normalize(min(cvals), max(cvals), clip=True)
tuples = list(zip(map(norm, cvals), colors))
my_cmap = LinearSegmentedColormap.from_list('', tuples)


im = axd['A'].imshow(tmean, aspect='auto',origin='lower',cmap='gist_heat_r')
#im = axd['A'].imshow(tmean, aspect='auto',origin='lower',cmap=my_cmap)

axd['A'].set_xticks(mainxticklocs)
axd['A'].set_yticks(mainyticklocs)
axd['A'].set_xticklabels([])
axd['A'].set_yticklabels([])
axd['b'].plot(tmean.mean(axis=1),range(tmean.shape[0]),ls='--',lw=0.5,color='black')
axd['c'].plot(range(tmean.shape[1]),tmean.mean(axis=0),ls='--',lw=0.5,color='black')
axd['b'].set_yticks(sideyticklocs)
axd['b'].set_yticklabels(sideyticks)
#axd['c'].set_xticks(sidexticklocs)
#axd['c'].set_xticklabels(sidexticks)
axd['b'].set_ylabel('Residue no.',fontsize=7)
axd['c'].set_xlabel('Residue no.',fontsize=7)
#axd['b'].set_xlabel('Contact Probability',fontsize=7)
#axd['c'].set_ylabel('Contact Probability',fontsize=7)
axd['c'].set_xlim(0,tmean.shape[1])
axd['b'].set_ylim(0,tmean.shape[0])
axd['b'].xaxis.tick_top()
cb = plt.colorbar(im,cax=axd['d'])
cb.ax.tick_params(length=1,pad=0.5,labelsize=5)
cb.ax.set_ylabel('Contacts per chain per frame',fontsize=6)
for i in axd:
    axd[i].tick_params(length=2,pad=0.5,labelsize=4)
axd['A'].tick_params(length=3,pad=0.0,labelsize=0)
plt.subplots_adjust(wspace=0.1, hspace=0.1)
axd['A'].set_title(title,fontsize=7)
plt.savefig('ctmap_%s.png'%filename,bbox_inches='tight',dpi=300)
plt.show()
