from ckanext.gobar_theme.routing import GobArRouter
from routes.mapper import SubMapper


class SeriesTiempoArRouter(GobArRouter):

    def __init__(self, route_map):
        self.test_controller = 'ckanext.seriestiempoarlanding.controller:SeriesTiempoArController'

    def set_routes(self):
        self.connect_test()

    def connect_test(self):
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        print("ROUTING")
        with SubMapper(self.route_map, controller=self.test_controller) as m:
            m.connect('test', '/test', action='test')
