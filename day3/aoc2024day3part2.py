import re

class instruction:
  def __init__(self, txt, control_flag):
    self.txt = txt
    self.factors = [int(x) for x in re.findall("\d+", self.txt)]
    self.product = self.factors[0] * self.factors[1]
    self.control_flag = control_flag

mult_pattern = "mul\(\d+\,\d+\)"
instructions = []

with open(r'./input.txt', 'r', newline="") as f:
  in_str = str(f.readlines())

# get the rest of the mults, setting control flag to false for those following a "don't"
for mult_inst in re.finditer(mult_pattern, in_str):
  prev_substr = in_str[:mult_inst.start()]
  last_do = prev_substr.rfind(r"do()")
  last_dont = prev_substr.rfind(r"don't()")
  flag_control_do = last_do > last_dont or last_dont == -1
  instructions.append(instruction(in_str[mult_inst.start():mult_inst.end()], flag_control_do))

print("Part 2:", sum(x.product for x in instructions if x.control_flag == True))
