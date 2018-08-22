{% assign data = include.data %}
<tr>
	<td>{{ data.semester }}</td>
	<td> 
	{% if data.final.versions %}
		{% for exam in data.final.versions %}		
		{{ exam.name }}: <a href="{{ data.home }}/{{ exam.blank }}">blank</a> <a href="{{ data.home }}/{{ exam.solutions }}">solutions</a><br>
		{% endfor %}
	{% else %}
		<a href="{{ data.home }}/{{ data.final.blank }}">blank</a><br>
		<a href="{{ data.home }}/{{ data.final.solutions }}">solutions</a><br>
	{% endif %}	
	</td>
</tr>
