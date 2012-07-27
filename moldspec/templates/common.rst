{% macro renderSchema(schema) %}
{% if schema.properties %}

{% for name,data in schema.properties|dictsort %}
{% if data.required %}{{ _prop(name, data) }}{% endif %}
{% endfor -%}
{%- for name,data in schema.properties|dictsort %}
{% if not data.required %}{{ _prop(name, data) }}{% endif %}
{% endfor %}
{% endif %}
{% endmacro %}

{% macro _prop(name, data) %}
``{{ name }}``{% if data.required %} **(required)**{% endif %}
    ``{{ data.type }}``{% if data.pattern %} matching ``"{{ data.pattern }}"``{% endif %}
    
    {{ data.title + ' - ' if data.title }}{{ data.description }}
{% endmacro %}
