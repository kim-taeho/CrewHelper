from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_Finished(context, project_job):
    if project_job.isFinished is True:
        return True
    else:
        return False
