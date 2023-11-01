from vcApplication import *

def OnStart():
    cmduri = getApplicationPath() + 'iso_grid_generate.py'
    cmd = loadCommand('isoGrid',cmduri)
    addMenuItem('VcTabTeach/Generate', "isoGrid", -1, "isoGrid")