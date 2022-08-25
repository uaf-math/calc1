---
layout: course-page
title: Syllabi
---

### Syllabi

Links to the syllabi are below. 


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
