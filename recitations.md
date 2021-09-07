---
layout: course-page
title: Math F251 Calculus I at UAF
---

### Tuesday Recitation Materials

<div class="x-scroll">
<table class="asst-table">
<tr><th>Date</th><th>Topic</th><th>Blank Sheets</th><th>Filled Sheets</th><th>Videos</th></tr>
{% for c in site.data.recitations %}
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
