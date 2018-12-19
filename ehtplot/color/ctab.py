# Copyright (C) 2018 Chi-kwan Chan
# Copyright (C) 2018 Steward Observatory
#
# This file is part of ehtplot.
#
# ehtplot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ehtplot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ehtplot.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname, join, splitext, basename
from glob    import glob

import numpy as np

Nc  = 1024 # nubber of quantization levels in a channel (10bit default)
ext = ".txt"

path   = dirname(__file__)
cscale = Nc - 1.0

def get_ctab(cmap):
    return np.array([cmap(i) for i in range(cmap.N)])

def list_ctab():
    return [splitext(basename(f))[0] for f in glob(join(path, '*'+ext))]

def save_ctab(ctab, name):
    if ctab.shape[1] == 4 and np.all(ctab[:,3] == 1.0):
        ctab = ctab[:,:3]
    np.savetxt(name, np.rint(ctab * cscale).astype(int), fmt="%i")

def load_ctab(name):
    ctab = np.loadtxt(join(path, name+ext)) / cscale
    if ctab.shape[1] == 3:
        alpha = np.full((ctab.shape[0], 1), 1.0)
        ctab  = np.append(ctab, alpha, axis=1)
    return ctab