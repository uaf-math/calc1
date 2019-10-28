from pbpic import *
from pbpic.geometry import BBox
from pbpic.graph import graph, xtick

#style.setstyle(arrow,tip=arrow.ArrowHead(width=5,length=5,wingangle=1/6.))
arrow=arrow.ArrowTo()

xmin=-1; xmax=1
ymin=-1; ymax=1

label = ["a","b"]
lsign = ["$+$","$-$"]
rsign = ["$-$","$+$"]
for k in (0,1):
	pbpbegin(6*cm,2*cm,'Fig-4-3%s.pdf' % label[k])
	w=BBox()
	moveto(loc.ne); rmoveto(-5*pt,0); w.include(currentpoint());
	moveto(loc.sw); rmoveto(30*pt,0); w.include(currentpoint());
	window(w, BBox((xmin,ymin),(xmax,ymax)) )

	moveto(xmin,0)
	lineto(xmax,0)
	moveto(0,0)
	rmoveto(0,4*pt)
	rlineto(0,-8*pt)
	stroke()

	moveto(0,0)
	rmoveto(0,-8*pt)
	drawtex('-3',origin=loc.north)

	moveto(-0.5,0)
	rmoveto(0,8*pt)
	drawtex(lsign[k],origin=loc.center)

	moveto(+0.5,0)
	rmoveto(0,8*pt)
	drawtex(rsign[k],origin=loc.center)

	moveto(0,0)
	rmoveto(0,-8*pt)
	drawtex('-3',origin=loc.north)
	moveto(-1,0)
	rmoveto(-4*pt,0)
	drawtex(r"$f'(x)$",origin=loc.east)

	pbpend()

