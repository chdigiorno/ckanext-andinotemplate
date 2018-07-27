.. image:: https://travis-ci.org/chdigiorno/ckanext-seriestiempoarlanding.svg?branch=master
    :target: https://travis-ci.org/chdigiorno/ckanext-seriestiempoarlanding

.. image:: https://coveralls.io/repos/chdigiorno/ckanext-seriestiempoarlanding/badge.svg
  :target: https://coveralls.io/r/chdigiorno/ckanext-seriestiempoarlanding

.. image:: https://pypip.in/download/ckanext-seriestiempoarlanding/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-seriestiempoarlanding/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-seriestiempoarlanding/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-seriestiempoarlanding/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-seriestiempoarlanding/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-seriestiempoarlanding/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-seriestiempoarlanding/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-seriestiempoarlanding/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-seriestiempoarlanding/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-seriestiempoarlanding/
    :alt: License

# ckanext-seriestiempoarlanding

Template de SeriesTiempoArLandingPlugin para Andino. Este repositorio es una muestra de cómo implementar un plugin base para una instancia de Andino y agregar funcionalidades extendiendo el plugin.


## Instalación

Para instalar `ckanext-seriestiempoarlanding`:

1. Activá el _virtualenv_ de tu instancia de CKAN:

     . /usr/lib/ckan/default/bin/activate

2. Instalá el paquete de Python `ckanext-seriestiempoarlanding` dentro del _virtualenv_:

     pip install -e git+https://github.com/chdigiorno/ckanext-seriestiempoarlanding.git#egg=ckanext-seriestiempoarlanding

3. Agregá `seriestiempoarlanding` a la lista de `ckan.plugins` en tu archivo de configuración de CKAN
   (por defecto ubicada en `/etc/ckan/default/production.ini` dentro del contenedor `portal`).

4. Reiniciá Andino.
