# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:12:43 2021

VM2Hack Main

Main Program The main program should construct a Parser to parse the VM input file and a CodeWriter
to generate code into the corresponding output file. It should then march through the VM commands in the
input file and generate assembly code for each one of them.
If the program’s argument is a directory name rather than a file name, the main program should process
all the .vm files in this directory. In doing so, it should use a separate Parser for handling each input file
and a single CodeWriter for handling the output.

@author: IKM1YH
"""
import VM2Hack_CodeWriter
import VM2Hack_Parser
