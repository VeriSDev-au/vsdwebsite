from django import template

register = template.Library()

# Detect active/selected SideBar Menu based on the routing
@register.simple_tag(takes_context=True)
def is_active_view(context, *view_names):
    request = context.get("request")
    for view_name in view_names:
        if getattr(request.resolver_match, "view_name", "") == view_name:
            return ""
    return "collapsed"
