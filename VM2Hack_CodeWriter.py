 # -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:13:20 2021

VM2Hack
CodeWriter

CodeWriter: Translates VM commands into Hack assembly code.

@author: IKM1YH
"""

class CodeWriter():
    '''
    Translates VM commands into Hack assembly code.
    '''
    
    def __init__(self, Outputfile):
        '''Opens the outputfile.asm and gets ready to write into it.'''
        self.filename=Outputfile
        self.counter = 0
        print('Start to write '+str(self.filename))
        
        #extract commands from strings
        self.f = open(self.filename, 'w')
        
    def setFileName(self,filename):
        '''Informs the code writer that the translation of a new VM file is started.'''
        
    def writeArithmetic(self, command):
        '''Wites the assembly code that iis the translation of the given arithmetic command.
        add, sub, neg, eq, gt, lt, and, or, not '''

        self.Arithdic = {'add':['@SP','A=M-1','D=M','A=A-1','M=D+M','@SP','M=M-1'],\
                         'sub':['@SP','A=M-1','D=M','A=A-1','M=M-D','@SP','M=M-1'],\
                         'neg':['@SP','A=M-1','M=-M'],\
                         'eq':[], 'gt':[], 'lt':[], 'and':[], 'or':[], 'not':[]}
        
        
        
    def writePushPop(self, command, segment, index):
        '''Writes assembly code that is the translatiion of the given command, 
        where command is eithr C_PUSH or C_POP.'''
        
        
        
    def close(self):
        '''Closes the output file.'''
        self.f.close()
