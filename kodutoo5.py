# -*- coding: utf8 -*-

#ÜL1
tekst = raw_input("Palun sisestage tekst: ")

if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "Väiketähed ja numbrid"
elif tekst == str(tekst.lower()):
	print "Väiketähed ja numbriteta"
elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Suurtähed ja numbrid" 
elif tekst == str(tekst.upper()):
	print "Suurtähed ja numbriteta"
elif any(c.isdigit() for c in tekst):
	print "Suur-väiketähed ja numbrid"
else:
	print "Suur-väiketähed ja numbriteta"

#ÜL2
arv1 = int(raw_input("Sisestage esimene arv: "))
arv2 = int(raw_input("Sisestage teine arv: "))
if arv1<arv2:
	x=arv1
	y=arv2+1
else:
	x=arv2
	y=arv1+1

i=0
for arvx in range(x, y):
	if arvx % 3 == 0:
		i = i+1;
		
print i
