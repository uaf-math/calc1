---
layout: course-page
title: Math F251 Calculus I at UAF
---

### In-person Worksheets

<div class="x-scroll">
<table class="asst-table">
<tr><th>Name</th><th>Topic</th><th>Sheets</th></tr>
{% for c in site.data.ipworksheets-s2023 %}
<tr valign="top">
  <td>
    {{ c.name }}
  </td>
  <td>
    {{ c.topic }}
  </td>
  <td>
    <table class="inner">
      <tr>
         <td> <a href="{{ c.urlblank }}">blank</a> </td>
      </tr>
      <tr>
         <td> <a href="{{ c.urlfilled }}">filled</a> </td>
      </tr>
      <tr>
         <td>
          {% for s in c.sections %}
          <a href="{{s.urlvideo}}">{{s.title}}</a><br>
          {% endfor %}
         </td>
      </tr>
    </table>
  </td>
</tr>
{% endfor %}
</table>
</div>
