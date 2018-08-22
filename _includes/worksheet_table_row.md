{% for ws in site.data.worksheets %}| {{ ws.day }} | [{{ws.topic}}]({{ws.file}}){% if ws.note %}<br>ws.note{% endif %} | {% if ws.solutions %} [Solutions]({{ws.solutions}}) {% endif %}
{% endfor %}
