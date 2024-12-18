# -*- coding: utf-8 -*-
import re

class instruction:
  def __init__(self, txt):
    self.txt = txt
    self.factors = [int(x) for x in re.findall("\d+", self.txt)]
    self.product = self.factors[0] * self.factors[1]

mult_pattern = "mul\(\d+\,\d+\)"

with open('./input.txt') as f:
   instructions = [instruction(x) for x in re.findall(mult_pattern,str(f.readlines()))]

print("Part 1:", sum(x.product for x in instructions))
