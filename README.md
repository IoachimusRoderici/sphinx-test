# Pruebas con Sphinx

La imagen se construye con `docker build -t doctest .`.

Los documentos se construyen con
- `docker run --rm -u $(id -u):$(id -g) -v .:/docs doctest make pdf`
- `docker run --rm -u $(id -u):$(id -g) -v .:/docs doctest make html`