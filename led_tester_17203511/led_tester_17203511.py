# -*- coding: utf-8 -*-

"""Main module."""
import sys
import re
from urllib.request import urlopen

class ledTester:
    lights = None
    def __init__(self,N):
        self.size_of_grid=N
        self.grid_element=[[0]*N for _ in range(N)]

    def apply(self,instructions):
        cmd,x1_value,y1_value,x2_value,y2_value=self.parseEachLine(instructions)
        #print(cmd,x1_value,y1_value,x2_value,y2_value)
        
        if x1_value<0:
            x1_value=0
        if x2_value<0:
            x2_value=0
        if y1_value<0:
            y1_value=0
        if y2_value<0:
            y2_value=0
            
        if x1_value>self.size_of_grid-1:
            x1_value=self.size_of_grid-1
        if x2_value>self.size_of_grid-1:
            x2_value=self.size_of_grid-1
        if y1_value>self.size_of_grid-1:
            y1_value=self.size_of_grid-1
        if y2_value>self.size_of_grid-1:
            y2_value=self.size_of_grid-1
        
        
        
        if cmd=="turn on":
            for i in range(x1_value,x2_value+1):
                for j in range(y1_value,y2_value+1):
                    self.grid_element[i][j]=1
        elif cmd=="turn off":
            for i in range(x1_value,x2_value+1):
                for j in range(y1_value,y2_value+1):
                    self.grid_element[i][j]=0
        elif cmd=="switch":
            for i in range(x1_value,x2_value+1):
                for j in range(y1_value,y2_value+1):
                    if self.grid_element[i][j]==0:
                        self.grid_element[i][j]=1  
                    else:
                        self.grid_element[i][j]=0
        elif cmd=="BadString":
            for i in range(x1_value,x2_value+1):
                for j in range(y1_value,y2_value+1):
                    self.grid_element[i][j]=0

    def parseEachLine(self,message):
        pattern=re.compile(".*(turn on|turn off|switch|switcy)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
       # print(pattern)
        #print(pattern.search(str(message))[1],int(pattern.search(message)[2]))
        while(pattern.search(str(message))):
            return(pattern.search(str(message))[1],int(pattern.search(message)[2]),int(pattern.search(message)[3]),int(pattern.search(message)[4]),int(pattern.search(message)[5]))
        #print(pattern.search(str(message))[1])
        return("BadString",0,0,0,0)
        
    
    def countOccupied(self):
       # for i in range(self.size_of_grid):
                #for j in range(self.size_of_grid):
                   # print(self.grid_element[i][j], end=' ')
                #print()
        count=0
        for i in range(self.size_of_grid):
                for j in range(self.size_of_grid):
                    if self.grid_element[i][j]==1:
                        count=count+1
        return count
                    
        
        

      
