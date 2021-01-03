# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.10
#  Last Updated: Jan 3rd, 2021
# --------------------------------------------------------------
# --------------------------------------------------------------
#  ::::WAVE TOOLS:::BY::ATTILA::GASPARETZ::::::::::::::::::::::
# --------------------------------------------------------------

### ADD THIS TO YOUR INIT.PY
### WaveTools_path = "<path to your .nuke folder>/WaveTools-main"
### nuke.pluginAddPath(WaveTools_path)

import nuke
import os

# For more info
# https://www.gatimedia.co.uk/wave-expression-tools
# https://github.com/GatiMedia/WaveTools


toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("WaveTools", icon = os.path.join(WaveTools_path, "icon/waveicon.png"))

#COLOR
m.addCommand('WaveGrade', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveGrade.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WGrade.png") )
m.addCommand('WaveMultiply', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveMultiply.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WGrade.png")  )
m.addCommand('WaveSaturation', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveSaturation.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WGrade.png") )
m.addCommand('WaveHSVTool', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveHSVTool.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WHSVTool.png") )
#FILTER
m.addCommand('WaveBlur', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveBlur.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WBlur.png")  )
m.addCommand('WaveDefocus', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveDefocus.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WBlur.png")  )
m.addCommand('WaveZDefocus', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveZDefocus.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WBlur.png") )
m.addCommand('WaveGlow', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveGlow.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WGlow.png")  )
#TRANSFORM
m.addCommand('WaveTransform', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveTransform.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WTransform.png")  )
#TIME
m.addCommand('WaveFrameHold', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveFrameHold.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WFrameHold.png") )
#KEYER
m.addCommand('WaveKeyer', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/WaveKeyer.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WKeyer.png") )
#DRAW
m.addCommand('DirNoise', "nuke.nodePaste(\"" + os.path.join(WaveTools_path + "/nodes/DirNoise.nk") + "\")", icon = os.path.join(WaveTools_path, "icon/WNoise.png") )



