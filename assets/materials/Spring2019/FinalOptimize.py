from pbpic import *
from pbpic.geometry import BBox
from pbpic.graph import graph, xtick

#style.setstyle(arrow,tip=arrow.ArrowHead(width=5,length=5,wingangle=1/6.))
# style.pbptex.preamble = r"\documentclass[12pt]{article}\usepackage[lf]{minionpro}\pagestyle{empty}\begin{document}"
pbpstyle.setstyle(pbptex,preamble=r"\documentclass[12pt]{article}\usepackage[lf]{minionpro}\pagestyle{empty}\begin{document}")
arrow=arrow.ArrowTo()

f=lambda x: 1./(x+1.)
L = 2
W = 5.
xmax=3; ymax=1.2
pbpbegin(10*cm,5*cm,'pdf')
scaleto(1*cm)
translate(loc.center)
dx=7.; dy=3.
moveto(-dx/2,-dy/2)
build(paths.rect,dx,dy); stroke()

moveto(0,-dy/2); rmoveto(0,-6*pt)
drawtex('metal',origin=loc.north)
moveto(0,dy/2); rmoveto(0,6*pt)
drawtex('metal',origin=loc.south)

moveto(dx/2,0); rmoveto(5*pt,0)
drawtex('metal',origin=loc.west)

moveto(-dx/2,0); rmoveto(-5*pt,0)
drawtex('brick',origin=loc.east)

moveto(0,0)
drawtex('800 ft$^2$',origin=loc.center)

pbpend()