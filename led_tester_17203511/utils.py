#led_tester_17203511/utils.py
'''
@author: Anjali Hullenahalli Papegowda
'''
from urllib.request import urlopen
def parseFile(input):
    print(input)    
    if input.startswith("http"):
        for line in urlopen(input):
            line = line.decode("utf-8")
            
                     
                
        
                       
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        # haven't written the code yet...
        return N, instructions
    return
