#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:10:51 2024

@author: noleska
"""

import csv


class report:
    def __init__(self, levels, dampen=True):
        self.dampen = dampen
        self.levels = [int(level) for level in levels]
        self.changes = [self.levels[i+1] - self.levels[i] \
                        for i in range(len(self.levels)-1)]
        self.abs_changes = [abs(x) for x in self.changes]
        self.overchanges = max(self.abs_changes) > 3 or min(self.abs_changes) < 1
        self.contains_ascend = len([x for x in self.changes if x > 0]) > 0
        self.contains_descend = len([x for x in self.changes if x < 0]) > 0
        self.switches_direction = self.contains_ascend and self.contains_descend
        self.inherent_safe = not self.switches_direction \
                             and not self.overchanges

        # problem dampener
        self.dampened_safe = False
        if self.dampen and not self.inherent_safe:
            for i in range(len(self.levels)):
                temp_levels = self.levels.copy()
                temp_levels.pop(i)
                if report(temp_levels, dampen=False).inherent_safe:
                    self.dampened_safe = True
                    break
                
        self.safe = self.inherent_safe or self.dampened_safe
            


if __name__ == '__main__':
    input_loc = r'./input.txt'
    
    reports = []
    
    with open(input_loc, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            reports.append(report(row))
            
    print(len([x for x in reports if x.safe]))
