#Need a G-code tapered helix, like a SPTM thread milled NPT thread? This is that.
#Designed for linuxcnc, but you can just change the template G code to whatever you need.
#WARNING! Be careful with this script. Always dry run generated code.

#all dims. in mm.
import math
import numpy as np
res = 0.01 #how accurate do you want the path to be
thread_pitch = 1.81356 #pretty obvious.
thread_depth = 13.71600 #how deep do you want the hole to be threaded
cutter_radius = 8.34 #How wide's your cutter?
hole_start_radius = 12.6 #start radius minus thread height.
hole_end_radius = 10.8518 #same.
start_thread_height = 0.25 #How deep should the first pass 
end_thread_height = 1.451 #How deep should the final pass make the threads?
thread_height_steps = 6.0
feed_rate = 600
tool_length_offset = -8.67
starting_offset = 2.0 #1 mm above the hole, to properly start the first thread.
f = open('taper.ngc',"w+")
f.write("%\n")
f.write("G64 P0.025\n")
f.write("M6 T1\n")
f.write("M3 S24000\n")
f.write("G0X0.0000Y0.0000Z15.0000\n")
for current_thread_height in np.linspace(start_thread_height, end_thread_height,thread_height_steps):
	f.write("G0X0.0000Y0.0000Z{}\n".format(tool_length_offset+starting_offset))
	for d in np.arange(-1.0*starting_offset, thread_depth, res):
		r = ((hole_start_radius-((hole_start_radius-hole_end_radius)*(d/thread_depth)))-cutter_radius)+current_thread_height
		x = math.sin((d*2.0*math.pi)/thread_pitch)*r
		y = math.cos((d*2.0*math.pi)/thread_pitch)*r
		f.write("G01 X{} Y{} Z{} F{}\n".format(round(x,5),round(y,5),(-1.0*round(d,5))+tool_length_offset,feed_rate))
	f.write("G0 X0.0000 Y0.0000\n")
f.write("M02\n")
f.write("%\n")
f.close()
