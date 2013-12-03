# -*- coding: utf8 -*-

i=1
y=6
while i<y:
	x=y-i
	print i*"$" + x*"#"
	i=i+1

#####################################
print 
print 

import sys
x=1 
while x<6: 
	y=0 
	while y<x:
		sys.stdout.write("$")
		y=y+1 
	y=6 
	while x<y: 
		sys.stdout.write("#")
		y=y-1 
	print 
	x=x+1
