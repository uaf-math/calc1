---
layout: course-page
title: Math F251 Calculus I at UAF
---

### Tuesday Recitation Materials

<div class="x-scroll">
<table class="asst-table">
<tr><th>Week</th><th>Date</th><th>Topic</th><th>Blank Sheets</th><th>Filled Sheets</th><th>Videos</th></tr>
{% for c in site.data.recitations_f2023 %}
<tr valign="top">
  <td>
    {{ c.Week }}
 </td>
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
      <a href="assets/recitations/Spring2022/{{s.blank}}">blank</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/recitations/Spring2022/{{s.filled}}">filled</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="{{s.video}}">video</a><br>
    {% endfor %}
 </td>
</tr>
{% endfor %}
</table>
</div>
