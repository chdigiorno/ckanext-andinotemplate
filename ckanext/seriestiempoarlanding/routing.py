from ckanext.gobar_theme.routing import GobArRouter


class SeriesTiempoArRouter(GobArRouter):

    def __init__(self, route_map):
        self.api_controller = 'ckanext.seriestiempoarlanding.controller:SeriesTiempoArController'

    def redirect(self, *routes):
        for url_from, url_to in routes:
            self.route_map.redirect(url_from, url_to)

    def set_routes(self):
        self.connect_test()

    def connect_test(self):
        self.home_routes.connect('test', '/test', action='test')
