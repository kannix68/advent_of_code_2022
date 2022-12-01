#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2022
# See [adventofcode](https://adventofcode.com/2022) original website.
# 
# This solution (Jupyter lab 3.2.7; python 3.10) by kannix68, @ 2022-12.  \
# Using anaconda distro, conda v22.9.0.  \
# Tested and run on MacOS v10.14.6 "Mojave".
# 
# Reddit [r/adventofcode](https://www.reddit.com/r/adventofcode)

# In[ ]:


import copy
import itertools
import logging
import re
import sys

import numpy as np
import pandas as pd

import pylib.aochelper as aoc
from pylib.aochelper import map_list as mapl
from pylib.aochelper import filter_list as filterl

print("Python version:", sys.version)
print("Version info:", sys.version_info)

log = aoc.getLogger(__name__)
print(f"Initial log-level={aoc.getLogLevelName(log.getEffectiveLevel())}.")


# ## Problem domain code

# ### --- Day 1: Calorie Counting ---

# In[ ]:


print("Day 1")

tests = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()


# In[ ]:


def solve_day01pt1(inp):
  """Solve Day 1 part 1."""
  reindeers = list(map(lambda it: it.split("\n"), inp.split("\n\n")))
  for idx, r in enumerate(reindeers):
    r = list(map(int, r))
    reindeers[idx] = r
  #print(reindeers)
  return max(map(sum, reindeers))


# In[ ]:


#log.setLevel(logging.DEBUG)
expected = 24_000
result = solve_day01pt1(tests)
aoc.assert_msg(f"test solve day 1 part 1 expected={expected} result={result}", result == expected) 


# In[ ]:


ins = aoc.read_file_to_str("./in/day01.in").strip()
out = solve_day01pt1(ins)
print("day 1 part 1 output:", out)


# In[ ]:


print("Day 1 part 2")


# In[ ]:


def solve_day01pt2(inp):
  """Solve Day 1 part 2."""
  reindeers = list(map(lambda it: it.split("\n"), inp.split("\n\n")))
  for idx, r in enumerate(reindeers):
    r = list(map(int, r))
    reindeers[idx] = r
  reindeers = map(sum, reindeers)
  top3 = sorted(reindeers, reverse=True)[0:3]
  return sum(top3)


# In[ ]:


expected = 45000
result = solve_day01pt2(tests)
aoc.assert_msg(f"test solve day 1 part 2 expected={expected} result={result}", result == expected) 


# In[ ]:


out = solve_day01pt2(ins)
print("day 1 part 2 output:", out)

