---
layout: course-page
title: "Course Materials: Fall 2017"
---

## Course Materials: Fall 2017

* [Syllabus](assets/materials/Fall2017/M251_Calculus-I_Syllabus_Fall_17.pdf)
* [Schedule](assets/materials/Fall2017/M251_weekly_schedule.pdf)
* [Grading Rubric](assets/materials/Fall2017GradingRubric_Fall17.pdf)
* [Sections](assets/materials/Fall2017/Calculus-1-Fall-2017-Instructor-Section-Info.pdf)

### Recitation Worksheets

{% assign data = site.data.materials-f2017.recitations %}
{% assign home = site.data.materials-f2017.recitations.home %}
<table class="asst-table">
<tr><th> Recitation</th><th>Topics</th><th>Worksheet</th></tr>
{% for w in data.worksheets %}
<tr>
	<td>{{ w.name }}</td>
	<td>{{ w.topics }}</td>
	<td> <table class='inner'>
  	       <tr><td><a href="{{ home }}/{{ w.blank }}">blank</a></td></tr>
           <tr><td><a href="{{ home }}/{{ w.filled }}">filled</a></td></tr>
        </table>
   </td>
</tr>
{% endfor %}
</table>

### Lecture Notes

{% assign data = site.data.materials-f2017.lecture-notes %}
{% assign home = site.data.materials-f2017.lecture-notes.home %}
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
