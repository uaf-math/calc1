#!/usr/bin/env python3

from datetime import date, timedelta
import yaml

def str_to_date(s):
	month, day, year = map(int, s.split("/"))
	return date(year, month, day)

class TableEntry:

	def __init__(self):
		self.value = "&"
		self.eol_pending = False

	def addline(self, line):
		if self.eol_pending:
			self.value +=  r"\newline "
		self.value += line
		self.eol_pending = True


dayStep = timedelta(1)

with open('schedule.yml') as f:
	schedule=yaml.load(f)
start_date = str_to_date(schedule['start'])

week_number = 1
recitation_number = 1
quiz_number = 0 
midterm_number = 1
homework_number = 1

preamble = r"""
% !TEX TS-program = pdflatexmk
\documentclass[12pt]{article}
% Layout.
\usepackage[top=1in, bottom=0.75in, left=1in, right=1in, headheight=1in, headsep=6pt]{geometry}
% Fonts.
\usepackage{mathptmx}
\usepackage[scaled=0.86]{helvet}
\renewcommand{\emph}[1]{\textsf{\textbf{#1}}}
% Misc packages.
\usepackage{amsmath,amssymb,latexsym}
\usepackage{graphicx}
\usepackage{array}
\usepackage{xcolor}
\usepackage{multicol}
\usepackage{tabularx,colortbl}
% Paragraph spacing
\parindent 0pt
\parskip 6pt plus 1pt
\usepackage{fancyhdr}
\pagestyle{fancy} 
\lhead{\large\sf\textbf{MATH 251 Calculus I}}
\chead{\large\sf\textbf{Weekly Schedule}}
\rhead{\large\sf\textbf{Fall 2018}}
\begin{document}
\begin{itemize}
\item \textbf{WebAssign} homework (\textcolor{red}{WA}) is due by 10PM on the due date. \item \textbf{Written} homework (\textcolor{blue}{WRH}) is due at the beginning of Recitation.\end{itemize}
"""
trailer = r"""\end{document}"""

top_table = r"""
\begin{tabularx}{\textwidth}{|l|| >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X |}
\hline
&Monday & Tuesday & Wednesday & Thursday & Friday \\
\hline \hline
"""
table = r"""
\begin{tabularx}{\textwidth}{|l|| >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X | >{\raggedright\arraybackslash}X |}
\hline
"""
end_table = r"""\end{tabularx}"""


def date_row(week_number, start):
	row = r"""\rowcolor{gray!20} Week %d""" % week_number
	date = start
	dayStep = timedelta(1)
	for k in range(5):
		row = row + "&%02d/%02d" % (date.month,date.day)
		date += dayStep
	row = row + r"""\\
	\hline"""
	return row


def topic_row(week_start, days):
	global recitation_number
	global midterm_number
	global quiz_number

	row = r"""Topics"""
	for d in range(5):
		day = d + week_start
		entry = TableEntry()
		try:
			today = days[week_start + d]
		except:
			row += entry.value
			continue
		if 'class' in today:
			entry.addline(today['class'])
		elif 'special' in today:
			pass
		elif 'recitation' in today:
			if today['recitation'] == None:
				entry.addline(r"\textbf{Recitation %d}" % recitation_number)
			else:
				entry.addline(r"\textbf{Recitation %d:}\newline %s" % (recitation_number,today['recitation']))
			recitation_number += 1
		elif 'holiday' in today:
			entry.addline(today['holiday'])
		elif 'midterm' in today:
			entry.addline(r"\textbf{\textcolor{dcyan}{Midterm %d:}}" % midterm_number)
			entry.addline(today['midterm'])
			midterm_number += 1
			slot = ord('A')
			for t in today['exam-times']:
				entry.addline(r"\textcolor{ddgreen}{Slot %s: %s}" % (chr(slot),t) )
				slot += 1
		elif 'final' in today:
			entry.addline(r"\textcolor{dcyan}{FINAL EXAM}")
			entry.addline(r"Time: %s" % today["final"]["time"])
		else:
			raise "missing day type"
		if 'quiz' in today:
			entry.addline(r"Quiz %d: %s" % (quiz_number, today['quiz']))
			quiz_number += 1
		if 'proficiency' in today:
			entry.addline(r"\textbf{\textcolor{dcyan}{%s Proficiency}}" % (today['proficiency']))
		if 'aleks_quiz' in today:
			entry.addline(r"ALEKS Quiz %d" % quiz_number)
			entry.addline(today['aleks_quiz']['location'])
			quiz_number += 1
		row += entry.value
	row += r"""\\
	\hline"""
	return row


def deadline_row(week_start, days):
	global recitation_number
	global midterm_number
	global homework_number

	row = r"""Deadlines"""
	for d in range(5):
		day = d + week_start
		entry = TableEntry()
		try:
			today = days[week_start + d]
		except:
			row += entry.value
			continue
		if 'deadline' in today:
			entry.addline(r"""\textcolor{ddgreen}{%s}""" % today['deadline'])
		if 'homework' in today:
			entry.addline(r"""\textcolor{blue}{WRH %d}""" % homework_number)
			homework_number += 1
		if 'webassign' in today:
			entry.addline(r"""\textcolor{red}{WA \S%s}""" % today['webassign'])
		row += entry.value

	row += r"""\\
	\hline"""
	return row


offset = start_date.weekday()
course_day = 0


days = schedule['schedule']

end_day = len(days) + offset


week_start = start_date - start_date.weekday()*dayStep
while course_day < end_day:

	if week_number == 1:
		print(top_table)
	else:	
		print(table)
	print(date_row(week_number, week_start))

	print(topic_row(course_day, days))
	print(deadline_row(course_day, days))
	print(end_table)
	print(r"\vskip 12pt\par")


	week_start = week_start + 7*dayStep
	week_number += 1
	course_day += 5
