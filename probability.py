import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (replace with your actual data)

# Calculate the histogram
hist, bins = np.histogram(Rg, bins=20, density=True)

# Calculate bin widths
bin_widths = np.diff(bins)

# Normalize the histogram to get the probability function
probability = hist * bin_widths
bin_midpoints = (bins[:-1] + bins[1:]) / 2
# Plot the probability function
# plt.bar(bins[:-1], probability, width=bin_widths, align='edge', edgecolor='black')
plt.plot(bin_midpoints, probability, marker='o', linestyle='-')
# Set labels and title
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Probability Function')

# Show the plot
plt.show()
