{% assign data = include.data %}
<tr>
	<td>{{ data.semester }}</td>
	<td> 
	{% if data.midterm1.versions %}
		{% for exam in data.midterm1.versions %}
		<table class="inner"><tr><td>{{ exam.name }}:</td><td><a href="{{ data.home }}/{{ exam.blank }}">blank</a></td></tr>
			<tr><td></td><td><a href="{{ data.home }}/{{ exam.solutions }}">solutions</a></td></tr>
		</table><br>
		{% endfor %}
	{% else %}
		<a href="{{ data.home }}/{{ data.midterm1.blank }}">blank</a><br>
		<a href="{{ data.home }}/{{ data.midterm1.solutions }}">solutions</a><br>
	{% endif %}	
	</td>
	<td> 
	{% if data.midterm2.versions %}
		{% for exam in data.midterm2.versions %}		
		<table class="inner"><tr><td>{{ exam.name }}:</td><td><a href="{{ data.home }}/{{ exam.blank }}">blank</a></td></tr>
			<tr><td></td><td><a href="{{ data.home }}/{{ exam.solutions }}">solutions</a></td></tr>
		</table><br>
		{% endfor %}
	{% else %}
		<a href="{{ data.home }}/{{ data.midterm2.blank }}">blank</a><br>
		<a href="{{ data.home }}/{{ data.midterm2.solutions }}">solutions</a><br>
	{% endif %}	
	</td>
</tr>
