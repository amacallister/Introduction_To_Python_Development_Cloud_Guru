"""
- You can call this file the following way to load the debugger at the top: python -m pdb .\debugging.py
- Run the following to see a list of commands when in debugger mode: <<< h
- Example for getting help info for a particular command: <<< help cont
- Command to see where the debugger is located in the file: <<< list or ll
- Set breakpoints while in debugger mode on the commandline example: <<< break 10, index == 5
"""
import pdb 

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        #pdb.set_trace()
        output_values.append(func(values[index]))
        index += 1
    return output_values

def  add_one(val):
    return val + 1

print(map(add_one, list(range(10))))
