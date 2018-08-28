---
layout: course-page
title: "Class Materials: Spring 2018"
---

## Course Materials: Spring 2018

* [Syllabus](assets/materials/Spring2018/M251_Calculus-I_Syllabus_Spring_18.pdf)
* [Schedule](assets/materials/Spring2018/M251Sp18_weekly_schedule.pdf)
* [Grading Rubric](assets/materials/Spring2018/GradingRubric_Spring18.pdf)
* [Sections](assets/materials/Spring2018/Calculus-1-Spring-2018-Instructor-Section-Info.pdf)


### Special Worksheet for Section 2.1

On Wednesday, January 24 we will have a worksheet that uses a Google Docs spreadsheet.  If you can bring a laptop on Wednesday, please do so.  Before you come to class, please verify you can create your own copy of the spreadsheet by doing the following.

1. If you are not already logged into a Google account, go to the 
[UAF Google page](https://www.alaska.edu/google) and log in with your UA ID and password.
2. After you have logged in, open the [spreadsheet](https://docs.google.com/spreadsheets/d/1ZdWufP2aBqipwtwqXYWFmYr4FkUJAlChJ2TGY-2LWlA).  You will not be able to edit this copy.
3. In the spreadsheet's **File** menu, select **Make a Copy...** and create a copy for yourself.
4. When opening the the new spreadsheet, be patient.  It can take a little time for it to fully load at first, and you may initially see error messages.  Fear not.  But if it comes to it, reload the page.

### Lecture Notes (Section F02: Faudree)
{% assign data = site.data.materials-s2018.lecture-notes %}
{% assign home = site.data.materials-s2018.lecture-notes.home %}
<table class="asst-table">
{% for item in data.items %}
{% if item.special %}
  {% if item.file %}
  <tr>
  	<td><b><a href="{{home}}/{{item.file}}">{{ item.special}}</a></b></td><td></td>
  </tr>
  {% else %}
  <tr>
  	<td><b>{{ item.special }}</b></a></td>
  	<td>
        <table class='inner'>
  	       <tr><td><a href="{{ home }}/{{ item.blank }}">blank</a></td></tr>
           <tr><td><a href="{{ home }}/{{ item.filled }}">filled</a></td></tr>
        </table>  		
  	</td>
  </tr>
  {% endif %}

{% endif %}
{% if item.chapter %}
<tr><td><b>Chapter {{ item.chapter }}</b></td><td></td></tr>
{% for section in item.notes %}
<tr>
	<td>{{ section.topic }}</td>
	<td> <table class='inner'>
  	       <tr><td><a href="{{ home }}/{{ item.subhome }}/{{ section.blank }}">blank</a></td></tr>
           <tr><td><a href="{{ home }}/{{ item.subhome }}/{{ section.filled }}">filled</a></td></tr>
        </table>
   </td>
</tr>
{% endfor %}
{% endif %}
{% endfor %}
</table>
