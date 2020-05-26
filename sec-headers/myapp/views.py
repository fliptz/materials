import logging

from django.http import HttpResponse

logger = logging.getLogger("django.server")


def index(request):
    logger.info(request.headers)
    return HttpResponse(
        """\
<!DOCTYPE html>
<html lang="en-US">
  <head><meta charset="utf-8"><title>My secure app</title></head>
  <body><p>Now this is some sweet HTML!</p></body>
</html>"""
    )
