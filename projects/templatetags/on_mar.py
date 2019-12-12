from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def on_mar(context, project):
    if project.on_market is True:
        return True
    else:
        return False
