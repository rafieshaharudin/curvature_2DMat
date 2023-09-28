#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:14:00 2023

@author: rafieshaharudin

Title: curvature_2DMat_v2.1

Aim: To create ripple on 2D materials
     using the normal distribution curve.
     Note: This code can handle 2 type of atoms max
      with an equal number of at1 and at2
"""

import numpy as np
import pandas as pd
import sys
import params   # need to be in the same directory

# in_file = input("input file:")
out_file = input("output file:")

# 1st part (i) : read XYZ coordinates, arrange by X before pass to DataFrame
# 1 type of atom
if params.n_typ == 1:
        x = []
        y = []
        z = []

        fr = open(params.in_file).readlines()
        for line in fr:
                s = line.split()
                x.append(float(s[0]))
                y.append(float(s[1]))
                z.append(float(s[2]))

# consistency check
        if len(x) != params.n_at1:
                print(" ")
                print(" ")
                print("Inconsistency ERROR: The number of atom specified in params.py;")
                print("is not equal to number of atoms in input_file.")
                print(" ")
                print("Exiting the program ...")
                print(" ")
                print(" ")

                sys.exit()

# if okay, continue
# rearrange in ascending order by "X"
        else:
                data = {"X": x, "Y": y, "Z": z}
                df = pd.DataFrame(data)
                df_sorted = df.sort_values(by="X")
                df_sorted.reset_index(drop=True, inplace=True)

# 1st part (ii) : read XYZ coordinates, arrange by X before pass to DataFrame
# 2 type of atoms
while params.n_typ == 2:
# check N atoms in params.py
        if params.n_at1 != params.n_at2:
                print(" ")
                print(" ")
                print("ERROR: The number of atom1 and atom2 are not equal;")
                print("       this code could not handle that ... YET!")
                print(" ")
                print("Exiting the program ...")
                print(" ")
                print(" ")

                sys.exit()

# if okay, continue
        elif params.n_at1 == params.n_at2:
                x1 = []
                y1 = []
                z1 = []
                x2 = []
                y2 = []
                z2 = []
                total_at = params.n_at1 + params.n_at2
# read 1st type
                fr1 = open(params.in_file).readlines()[:params.n_at1]
                for line in fr1:
                        s1 = line.split()
                        x1.append(float(s1[0]))
                        y1.append(float(s1[1]))
                        z1.append(float(s1[2]))
# read 2nd type
                fr2 = open(params.in_file).readlines()[params.n_at1:total_at]
                for line in fr2:
                        s2 = line.split()
                        x2.append(float(s2[0]))
                        y2.append(float(s2[1]))
                        z2.append(float(s2[2]))

# consistency check
        fr_check = open(params.in_file).readlines()
        count = 0
        for line in fr_check:
                count += 1
        if count != total_at:
                print(" ")
                print(" ")
                print("Inconsistency ERROR: The number of atom specified in params.py;")
                print("is not equal to number of atoms in input_file.")
                print(" ")
                print("Exiting the program ...")
                print(" ")
                print(" ")

                sys.exit()

# if okay, continue
# rearrange in ascending order by "X"
        else:
                data1 = {"X1": x1, "Y1": y1, "Z1": z1}
                df1 = pd.DataFrame(data1)
                df1_sorted = df1.sort_values(by="X1")
                df1_sorted.reset_index(drop=True, inplace=True)

                data2 = {"X2": x2, "Y2": y2, "Z2": z2}
                df2 = pd.DataFrame(data2)
                df2_sorted = df2.sort_values(by="X2")
                df2_sorted.reset_index(drop=True, inplace=True)

# recombine both atom types after rearrangement
                df1_sorted.columns = ["X", "Y", "Z"]
                df2_sorted.columns = ["X", "Y", "Z"]
                df_sorted = pd.concat([df1_sorted, df2_sorted], axis=0, ignore_index=True)
                break
        break

# 2nd part : generate shift parameters from normal distribution
num_points = params.n_at1
mu = num_points//2              # integer division
sigma = params.sigma            # how to decide the spread?
shift_factor = []
shifted_Z = []
idx = list(range(1,num_points+1))

for i in idx:
        norm = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((i - mu)**2) / (2 * sigma**2))
        shift_factor.append(norm*params.amp)

if params.n_typ == 2:
        shift_factor = shift_factor + shift_factor
else:
        shift_factor = shift_factor

# manipulate Z to create 1D curve
for i,j in zip(df_sorted["Z"],shift_factor):
        if len(df_sorted) == len(shift_factor):
                newZ = i+j
                shifted_Z.append(newZ)

# this might be unnecessary now
        else:
                print(" ")
                print(" ")
                print("ERROR: N shift factor != N z_points!")
                print("check you have the correct number of atoms.")
                print(" ")
                print(" ")
                break

# update shifted Z coordinates in the DataFrame
df_sorted["Z"] = shifted_Z

# calculate curvature (h/L)
L = max(df_sorted["X"]) - min(df_sorted["X"])
h = max(df_sorted["Z"]) - min(df_sorted["Z"])
D = 100 * (h/L)

# 3rd part : write output file
fw = open(out_file, "w")
for x,y,z in zip(df_sorted["X"], df_sorted["Y"], df_sorted["Z"]):
        fw.write(str("%20.16f" % x) + str("%20.16f" % y) + str("%20.16f\n" % z))

fout = open("out.dat", "w")
fout.write(str("%20s" % "curvature %") + str("%10.2s" % D) +str("%2s\n" % "%"))

fw.close()
fout.close()

print("-----------------------------------")
print(f"Your output file: {out_file}")
print(f"h/L: {D:.2f} %")
print("-----------------------------------")


