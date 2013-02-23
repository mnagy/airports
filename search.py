#!/usr/bin/env python

import fileinput
import sys

sources = ('PRG', 'BRQ', 'BTS', 'VIE')
destinations = ('AMS', 'EIN', 'MST', 'RTM', 'SAB', 'EUX')

there = []
back = []

airports = {}
for line in fileinput.input('airports.dat'):
    _, name, city, _, iata, _ = line.split(',', 5)
    iata = iata.strip('"')
    name = name.strip('"')
    city = city.strip('"')
    airports[iata] = "%s (%s), %s" % (name, iata, city)

airlines = {}
for line in fileinput.input('airlines.dat'):
    aid, name, _ = line.split(',', 2)
    name = name.strip('"')
    airlines[aid] = name

for line in fileinput.input('routes.dat'):
    _, aid, src, _, dst, _, _, stops, _ = line.split(',', 8)
    if stops != "0":
        continue
    if src in sources and dst in destinations:
        there.append((src, dst, aid))
    elif src in destinations and dst in sources:
        back.append((src, dst, aid))

for airport in sources + destinations:
    print airports[airport]

print "How to get there:"
for src, dst, aid in there:
    print "%s -> %s with %s" % (airports[src], airports[dst], airlines[aid])

print "How to get back:"
for src, dst, aid in back:
    print "%s -> %s with %s" % (airports[src], airports[dst], airlines[aid])
