# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import glob



############## USER PARAMETERS ##############################################################################################

# Where your files are saved:
datapath = "C://Users//s3599678//OneDrive - RMIT University//PhD//thermal PILs paper//DSC//RAW DATA//EtAA//"

# X axis, play with this number to get a nice temperature x axis scale
Xaxis = 300
        
# Axis font size
Font = 18

# Axis lables and legend font size   
LabelFont = 30
# Changes shape of plot frame (in inches i think), pair this with "Xaxis" to get a nice scale for the x and y axis
Xdistance = 30
Ydistance = 10


############### DONT TOUCH FROM HERE #########################################################################################
files = sorted(glob.glob(datapath+"*.txt"))
for data in files:
        split_path = data.split("\\") 
        file_name = split_path[-1]
        #File_title.append(file_name)
        file_tag = file_name[:-4] 
        data = np.loadtxt((open(data,'rt').readlines()[:-1]), skiprows= 2)
        Temp = (data[:,3])
        x = data[:, 1]
        plt.grid(False)
        plt.xlabel("Temp(C)", fontsize = LabelFont)
        plt.ylabel("HF(mW)", fontsize = LabelFont)
        plt.xticks(ticks = data[:,1][::Xaxis], labels =  Temp[::Xaxis].astype(int), fontsize = Font)
        y = data[:, 2]
        plt.yticks(fontsize = Font)
        plt.plot(x,y,label = file_tag)
        plt.legend(loc="upper right", fontsize = LabelFont)
        plt.rcParams["figure.figsize"] = (Xdistance,Ydistance)
        plt.show 
        plt.savefig(datapath, dpi = 100)
        
       
    
    


