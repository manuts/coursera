#!/usr/bin/env python
# 
# Copyright 2013 IIT Bombay.
# Author: Manu T S
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

def merge((a, ListA), (b, ListB)):
    N = len(ListA) + len(ListB)
    ListC = []
    indexA = 0
    indexB = 0
    inversions = 0
    for n in range(N):
        if indexA == len(ListA):
            for k in range(indexB, len(ListB)):
                ListC.append(ListB[k])
            break
        elif indexB == len(ListB):
            for k in range(indexA, len(ListA)):
                ListC.append(ListA[k])
            break
        elif ListA[indexA] < ListB[indexB]:
            ListC.append(ListA[indexA])
            indexA += 1
        else:
            ListC.append(ListB[indexB])
            indexB += 1
            inversions += (len(ListA) - indexA)
    return (a + b + inversions, ListC)

def merge_sort(List):
    if len(List) < 2:
        return (0, List)
    else:
        (a, ListA) = merge_sort(List[:len(List)/2])
        (b, ListB) = merge_sort(List[len(List)/2:])
        return merge((a, ListA), (b, ListB))

a = []
f = open("IntegerArray.txt", "r")
line = f.readline()
while line:
    a.append(int(line))
    line = f.readline()

print merge_sort(a)[0]
