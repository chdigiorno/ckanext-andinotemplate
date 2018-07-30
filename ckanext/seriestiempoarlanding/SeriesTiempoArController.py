import ckan.lib.base as base
from base import BaseController


class SeriesTiempoArController(BaseController):

    def test(self):
        return base.render('template_test.html')
