import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd

sns.set(palette="colorblind")
sns.set_context("paper")

data = {'years':[2002, 2003, 2004, 2005, 2006, 2007, 
                 2008, 2009, 2010, 2011, 2012, 2013, 
                 2014, 2015, 2016, 2017, 2018],
        'chemistry':[986000, 1050000, 1040000, 1050000, 
                     1060000, 1050000, 1030000, 1050000, 
                     1010000, 874000, 898000, 794000, 
                     586000, 485000, 324000, 194000, 107000], 
         'chem_python':[351, 395, 462, 599, 809, 887, 
                        1250, 1410, 1900, 2630, 
                        3520, 4420, 5340, 6710, 
                        8120, 9930, 7750]}

df = pd.DataFrame(data)

fig, ax1 = plt.subplots(figsize=(5, 3))
ax1.plot(df['years'], df['chem_python'] / df['chemistry'] * 100, 's')
ax1.set_ylim([0, 8])
ax1.set_xlabel('Year')
ax1.set_ylabel('Chemistry publications/%')
ax1.set_xticks([2002, 2006, 2010, 2014, 2018])
#ax1.set_yticks([0, 0.05, .1])
plt.tight_layout()
plt.savefig('chem_data_py.pdf')
plt.close()