import os
import Qcircuits.core_net as core
from Qcircuits.core_net import string_to_component
from Qcircuits.constants import *
png_directory = os.path.join(os.path.dirname(__file__),".graphics")
try:
    os.mkdir(png_directory)
except FileExistsError:
    pass
dpi = 300
core.pp = {
    "element_width": 1.,
    "element_height": 1.,
    "margin": 0.,
    "figsize_scaling": 1,
    "color": [0.15, 0.15, 0.15],
    "x_fig_margin": 0.,
    "y_fig_margin": 0.25,
    "C": {
        "gap": 0.2,
        "height": 0.25,
        "lw": 6
    },
    "J": {
        "width": 0.25,
        "lw": 6
    },
    "L": {
        "width": 0.7,
        "height": 0.25,
        "N_points": 150,
        "N_turns": 5,
        "lw": 2
    },
    "R": {
        "width": 0.6,
        "height": 0.25,
        "N_points": 150,
        "N_ridges": 4,
        "lw": 2
    },
    "P": {
        "side_wire_width": 0.25
    },
    "W": {
        "lw": 2
    }
}
# Generate pngs of the different components in their HOVER state
increment = 1
core.pp['W']['lw']+=increment
core.pp['C']['lw']+=increment
core.pp['L']['lw']+=increment
core.pp['R']['lw']+=increment
core.pp['J']['lw']+=increment
el_str_list = ['R','C','L','J','G']

for el in el_str_list:
    string_to_component(el,None,None,'').show(save_to = os.path.join(png_directory,'%s_hover.png'%el),plot = False, dpi = dpi)

# hover selected state
core.pp['color'] = gray
for el in el_str_list:
    string_to_component(el,None,None,'').show(save_to = os.path.join(png_directory,'%s_hover_selected.png'%el),plot = False, dpi = dpi)
# selected state
increment = -1
core.pp['W']['lw']+=increment
core.pp['C']['lw']+=increment
core.pp['L']['lw']+=increment
core.pp['R']['lw']+=increment
core.pp['J']['lw']+=increment
for el in el_str_list:
    string_to_component(el,None,None,'').show(save_to = os.path.join(png_directory,'%s_selected.png'%el),plot = False, dpi = dpi)

# rest state
core.pp['color'] = light_black
for el in el_str_list:
    string_to_component(el,None,None,'').show(save_to = os.path.join(png_directory,'%s.png'%el),plot = False, dpi = dpi)
