#led_tester_17203511/utils.py
'''
@author: Anjali Hullenahalli Papegowda
'''
from urllib.request import urlopen
def parseFile(input):
        
    if input.startswith("http"):
        print("I am here")
        N, instructions = None, []
        with urlopen(input) as u:
            N = int(u.readline())
            print(N)
          # for line in u.readline():
         #      instructions.append(line)
        #print(instructions)
        pass          
                
        
                       
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
