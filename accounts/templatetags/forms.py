from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def sum_total(items):
    return sum(item[0] * item[1].price for item in items)