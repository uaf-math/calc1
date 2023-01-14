---
layout: course-page
title: Math F251 Calculus I at UAF
---

### In-person Worksheets

<div class="x-scroll">
<table class="asst-table">
<tr><th>Section</th><th>Topic</th><th>Blank Sheets</th><th>Filled Sheets</th>
{% for c in site.data.ipworksheets-s2023 %}
<tr valign="top">
  <td>
    {{ c.Section }}
 </td>
  <td>
    {% for s in c.sections %}
      {{ s.topic }}
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/ipworksheets/s2023/{{s.blank}}">blank</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="assets/ipworksheets/s2023/{{s.filled}}">filled</a><br>
    {% endfor %}
 </td>
</tr>
{% endfor %}
</table>
</div>
