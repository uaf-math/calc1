{% assign data = include.data %}
<table class="asst-table">
{% for hw in data.homework %}
<tr>
	<td>{{ hw.name }}</td>
	<td>
		<table class="inner">
		  <tr>
			    <td><a href="{{ data.home }}/{{ hw.problems }}">blank</a></td>
		  </tr>
		</table>
		<div style="padding-bottom: 10px"></div>
	</td>
</tr>
{% endfor %}
</table>
