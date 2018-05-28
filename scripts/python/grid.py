import linuxcnc
s = linuxcnc.stat()
c = linuxcnc.command()

c.mode(linuxcnc.MODE_MDI)
c.wait_complete() # wait until mode switch executed
c.mdi("G0 X0 Y0 Z0")