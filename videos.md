---
layout: course-page
title: Daily Log
---

### Introductory Videos


<div class="x-scroll">
<table class="asst-table">
<tr><th>Chapters</th><th>Topics</th></tr>
{% for c in site.data.videos %}
<tr valign="top">
  <td>{{ c.chapter }}</td>
  <td>
    {% for s in c.sections %}
      <a href="{{s.url}}">{{s.title}}</a><br>
    {% endfor %}
 </td>
</tr>
{% endfor %}
</table>
</div>

