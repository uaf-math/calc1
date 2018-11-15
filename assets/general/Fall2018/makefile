all: MATH251-Schedule-F2018.pdf

# see README-schedule.md
MATH251-Schedule-F2018.pdf: schedule.yml MATH251-Schedule-F2018.tex
	python3 schedule-yml-to-tex.py > schedule-auto.tex
	pdflatex MATH251-Schedule-F2018.tex

.PHONY: clean

clean:
	@rm -f schedule-auto.tex *.pyc *.out *.aux *.log *.bbl *.blg *.synctex.gz *~
