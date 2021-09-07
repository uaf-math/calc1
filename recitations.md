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
  <td>{{ c.week }}</td>
  <td>
    {% for s in c.sections %}
      {{ s.date }}
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      {{ s.topic }}
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/recitations/{{s.blank}}">blank</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/recitations/{{s.filled}}">filled</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/recitations/{{s.video}}">video</a><br>
    {% endfor %}
 </td>
</tr>
{% endfor %}
</table>
</div>
