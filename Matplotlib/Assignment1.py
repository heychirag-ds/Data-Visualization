'''
With dataset of hypothetical runs of Kohli, Rohit and Sehwag across 10 years:
Use:
Labels
Legends
Colors
Line styles
One custom style
import matplotlib.pyplot as plt
'''

import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
kohli = [1200, 1380, 1020, 1260, 1500, 1320, 1450, 1600, 1325, 1400]
rohit = [800,  950,  1130, 1100, 980,  1200, 1400, 1300, 1250, 1500]
sehwag = [1100, 1250, 980,  850,  700,  600,  450,  300,  200,  100]

# Use a custom style
print(plt.style.available)
plt.style.use("_classic_test_patch")

# Plot with custom styles
plt.plot(years, kohli, color="green", linestyle='-', marker='o', linewidth=2.5, label="Kohli")
plt.plot(years, rohit, color="blue", linestyle='--', marker='s', linewidth=2.5, label="Rohit Sharma")
plt.plot(years, sehwag, color="red", linestyle='-.', marker='^', linewidth=2.5, label="Sehwag")

# Labels and title
plt.xlabel("Year", fontsize=12)
plt.ylabel("Runs Scored", fontsize=12)
plt.title("Hypothetical Runs: Kohli vs Rohit vs Sehwag (2010–2019)", fontsize=14, fontweight='bold')

# Grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()