from ckanext.gobar_theme.routing import GobArRouter
from routes.mapper import SubMapper
import logging
logger = logging.getLogger(__name__)


class SeriesTiempoArRouter(GobArRouter):

    def __init__(self, route_map):
        self.test_controller = 'ckanext.seriestiempoarlanding.controller:SeriesTiempoArController'

    def set_routes(self):
        self.connect_test()

    def connect_test(self):
        with SubMapper(self.route_map, controller=self.test_controller) as m:
            m.connect('test', '/test', action='test')
