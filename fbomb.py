#!/usr/bin/python

import re
import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) < 4):
	print ("usage: fbomb <file> <incr> <title>")
else:
	timestamp = re.compile("(\d{2}):(\d{2}):(\d{2}),\d{3} -->")
	fuck = re.compile("[Ff]uck")

	hits = [];
	num = 0;


	with open(sys.argv[1]) as f:
		for line in f:
			if (timestamp.match(line)):
				match = timestamp.search(line)
				num = int(match.group(1)) * 60 * 60 + int(match.group(2)) * 60 + int(match.group(3))
			if (fuck.findall(line)):
				for afuck in fuck.findall(line):
					hits.append(num)
					num += 1

	increment = int(sys.argv[2])
	ticker = 0
	bars = [0]
	ticks = [0]

	while(len(hits) > 0):
		while (ticker * increment < hits[0]):
			ticker += 1
			bars.append(0)
			ticks.append(ticker)
		bars[ticker] += 1
		hits.pop(0)

	print (bars)

	pos = np.arange(len(ticks))
	width = 0.3
	ax = plt.axes()

	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(ticks)
	ax.set_title(sys.argv[3])

	plt.bar(pos, bars, width, color='r')
	plt.show()