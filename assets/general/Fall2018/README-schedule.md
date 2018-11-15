The schedule is created in a multi-step process.

The file `schedule.yml` is a database that lists topics, exam days, etc.  Edit this to create the schedule.

The python script `schedule-yml-to-tex.py` converts the data in the `schedule.yml` file to a snippit of LaTeX code consisting of tables
for each week of the course:

	python schedule-yml-to-tex.py > schedule-auto.tex

Finally, the file `MATH251-Schedule-F2018.tex` imports the auto-generated tables to make the final copy of the schedule.

	pdflatex MATH251-Schedule-F2018.tex


