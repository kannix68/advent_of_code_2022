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
import time

from collections import defaultdict

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


# ### --- Day 3: Rucksack Reorganization ---

# In[ ]:


tests = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


# In[ ]:


def split_str_halfs(s):
  """Split a string in two of equel length"""
  pos = len(s)//2
  return [s[:pos], s[pos:]]

def solve_day03pt1(inp):
  """Solve Day 3 part 1."""
  score = 0
  ofst_lower = ord("a") - 1
  ofst_upper = ord("A") - 27
  for line in inp.splitlines():
    sh1, sh2 = split_str_halfs(line)
    #[sh1, sh2] |> print
    freqh1, freqh2 = [defaultdict(int), defaultdict(int)]
    for c in sh1:
      freqh1[c] += 1
    for c in sh2:
      freqh2[c] += 1
    isct = set(freqh1.keys()).intersection(set(freqh2.keys()))
    assert len(isct) == 1
    isct = list(isct)[0]
    if isct.isupper():
      prio = ord(isct) - ofst_upper
    else:
      prio = ord(isct) - ofst_lower
    score += prio
    #f"set-intersection={isct}, prio={prio}" |> print
  return score


# In[ ]:


print("Day 3 part 1")
expected = 157
result = solve_day03pt1(tests)
aoc.assert_msg(f"test solve day 3 part 1 expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str("./in/day03.in").strip()
out = solve_day03pt1(ins)
print(f"day 3 part 1 output: {out}")


# In[ ]:


def solve_day03pt2(inp):
  """Solve Day 3 part 2."""
  score = 0
  ofst_lower = ord("a") - 1
  ofst_upper = ord("A") - 27
  grp = []
  for idx, line in enumerate(inp.splitlines()):
    grp.append(line)
    if len(grp) == 3:
      tgtset = set()
      for idx, memb in enumerate(grp):
        freqs = defaultdict(int)
        for c in memb:
          freqs[c] += 1
        if idx==0:
          tgtset = set(freqs.keys())
        else:
          tgtset = tgtset.intersection(freqs.keys())
      grp = []
      assert len(tgtset) == 1
      un = list(tgtset)[0]
      if un.isupper():
        prio = ord(un) - ofst_upper
      else:
        prio = ord(un) - ofst_lower
      #f"grp set-intersection={tgtset}, prio={prio}" |> print
      score += prio
  assert idx > 0 
  assert (idx+1) % 3 == 0
  return score


# In[ ]:


print("Day 3 part 2")
expected = 70
result = solve_day03pt2(tests)
aoc.assert_msg(f"test solve day 3 part 2 expected={expected} result={result}", result == expected)


# In[ ]:


out = solve_day03pt2(ins)
print(f"day 3 part 2 output: {out}")


# ### --- Day 4: Camp Cleanup ---

# In[ ]:


day = "Day 4"
symb = "day04"
part = "part 1"
tests = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


# In[ ]:


def has_fully_containment(e1, e2):
  return (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1])

def solve_day04pt1(inp):
  """Solve Day 4 part 1."""
  score = 0
  #pairs = []
  for line in inp.splitlines():
    elves = line.split(",")
    elves = list(map(lambda it: list(map(int, it.split("-"))), elves))
    if has_fully_containment(elves[0], elves[1]):
      #f"{elves} has fully containment" |> print
      score += 1
  #pairs |> print
  return score


# In[ ]:


print(f"{day} {part}")
expected = 2
result = solve_day04pt1(tests)
aoc.assert_msg(f"test solve {day} {part} expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str(f"./in/{symb}.in").strip()
out = solve_day04pt1(ins)
print(f"{day} {part} output: {out}")


# In[ ]:


def has_overlap(e1, e2):
  return (e1[1] >= e2[0] and e1[1] <= e2[1]) or (e2[1] >= e1[0] and e2[1] <= e1[1])

def solve_day04pt2(inp):
  """Solve Day 4 part 2."""
  score = 0
  for line in inp.splitlines():
    elves = line.split(",")
    elves = list(map(lambda it: list(map(int, it.split("-"))), elves))
    if has_overlap(elves[0], elves[1]):
      #f"{elves} has overlap" |> print
      score += 1
  return score


# In[ ]:


part = "part 2"
expected = 4
print(f"{day} {part}")
result = solve_day04pt2(tests)
aoc.assert_msg(f"test solve {day} {part} expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str(f"./in/{symb}.in").strip()
out = solve_day04pt2(ins)
print(f"{day} {part} output: {out}")


# ### --- Day 5: Supply Stacks ---

# In[ ]:


day = "Day 5"
symb = "day05"
part = "part 1"
tests = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


# In[ ]:


def pop_n(l, n):
  """Pop n members from top of stack (list), return popped head and altered stack."""
  popped, popped_lst = [ l[-n:], l[0:len(l)-n] ]
  return [popped, popped_lst]

def push_n(l, data):
  """Push data (list) members to top of stack (list), return altered stack."""
  for elem in data:
    l.append(elem)
  return l

def transpose_lol(lol):
  """Transpose a list-of-lists."""
  # short circuits at shortest nested list if table is jagged:
  return list(map(list, zip(*lol)))

def get_stacks(rows):
  """Take parsed rows from input string and pprocess into target data structure list-of-tacks."""
  stacks = transpose_lol(rows)
  stacks = mapl(lambda it: list(reversed(it)), stacks)
  for stack in stacks:
    while stack[-1] == "":
      stack.pop()
  return stacks

def play_stack_cmds(stacks, cmds):
  """Play the commands on stacks data."""
  for cmd in cmds:
    anz, frm, to = cmd
    hd, stacks[frm-1] = pop_n(stacks[frm-1], anz)
    stacks[to-1] = push_n(stacks[to-1], reversed(hd))
  return stacks


# In[ ]:


def solve_day05pt1(inp):
  """Solve Day 5 part 1."""
  chunk_size = 4
  stacks = []
  rows = []
  cmds = []
  #f"inp=\n{inp}" |> print
  for line in inp.split("\n"):
    #f"line=>{line}< len={len(line)}" |> print
    line += " "
    if "[" in line:
      llen = len(line)
      row = [ line[i:i+chunk_size] for i in range(0, llen, chunk_size) ]
      #f"found row1={row}" |> print
      row = mapl(lambda it: it.replace("[", "").replace("]", "").strip(), row)
      #f"found row2={row}" |> print
      rows.append(row)
    elif line.strip() == "":
      #"empty line found" |> print
      continue
    elif "move" in line:
      m = re.search(r"^move (\d+) from (\d+) to (\d+)", line)
      l = mapl(int, [m.group(1), m.group(2), m.group(3)])
      cmds.append(l)
    else:
      #f"unparsed line=>{line}<" |> print
      continue
  stacks = get_stacks(rows)
  #f"initial_stacks=\n{stacks}" |> print
  #f"  cmds=\n{cmds}" |> print
  stacks = play_stack_cmds(stacks, cmds)
  result = "".join([stack.pop() for stack in stacks])
  #f"result={result}" |> print
  return result


# In[ ]:


print(f"{day} {part}")
expected = "CMZ"
result = solve_day05pt1(tests)
aoc.assert_msg(f"test solve {day} {part} expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str(f"./in/{symb}.in")
out = solve_day05pt1(ins)
print(f"{day} {part} result: {out}")


# In[ ]:


def play_stack_cmds_pt2(stacks, cmds):
  """Play the commands on stacks data, modified for part 2."""
  for cmd in cmds:
    anz, frm, to = cmd
    hd, stacks[frm-1] = pop_n(stacks[frm-1], anz)
    stacks[to-1] = push_n(stacks[to-1], hd)  # changed, not reversed
  return stacks


# In[ ]:


def solve_day05pt2(inp):
  """Solve Day 5 part 2."""
  chunk_size = 4
  stacks = []
  rows = []
  cmds = []
  for line in inp.split("\n"):
    line += " "
    if "[" in line:
      llen = len(line)
      row = [ line[i:i+chunk_size] for i in range(0, llen, chunk_size) ]
      row = mapl(lambda it: it.replace("[", "").replace("]", "").strip(), row)
      rows.append(row)
    elif line.strip() == "":
      continue
    elif "move" in line:
      m = re.search(r"^move (\d+) from (\d+) to (\d+)", line)
      l = mapl(int, [m.group(1), m.group(2), m.group(3)])
      cmds.append(l)
    else:
      continue
  stacks = get_stacks(rows)
  stacks = play_stack_cmds_pt2(stacks, cmds)  # changed, pt2
  result = "".join([stack.pop() for stack in stacks])
  return result


# In[ ]:


part = "part 2"
expected = "MCD"
print(f"{day} {part}")
result = solve_day05pt2(tests)
aoc.assert_msg(f"test solve {day} {part} expected={expected} result={result}", result == expected)


# In[ ]:


ins = aoc.read_file_to_str(f"./in/{symb}.in")
out = solve_day05pt2(ins)
print(f"{day} {part} output: {out}")


