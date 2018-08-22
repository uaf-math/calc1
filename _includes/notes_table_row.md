{% for n in site.data.notes %}| {{ n.day }} | {% if n.placeholder %} {{ n.topic }}:<br>{{n.placeholder}} | {% else %} [{{ n.topic }}]({{ n.file }}) | {% endif %}
{% endfor %}
