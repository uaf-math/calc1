# generating the schedule PDF

The schedule is created in a multi-step process.  The file `schedule.yml` is a database that lists topics, exam days, etc.  Edit this to create or modify the schedule.  To generate the schedule as a PDF you may be able to just type

	make

### manual version

If this does not work, here is the manual version, which also documents the `makefile`.

The python script `schedule-yml-to-tex.py` converts the data in the `schedule.yml` file to a snippit of LaTeX code consisting of tables for each week of the course:

	python3 schedule-yml-to-tex.py > schedule-auto.tex

Then the file `MATH251-Schedule.tex` imports the auto-generated tables to make the final copy of the schedule.

	pdflatex MATH251-Schedule.tex

# generating the syllabus PDF

Just LaTeX it:

	pdflatex MATH251-Syllabus.tex

