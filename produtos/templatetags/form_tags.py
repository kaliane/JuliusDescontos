from django import template

register = template.Library()

@register.filter
def field_type(produto_field):
    return produto_field.field.widget.__class__.__name__

@register.filter
def input_class(produto_field):
    css_class = ''
    if produto_field.form:
        if produto_field.errors:
            css_class = 'is-invalid'
        elif field_type(produto_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)