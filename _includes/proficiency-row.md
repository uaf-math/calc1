{% assign data = include.data %}
<tr>
	<td>{{ data.semester }}</td>
	<td> 
		{% for prof in data.derivative.versions %}		
		<table class="inner"><tr><td>{{ prof.name }}:</td><td><a href="{{ data.home }}/{{ prof.blank }}">blank</a></td></tr>
			<tr><td></td><td><a href="{{ data.home }}/{{ prof.solutions }}">solutions</a></td></tr>
		</table><br>
		{% endfor %}
	</td>
	<td> 
		{% for prof in data.integral.versions %}		
		<table class="inner"><tr><td>{{ prof.name }}:</td><td><a href="{{ data.home }}/{{ prof.blank }}">blank</a></td></tr>
			<tr><td></td><td><a href="{{ data.home }}/{{ prof.solutions }}">solutions</a></td></tr>
		</table><br>
		{% endfor %}
	</td>
</tr>
