#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:14:00 2023

@author: rafieshaharudin

Title: curvature_2DMat_v2.1

Aim: To create ripple on graphene flake (2D)
     using the normal distribution curve.

Note: This code can handle 2 type of atoms max
      with an equal number of at1 and at2
"""

# input parameters
in_file = "coord_hBN"           # input file name
n_typ   = 2                     # number of atom type
n_at1   = 25                    # number of type1 atom
n_at2   = 25                    # number of type2 atom

# normal distribution
amp     = 15                    # control height, amp>=1, 1 = no amplification
sigma   = 8                     # subtle control on width

# end of file

