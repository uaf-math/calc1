---
layout: course-page
title: Daily Log
---

### Introductory Videos

The chapter and section numbers for these videos are aligned with a previous text and should be ignored. The *topics* are the same as our text.


<div class="x-scroll">
<table class="asst-table">
<tr><th>Chapters</th><th>Topics</th><th>Slides</th></tr>
{% for c in site.data.videos %}
<tr valign="top">
  <td>{{ c.chapter }}</td>
  <td>
    {% for s in c.sections %}
      <a href="{{s.url}}">{{s.title}}</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/intro-videos/{{s.pdf}}">slides</a><br>
    {% endfor %}
 </td> 
</tr>
{% endfor %}
</table>
</div>

