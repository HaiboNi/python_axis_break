import numpy as np
import collections
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import csv
from numpy import *
import pandas as pd
from matplotlib import rc
# from load import *
### rcParams are the default parameters for matplotlib
import matplotlib as mpl
rc('mathtext',default='regular')

fonts = 18;
fonts_title = 18
leng_fontsize = 18
mpl.rcParams['font.size'] = fonts
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['axes.labelsize'] = fonts
mpl.rcParams['xtick.labelsize'] = fonts
mpl.rcParams['ytick.labelsize'] = fonts
mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['ytick.major.pad']='10'
mpl.rcParams['xtick.major.pad']='10'
mpl.rcParams['xtick.major.size']=5
mpl.rcParams['ytick.major.size']=5
mpl.rcParams['xtick.minor.size']= 0
mpl.rcParams['ytick.minor.size']= 0

mpl.rcParams['xtick.major.width']=1.5
mpl.rcParams['ytick.major.width']=1.5



dcon = np.log10(np.array([0.3, 1, 3, 10, 30, 100]))

force = [8.330626015244283,  8.173934774459575,  9.856303886042731, 10.856428839185304, 30.877670873422463, 12.975134324628263]  # expri Schotten et al., 2007

fig = plt.figure(figsize=(7,4))
num_row = 2;
num_col = 1;

ratio = 4;

gs1 = gridspec.GridSpec(num_row,num_col, height_ratios = (1/ratio,1))


ax = plt.subplot(gs1[0,0]);

ax2 = plt.subplot(gs1[1,0],sharex=ax)



# f, (ax, ax2) = plt.subplots(1, 2, sharey=True)
ax.plot(dcon, force, 'ks-',ms=10)
ax2.plot(dcon, force, 'ks-',ms=10)

# ax.set_xscale('log')

# ax.set_xlim(-1e-7,1e-7)  # outliers only
# ax2.set_xlim(5e-7,2e-4)  # most of the data

# ax2.set_xscale('log')

ax.set_ylabel('Force (mN/mm$^2$)')
ax.yaxis.set_label_coords(-1, 0.5)
# ax.set_xticks([0])

ax.set_ylim(27.5,32)
ax.set_yticks([28,30,32])
ax2.set_ylim(7.5,14.5)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_visible(False)
# ax_twin.spines['right'].set_visible(False)
# ax_twin.yaxis.set_ticks_position('none')
# ax_twin.yaxis.set_ticks_position('none')
# ax_twin.get_yaxis().set_ticks([])

# ax.set_ylim(8,14)

# ax2.spines['left'].set_visible(False)
# ax.xaxis.tick_top()
# ax2_twin.yaxis.set_ticks_position('none')

ax2.spines['right'].set_visible(False)
# ax2_twin.spines['left'].set_visible(False)
# ax2_twin.yaxis.set_ticks_position('right')
# ax2_twin.set_ylabel('$\Delta[Ca^{2+}]_i$ ($\mu$M)',color='tab:blue')
# ax2_twin.yaxis.set_tick_params(color='tab:blue',labelcolor='tab:blue')
# ax2_twin.spines['right'].set_color('tab:blue')
# ax2.yaxis.set_ticks_position('right')
# ax2.yaxis.set_visible(False)

ax2.set_xlabel( 'AVE0118 (M)')

ax2.set_ylabel('Y label ($a^2$)',weight='bold')
ax2.yaxis.set_label_coords(-0.12, 0.75)
# ax2_twin.set_ylim(0.25,0.43)
# ax_twin.set_ylim(0.25,0.43)

d = .03  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False, lw=2)
# ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((- d, + d), (-d*ratio, +d*ratio), **kwargs)  # top-right diagonal
# ax2.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal
kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False, lw =2)
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)        # top-left diagonal


for axs in [ax, ax2]:
	axs.spines['top'].set_visible(False)
	# axs.spines['left'].set_smart_bounds(True)
	# axs.spines['right'].set_smart_bounds(True)
# ax.tick_params(labeltop=False)  # don't put tick labels at the top
# ax2.xaxis.tick_bottom()

	plt.subplots_adjust(left=0.18, bottom=0.20, right=0.9, top=0.95,
		wspace=0.09, hspace=0.15)



# plt.savefig('Force_Cai.pdf')

plt.show()

		