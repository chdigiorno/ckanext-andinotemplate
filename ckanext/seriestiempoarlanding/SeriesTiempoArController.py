import ckan.lib.base as base
from base import BaseController


class SeriesTiempoArController(BaseController):

    def test(self):
        print("CONTROLLER")
        print("CONTROLLER")
        print("CONTROLLER")
        print("CONTROLLER")
        return base.render('template_test.html')
