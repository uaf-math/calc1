---
layout: course-page
title: Math F251 Calculus I at UAF
---

### In-person Worksheets

<div class="x-scroll">
<table class="asst-table">
<tr><th>Section</th><th>Topic</th><th>Materials</th></tr>
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
         <td> <a href="{{ c.urlvideo1 }}">video 1 </a><br></td>         
      </tr>
       <tr>
         <td> <a href="{{ c.urlvideo2 }}">video 2 </a><br></td>         
      </tr>
    </table>
  </td>
</tr>
{% endfor %}
</table>
</div>
