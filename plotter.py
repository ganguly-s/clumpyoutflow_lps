#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 08:30:34 2021

@author: ganguly93
"""

import astropy.table as ta
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec
from matplotlib import cm

# model select

#num = 0 # choose model A, B or C
if 1: # steady models A21, B , C
    path1 = ['../new_model_dumps/Ax8/','../new_model_dumps/Bx8/','../new_model_dumps/Cx8/']
    path2 = '../new_Output/'
    fn0 = ['966','1000','1000']
    Models = ['Ax8','Bx8','Cx8']
    labels = ['A21','B','C']
    fname = 'combABC.pdf' #output image filename

if 0: #models B and B-c
    path1 = ['../new_Output/Bx8/','../new_Output/Bx8-m5/']
    path2 = '../new_Output/'
    fn0 = ['1000','1000']
    Models = ['Bx8','Bx8-m5']
    labels = ['B','B (m5)']
    fname = 'combB.pdf'
    
if 0: #models C and C-c
    path1 = ['../new_Output/Cx8/','../new_Output/Cx8-m5/']
    path2 = '../new_Output/'
    fn0 = ['1000','1000']
    Models = ['Cx8','Cx8-m5']
    labels = ['C','C (m5)']
    fname = 'combC.pdf'


Line = ['Fe_XXVI','Fe_XXV','Ar_XVIII','S_XVI_4','Si_XIV_6','Si_XIV_5','Mg_XII','Ne_X','O_VIII_19','O_VIII_16','O_VIII_15','O_VII','N_VII','C_VI','Ne_VIII','O_VI','N_V','C_IV','He_II','S_IV','S_IV*','Si_IV','Si_III','C_II','Mg_II']
Doublets = ['Si_XIV_6','Si_XIV_5','Mg_XII','C_II','S_IV','C_IV','C_VI','Fe_XXVI','O_VI','He_II','N_V','O_VIII_19','O_VIII_16','O_VIII_15','Si_IV','N_VII','Ne_X']

row = len(Line) 
hr = np.ones(row)
fig, axs = plt.subplots(nrows=row,ncols=len(path1),gridspec_kw={'height_ratios': hr},figsize=(8,25)) 
plt.subplots_adjust(left=0.05, bottom=0.08, right=0.92, top=0.93, wspace=0., hspace=0.)

fs = 12
alp = 0.3
colors = [ cm.brg(x) for x in np.linspace(0,0.9,len(Line)) ]
lws = [0.8,1,1]
lss = ['-','--',':']

plt.rcParams['font.family'] = 'serif' #'STIXGeneral' #'serif'
matplotlib.rcParams['font.size'] = '16'
matplotlib.rcParams['ps.fonttype'] = 42 #note: fontype 42 compatible with MNRAS style file when saving figs
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.linewidth'] = 1.
plt.rcParams['xtick.major.size'] = 4
plt.rcParams['xtick.minor.size'] = 2
plt.rcParams['ytick.major.size'] = 4
plt.rcParams['ytick.minor.size'] = 2
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.numpoints'] = 1  # uses 1 symbol instead of 2
plt.rcParams['legend.frameon'] = False 
plt.rcParams['legend.handletextpad'] = 0.3

for i,ln in enumerate(Line):
    for j in range(len(path1)):
        axs[i][j].plot([0,0],[0,1.2],'k--',alpha=0.5,lw=1)
        axs[i][j].set_xlim(-600,100)
        axs[i][j].set_ylim(0,1.4)
        axs[i][j].minorticks_on()
        axs[i][j].tick_params(which='both',bottom=True, top=False, left=True, right=False,direction='in')
        axs[i][j].tick_params(which='minor',bottom=True, top=False, left=False, right=False,direction='in')
        axs[i][j].set_xticks([-600,-500,-400,-300,-200,-100,0,100])
        if i != len(Line)-1:
            axs[i][j].set_xticklabels([])
        else:
            axs[i][j].set_xticklabels([-600,-500,-400,-300,-200,-100,0,100])
        if i==12 and j==0:
            axs[i][j].set_ylabel(r"$I_\mathrm{v}$", fontsize=fs,rotation=90)
        fn = Models[j]+'_'+ln+'.fits'
        f = fits.open(fn)
        data = f[1].data
        if ln in Doublets:
            axs[i][j].plot(data['v'],data['flux_r'],color='r',ls='--',lw=1)
            axs[i][j].plot(data['v'],data['flux_b'],color='b',ls='--',lw=1)
            axs[i][j].fill_between(data['v'],data['flux'],1.,color=colors[i],alpha=alp,lw=0)
            if i==0:
                axs[i][j].plot(data['v'],data['flux'],color='k',ls=lss[0],lw=lws[j],label=fn0[j])
            else:
                axs[i][j].plot(data['v'],data['flux'],color='k',ls=lss[0],lw=lws[j])
            if j==0:
                axs[i][j].text(-580,0.3,Line[i].replace('_',' '),fontsize=7)
            #break
        else:
            for key in f[1].columns.names:
                if 'flux' in key:
                    axs[i][j].fill_between(data['v'],data[key],1.,color=colors[i],alpha=alp,lw=0)
                    axs[i][j].plot(data['v'],data[key],color='k',ls=lss[0],lw=lws[j])
                    break
        if j==0:
            axs[i][j].text(-580,0.3,Line[i].replace('_',' '),fontsize=7)
            axs[i][j].tick_params(axis='y',which='major',labelsize=7)
            axs[i][j].set_yticks([0,0.5,1])
            axs[i][j].set_yticklabels(['0','','1'])
        else:
            axs[i][j].set_yticks([0,0.5,1])
            axs[i][j].set_yticklabels([])
            axs[i][j].tick_params(axis="y",labelsize=8)
        axs[0][j].set_title(labels[j],fontsize=fs-4)
        
        f.close()
if len(path1)==3:
    axs[-1][1].set_xlabel(r'$v$ [km s$^{-1}$]',fontsize=fs)
    plt.setp(axs[-1][-1].get_xticklabels()[0], visible=False)
    plt.setp(axs[-1][0].get_xticklabels()[-1], visible=False)
else:
    for j in range(len(path1)):
        axs[-1][j].set_xlabel(r'$v$ [km s$^{-1}$]',fontsize=fs)
    plt.setp(axs[-1][0].get_xticklabels()[-1], visible=False)

plt.savefig(fname,dpi=300,bbox_inches='tight')