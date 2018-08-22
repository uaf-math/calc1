{% for asst in site.data.assignments %}| {{ asst.week }} | {{asst.reading}} | {{asst.assignment}} | {{asst.due}} | {{asst.solutions}} |
{% endfor %}
