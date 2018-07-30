import ckan.lib.base as base
from base import BaseController
import logging
logger = logging.getLogger(__name__)


class SeriesTiempoArController(BaseController):

    def test(self):
        logger.info('CONTROLLER')
        logger.info('CONTROLLER')
        logger.info('CONTROLLER')
        logger.info('CONTROLLER')
        logger.info('CONTROLLER')
        return base.render('template_test.html')
