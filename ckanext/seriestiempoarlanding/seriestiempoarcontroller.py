from ckan.lib.base import BaseController
import logging
logger = logging.getLogger(__name__)


class SeriesTiempoArController(BaseController):

    def test(self):
        return ckan.lib.base.render('config/config_01_title.html')
