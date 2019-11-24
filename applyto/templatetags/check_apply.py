from django import template
from django.db.models import Q
from users import models as user_models
from applyto import models

register = template.Library()


@register.simple_tag(takes_context=True)
def check_apply(context, project):
    try:
        ck_apply = models.Apply.objects.get(
            Q(apply_user=context.request.user) & Q(project=project)
        )
        return True
    except models.Apply.DoesNotExist:
        return False
