{% for recitation in include.data %}
### {{recitation.name}}

<table style="border-spacing:10px">
{% for v in quiz.versions %}
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
      <a href="{{s.blank}}">blank</a><br>
    {% endfor %}
 </td>
  <td>
    {% for s in c.sections %}
      <a href="{{s.filled}}">filled</a><br>
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
{% endfor %}
