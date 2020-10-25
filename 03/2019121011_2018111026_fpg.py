#!/usr/bin/env python
with open('BMS1.txt', 'r') as fi:
    dataset = fi.readlines()
dataset = ''.join(dataset)
dataset = dataset.replace('\n', ' ')
dataset = dataset.replace('\r', ' ')
dataset = dataset.split('-2')

for idx, val in enumerate(dataset):
    dataset[idx] = [int(x) for x in val.split('-1') if x.isdigit()]
