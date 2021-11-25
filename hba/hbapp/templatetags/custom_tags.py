from django import template
register=template.Library()
@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success text-light'
    else:
        return 'bg-danger text-light'
