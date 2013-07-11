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
import random

def merge(ListA, ListB):
    N = len(ListA) + len(ListB)
    ListC = []
    indexA = 0
    indexB = 0
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
    return ListC

def merge_sort(List):
    if len(List) < 2:
        return List
    else:
        ListA = merge_sort(List[:len(List)/2])
        ListB = merge_sort(List[len(List)/2:])
        return merge(ListA, ListB)


N = 30
a = []
for i in range(N):
    a.append(random.randint(0, 99))
print a
print merge_sort(a)
