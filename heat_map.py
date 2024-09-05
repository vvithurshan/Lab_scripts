from re import X
import numpy as np, numpy.ma as ma
import os
import random
import sys
import matplotlib as mpl
# mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.gridspec import GridSpec
from textwrap import wrap
from matplotlib import rc  # This sometimes gives problems
import csv
from random import randint
import pandas as pd
import seaborn as sns  # Import Seaborn for heatmap plotting
import matplotlib.font_manager as fm

# Setting publication quality figure parameters
mpl.rcParams['axes.linewidth'] = 1.2
mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.major.width'] = 1.2
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1.2
mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.major.width'] = 1.2
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['ytick.minor.width'] = 1.2
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'
mpl.rcParams['font.size'] = 10
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['pdf.fonttype'] = 42  # Ensure compatibility with PDF fonts
mpl.rcParams['legend.frameon'] = False
legend_properties = {'weight': 'bold', 'size': 8}
axisl_properties = {'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'weight': 'bold'}
label_properties = {'weight': 'normal', 'size': 10}

# Create figure and add a custom axis
fig = plt.figure()
fig.set_size_inches(3.25, 3.25, forward=True)
ax1 = plt.Axes(fig, [0.115384615, 0.230769231, 0.769230769, 0.769230769])
fig.add_axes(ax1)

# Plotting the heatmap with explicit colorbar axis
ax = sns.heatmap(difference_matrix_thresholded, cmap='RdBu', center=0, annot=True, fmt=".2f",
                 cbar_kws={'label': 'Difference', 'shrink': 0.8}, ax=ax1)

# Access the colorbar object through the heatmap
colorbar = ax.collections[0].colorbar

# Set the colorbar label and tick label font sizes
colorbar.ax.set_ylabel('Difference', fontsize=12, fontweight='bold')  # Set label font size
# colorbar.ax.tick_params(labelsize=10)  # Set tick labels font size

# for the colorbar label

font_properties = fm.FontProperties(family='sans-serif',style='normal', size=10, weight='normal')

for label in colorbar.ax.get_yticklabels():
    label.set_fontproperties(font_properties)

# Define a formatter to align the colorbar tick labels
def format_ticks(x, pos):
    return f'{x: >6.2f}'  # Aligns values with fixed-width formatting (6 spaces, 2 decimal places)

# Apply the formatter to the colorbar ticks
colorbar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))

# Set labels for x and y axes
angstrom_symbol = '\u212B'  # for angstrom
ax1.set_ylabel(rf'$MSD ({angstrom_symbol}^2)$', fontsize=12, fontweight='bold')  # y-axis label
ax1.set_xlabel(f'Time (ns)', fontsize=12, fontweight='bold')  # x-axis label

# Set tick parameters
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))  # sets major tick spacing
ax1.set_xticklabels(ax1.get_xticks(), fontweight='bold', fontsize=10)
ax1.set_yticklabels(ax1.get_yticks(), fontweight='bold', fontsize=10)
ax1.tick_params(top=False, right=False)

# Set plot title
ax1.set_title(f'MSD of Linker', fontweight='bold')

# Save the figure
plt.savefig('msd.png', bbox_inches='tight', dpi=300)
plt.show()
