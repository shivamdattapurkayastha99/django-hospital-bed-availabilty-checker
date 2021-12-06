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
@register.simple_tag
def is_state_selected(selected_state,pk):
    if selected_state==str(pk):
        return 'selected'
@register.simple_tag
def is_city_selected(selected_city_id,pk):
    if selected_city_id==str(pk):
        return 'selected'
    
@register.simple_tag
def is_option_selected(selected_option,pk):
    if selected_option==str(pk):
        return 'selected'
    return ''