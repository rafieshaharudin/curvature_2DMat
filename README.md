author: rafieshaharudin

# curvature_2DMat
generate curvature on 2D materials for AIMD (VASP)

Version 2.3:
  - This code read/write coordinates (x,y,z) of a unit cell from/for POSCAR.
  - Works on both Direct or Cartesian coordinates.
  - params.py is the input control.
  - amp and sigma in params.py are abitrary value to control the curvature.
  - Change amp and sigma to fit the curvature you need to create.
  - curve is to decide the type of flip (convex or concave).
  - The coordinates need to be isolated from POSCAR to an input file in which the code will read.
  - The code can handle 2D materials with a maximum of 2 type of atoms i.e. hBN.
  - The number of atoms for each type (n_at1 and n_at2) within the unitcell need to be the same.
  - The curvature is 1 dimensional along the X-axis.
  - Included correction to shift the lowest point in z to original flat position.
  - Updated D calculation for n_typ == 1 and n_typ == 2.

Warning:
  - Ensure the D - h/L calculation is on carried out over the backbone atoms!

In the coming version:
  - Upgrade on the curvature making it 2 dimensionals along X- and Y-axis.
  - Increase the robustness of the code so: n_typ > 2 and n_at1 != n_at2.

For any issue please email:
rafieshaharudin@gmail.com
