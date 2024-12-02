#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:10:51 2024

@author: noleska
"""

import csv

class report:
    def __init__(self, levels):
        self.levels = [int(level) for level in levels]
        self.changes = [self.levels[i+1] - self.levels[i] \
                        for i in range(len(self.levels)-1)]
        self.abs_changes = [abs(x) for x in self.changes]
        self.contains_ascend = len([x for x in self.changes if x > 0]) > 0
        self.contains_descend = len([x for x in self.changes if x < 0]) > 0
        self.safe = max(self.abs_changes) <= 3 \
            and min(self.abs_changes) >= 1 \
                and not(self.contains_ascend and self.contains_descend)


if __name__ == '__main__':
    input_loc = r'./input.txt'
    
    reports = []
    
    with open(input_loc, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            reports.append(report(row))
            
    print(len([x for x in reports if x.safe]))
