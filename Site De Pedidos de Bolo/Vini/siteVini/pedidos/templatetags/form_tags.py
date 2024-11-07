from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adiciona uma classe CSS ao campo do formulário."""
    return field.as_widget(attrs={'class': css_class})
