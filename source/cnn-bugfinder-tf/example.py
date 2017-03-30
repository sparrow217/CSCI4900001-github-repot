#!/usr/bin/python

#import countbugs python file
import countbugs as eval

x_raw = []
with open('test.txt') as f:
	for line in f:
		x_raw.append(line.strip())
f.close()

#eval is the imported file,  evaluate takes in a list of issues and returns
#the estimated number of true issues
print eval.evaluate(x_raw)
