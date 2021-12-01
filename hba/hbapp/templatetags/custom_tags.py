from django import template

from hbapp.models import Availability
register=template.Library()
@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success text-light'
    else:
        return 'bg-danger text-light'
@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')
    
