#led_tester_17203511/utils.py
'''
@author: Anjali Hullenahalli Papegowda
'''
from urllib.request import urlopen
def parseFile(input):
      
    if input.startswith("http"):
        N, instructions = None, []
        count=0
        for s in urlopen(input):
            s=s.decode("utf-8")
            s=s.strip()
            if count==0:
                N = int(s)
                print()
                count=count+1
            elif len(s)>1:
                instructions.append(s)
        return N, instructions      
                
        
                       
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
