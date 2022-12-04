#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2022
# See [adventofcode](https://adventofcode.com/2022) original website.
# 
# This solution (Jupyter lab 3.5.0; python 3.10) by kannix68, @ 2022-12.  \
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


# ### --- Day 2: Rock Paper Scissors ---

# In[ ]:


tests = """
A Y
B X
C Z
""".strip()


# In[ ]:


values = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {
  'A': {'X': 3, 'Y': 6, 'Z': 0},
  'B': {'X': 0, 'Y': 3, 'Z': 6},
  'C': {'X': 6, 'Y': 0, 'Z': 3},
}

def solve_day02pt1(inp):
  """Solve Day 2 part 1."""
  score = 0
  for line in inp.splitlines():
    [p1, p2] = line.split()
    round_score = values[p2]  # item value score
    round_score += outcomes[p1][p2]  # outcome score
    score += round_score
  return score


# In[ ]:


print("Day 2 part 1")
expected = 15
result = solve_day02pt1(tests)
aoc.assert_msg(f"test solve day 2 part 1 expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str("./in/day02.in").strip()
out = solve_day02pt1(ins)
print(f"day 2 part 1 output: {out}")


# In[ ]:


def solve_day02pt2(inp):
  """Solve Day 2 part 2."""
  outcome_tags = {'X': 0, 'Y': 3, 'Z': 6}  # who wins on pt 2
  outcomes_inv = {}
  for k, innerdict in outcomes.items():
    outcomes_inv[k] = {v: k for k, v in innerdict.items()}  # keys and values swapped
  score = 0
  for line in inp.splitlines():
    [p1, o2] = line.split()
    round_score = outcome_tags[o2]
    p2 = outcomes_inv[p1][round_score]  # my item (player 2)
    round_score += values[p2]  # outcome score
    score += round_score
  return score


# In[ ]:


print("Day 2 part 2")
expected = 12
result = solve_day02pt2(tests)
aoc.assert_msg(f"test solve day 2 part 2 expected={expected} result={result}", result == expected)


# In[ ]:


out = solve_day02pt2(ins)
print(f"day 2 part 2 output: {out}")

