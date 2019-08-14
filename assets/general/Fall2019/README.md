# generating the schedule PDF

The schedule is created in a multi-step process.  The file `schedule.yml` is a database that lists topics, exam days, etc.  Edit this to create or modify the schedule.  To generate the schedule as a PDF you may be able to just type

	make

If you get an error about `import yaml` then consider doing

	PYTHON=python3 make


### manual version

If this does not work, here is the manual version, which also documents the `makefile`.

The python script `schedule-yml-to-tex.py` converts the data in the `schedule.yml` file to a snippit of LaTeX code consisting of tables for each week of the course:

	python schedule-yml-to-tex.py > schedule-auto.tex

(If error try `python3`.)  Then the file `MATH251-Schedule.tex` imports the auto-generated tables to make the final copy of the schedule.

	pdflatex MATH251-Schedule.tex

# generating the syllabus PDF

Just LaTeX it:

	pdflatex MATH251-Syllabus.tex
	
# changes in Fall 2019

Because we gave midterms in the usual classtimes and not in the evening, they python code was changed to omit the "slot A" and "slot B" items in the schedule. This file named:
	
	schedule-yml-to-tex-new.py
	
is the file used in Fall 2019.

The .yml file with the "slot A" and "slot B" syntax is called 

	schedule-with-evening-midterms.yml

