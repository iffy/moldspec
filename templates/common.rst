{%- macro prop(name, data) -%}
``{{ name }}``{% if data.required %} **(required)**{% endif %}
    ``{{ data.type }}``{% if data.pattern %} matching ``"{{ data.pattern }}"``{% endif %}
    
    {{ data.title + ' - ' if data.title }}{{ data.description }}
{%- endmacro -%}

{%- set title = '%s' % (doctype,) -%}
{{ title|title }}
{{'-' * title|length }}

{% if schema.properties %}

{% for name,data in schema.properties|dictsort %}
{% if data.required %}{{ prop(name, data) }}{% endif %}
{% endfor -%}
{%- for name,data in schema.properties|dictsort %}
{% if not data.required %}{{ prop(name, data) }}{% endif %}
{% endfor %}
{% endif %}