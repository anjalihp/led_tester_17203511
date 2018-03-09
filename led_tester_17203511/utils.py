#led_tester_17203511/utils.py
'''
@author: Anjali Hullenahalli Papegowda
'''
import os
from urllib.request import urlopen
def parseFile(input):
      
    if input.startswith("http"):
        N, instructions = None, []
        #Referenced from https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
        try:
            urlopen(input)
        except:
            print("URL is invalid")
            return 0,0
        count=0
        for s in urlopen(input):
            s=s.decode("utf-8")
            s=s.strip()
            if count==0:
                N = int(s)
                count=count+1
            elif len(s)>1:
                instructions.append(s)
        return N, instructions      
                
        
                       
    else:
        if not os.path.isfile(input):
            print("File does not  exists")
        else:
        # read from disk
            N, instructions = None, []
            with open(input, 'r') as f:
                N = int(f.readline())
                for line in f.readlines():
                    instructions.append(line)
        # haven't written the code yet...
            return N, instructions
    return 0,0  
