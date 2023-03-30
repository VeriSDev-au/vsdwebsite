"""
Utility to allow having python script inside HTML Template

"""

import datetime
import timeago

import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active_view(context, *view_names):
    """Detect active/selected SideBar Menu based on the routing"""
    request = context.get("request")
    for view_name in view_names:
        if getattr(request.resolver_match, "view_name", "") == view_name:
            return ""
    return "collapsed"


@register.filter
@stringfilter
def convert_markdown(value):
    """Allow to convert markdown format and render it as HTML to the client"""
    return markdown.markdown(value, extensions=["markdown.extensions.fenced_code"])


@register.filter
@stringfilter
def convert_timeago(value):
    """Convert the datetime, compare with the UTC time and display as time ago"""
    now = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 3.4)
    return timeago.format(datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ"), now)[
        :
    ].replace("minutes", "mins")


@register.filter
@stringfilter
def convert_timeago_color_code(value):
    """Display the color of timeline in dashboard based on time ago"""
    result_timeago = convert_timeago(value)
    if "min" in result_timeago:
        return "text-danger"
    elif "hour" in result_timeago:
        return "text-primary"
    elif "day" in result_timeago:
        return "text-info"
    elif "week" in result_timeago:
        return "text-warning"
    else:
        return "text-success"


@register.filter
@stringfilter
def remove_gh_owner_name(value):
    """Remove GitHub source code owner to simplify the display"""
    return value[12:]
