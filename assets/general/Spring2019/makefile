all: MATH251-Schedule.pdf MATH251-Syllabus.pdf

# see README-schedule.md
schedule-auto.tex: schedule.yml
	python schedule-yml-to-tex.py > schedule-auto.tex

MATH251-Schedule.pdf: schedule-auto.tex MATH251-Schedule.tex
	pdflatex MATH251-Schedule.tex

MATH251-Syllabus.pdf: MATH251-Syllabus.tex
	pdflatex MATH251-Syllabus.tex

.PHONY: clean

clean:
	@rm -f schedule-auto.tex *.pyc *.out *.aux *.log *.bbl *.blg *.synctex.gz *~
