# generating the schedule PDF

The schedule is created in a multi-step process.  The file `schedule.yml` is a database that lists topics, exam days, etc.  Edit this to create or modify the schedule.  To generate the schedule as a PDF you may be able to just type

	make

If you get an error about `import yaml` then consider doing

	PYTHON=python3 make


### manual version

If this does not work, here is the manual version, which also documents the `makefile`.

The python script `schedule-yml-to-tex.py` converts the data in the `schedule.yml` file to a snippit of LaTeX code consisting of tables for each week of the course:
Navigate to the directory where everything is kept, and then run the commandline command:

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
	
# Changes in Fall 2020

	python schedule-yml-to-tex-WRHtoDH.py > schedule-auto.tex

The .yml file used is 
	schedule-yml-to-tex-WRHtoDH
	
So you need to go into the directory where things live, (which you can do by having set up a link to iCloud, 

type
	ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs ~/iCloud

otherwise go to
	~/Library/Mobile Documents/com~apple~CloudDocs
and then navigate to the correct folder in the GitHub directory structure)

type into the terminal: 	python3 schedule-yml-to-tex-WRHtoDH.py > schedule-auto.tex

This changes from WRH for written homework to DH for daily homework.

We're also back to evening exams, so we're using slots A and B, this time not only for midterms but also for proficiencies.	

