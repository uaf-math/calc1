{% assign data = include.data %}
<table class="asst-table">
{% for hw in data.homework %}
<tr>
	<td>{{ hw.name }}</td>
	<td>
		<table class="inner">
		  <tr>
			    <td><a href="{{ data.home }}/{{ hw.problems }}">problems</a></td>
		  </tr>
		</table>
	</td>
</tr>
{% endfor %}
</table>
