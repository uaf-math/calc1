all: MATH251-Schedule.pdf

# see README-schedule.md
MATH251-Schedule.pdf: schedule.yml MATH251-Schedule.tex
	python schedule-yml-to-tex.py > schedule-auto.tex
	pdflatex MATH251-Schedule.tex

MATH251-Syllabus.pdf: MATH251-Syllabus.tex
	pdflatex MATH251-Syllabus.tex

.PHONY: clean

clean:
	@rm -f schedule-auto.tex *.pyc *.out *.aux *.log *.bbl *.blg *.synctex.gz *~
