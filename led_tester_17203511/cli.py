# -*- coding: utf-8 -*-

"""Console script for led_tester_17203511."""
import sys
import click
sys.path.append('.')
from  utils import *
from led_tester_17203511.led_tester_17203511 import ledTester
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester_17203511."""
    print("input", input)
    
    
    N,instructions=parseFile(input)
    
    if N!=0:
        lights = ledTester(N)
    
        for instruction in instructions:
            lights.apply(instruction)    
    
        
        print('#LEDs TURNED ON: ', lights.countOccupied()) 
        return input

if __name__ == "__main__":
    sys.exit(main())
