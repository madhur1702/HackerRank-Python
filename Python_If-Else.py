#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2==1:
    print("Weird")
else:
  if 2<=n<=5:
    print("Not Weird")      
  elif 5 <n<=20:
    print("Weird")
  else:
    print("Not Weird")
