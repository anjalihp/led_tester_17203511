# -*- coding: utf-8 -*-

"""Console script for led_tester_17203511."""

import click
from led_tester_17203511 import ledTester
from utils import parseFile
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester_17203511."""
    print("input", input)
    
    N,instructions=parseFile(input)
    
    lights = ledTester(N)
    
    for instruction in instructions:
        lights.apply(instruction)    
    
    
        
        
    print('#occupied: ', lights.countOccupied()) 
    
    return input

if __name__ == "__main__":
    import sys
    sys.exit(main())