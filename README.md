
[![Build Status](https://travis-ci.org/datosgobar/ckanext-andinotemplate.svg?branch=master)](https://travis-ci.org/datosgobar/ckanext-andinotemplate)

[![Docs Status](https://readthedocs.org/projects/ckanext-andinotemplate/badge/?version=master)](http://ckanext-andinotemplate.readthedocs.io/es/master/)

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

4. Editar el archivo de configuración de Andino `/etc/ckan/default/production.ini` dentro del contenedor `portal` y agregar el setting `andino.base_page = andino_custom_base_page.html`, provisto por `ckanext-andinotemplate`.

5. Reiniciá Andino.

## Funcionalidades base

El plugin template default permite agregar a tu instancia de Andino dos puntos de menú en la navegación superior de Andino:

* Andino: Al hacer click redirige a la [documentación oficial de Portal Andino](http://portal-andino.readthedocs.io/).
* Nueva Sección: Es una demostración de cómo agregar una ṕágina de contenido estático en Andino.
