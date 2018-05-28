import linuxcnc
import os
from time import sleep
c = linuxcnc.command()
status = linuxcnc.stat()
status.poll()
NGC_DIR = '/home/cnc/Desktop/scripts/ngc/'
os.system('clear')
raw_input("Turn the coolant pump on.")

def run_program(name):
    c.mode(linuxcnc.MODE_AUTO)
    c.wait_complete()
    c.program_open(NGC_DIR + name)
    c.maxvel(60)
    c.auto(linuxcnc.AUTO_RUN, 1)
    c.wait_complete()

def edge_finder():
    c.mode(linuxcnc.MODE_AUTO)
    c.wait_complete()
    print("Edges: ")
    print("1: \n") 
    edge_select = raw_input("> ")
    if(edge_select == '1'):
        pass

while not status.homed:
    raw_input("Machine not homed.")
    status.poll()

if(raw_input("Setup probe? > ")):
    raw_input("Ground probe.")
    run_program("setup.ngc")

while(True):
    os.system('clear')
    print("Welcome to Dan's CNC Script. Select an option: ")
    print("1. Re-setup")
    print("2. Touch off a tool")
    print("3. Zero an edge")
    print("4. Zero a hole")
    selection = raw_input("> ")
    print("\n\n")
    if(selection == '1'):
	run_program("setup.ngc")
    if(selection == '2'):
	run_program("tool.ngc")
    if(selection == '3'):
        edge_finder()
    if(selection == '4'):
	raw_input("Connect jumper to probe.")
	raw_input("Move probe within hole.")
	run_program("zero_hole.ngc")