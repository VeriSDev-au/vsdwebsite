import markdown
from django import template
from django.template.defaultfilters import stringfilter

import timeago, datetime

register = template.Library()

# Detect active/selected SideBar Menu based on the routing
@register.simple_tag(takes_context=True)
def is_active_view(context, *view_names):
    request = context.get("request")
    for view_name in view_names:
        if getattr(request.resolver_match, "view_name", "") == view_name:
            return ""
    return "collapsed"


@register.filter
@stringfilter
def convert_markdown(value):
    return markdown.markdown(value, extensions=["markdown.extensions.fenced_code"])


@register.filter
@stringfilter
def convert_timeago(value):
    now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
    return timeago.format(datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ"), now)[
        :-4
    ]


@register.filter
@stringfilter
def remove_GitHubOwnerName(value):
    return value[12:]
