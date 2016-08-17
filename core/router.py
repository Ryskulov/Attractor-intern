from exceptions import RouteNotFoundException
from views import handle_404
import os
import settings
import re


ROUTE_NOT_FOUND_EXCEPTION_MESSAGE = 'Route for method {method} and path {path} not found'


class Router(object):
    def __init__(self):
        self.routes = []

    def handle(self, request):
        try:
            handler = self._get_handler_for_path(request.command, request.path)
            handler(request)
        except RouteNotFoundException:
            handle_404(request)

    def register_routes(self, routes):
        if type(routes) != list:
            raise TypeError("Routes must be list")
        self.routes.extend(routes)

    def _get_handler_for_path(self, method, path):
        for route in self.routes:
            if route.check_method_and_path(method, path):
                return route.get_handler()
        raise RouteNotFoundException(ROUTE_NOT_FOUND_EXCEPTION_MESSAGE.format(method=method, path=path))


class Url(object):
    def __init__(self, method, path, handler):
        self.method = method
        self.path = path
        self.handler = handler

    def get_handler(self):
        return self.handler

    def get_url(self):
        return self.path

    def check_method_and_path(self, method, path):
        if self.path == '/media/' and os.path.isfile(settings.MEDIA_DIR + path):
            return True
        if self.path == '/static/' and os.path.isfile(settings.STATIC_DIR + path):
            return True
        else:
            if re.match(self.path, path) and self.method == method:
                return True
            else:
                return False
