Diseño y implementación del back-end de un e-commerce
=====================================================

Formas parte del equipo de desarollo y en el sprint actual tienes la siguiente tarea:

-------------------------------------------------------------------------------------------------------------------------------

"Back-end: Añadir productos con dto. en cesta y poder aplicar códigos promocionales"

Como propietario de una cadena de tiendas a nivel internacional quiero poder introducir mis productos en el sistema
y que los clientes puedan comprarlos con ciertos descuentos en función del país. También quiero poder crear códigos
promocionales para poder hacer campañas de marketing aplicando un descuento de cierta cantidad de dinero si la
compra supera un mínimo.

*Criterio de aceptación:*
* Se guardan los productos. Estos pueden:
** Tener precios distintos según el país
** Tener un porcentaje de descuento sobre el precio.

* Se pueden aplicar códigos promocionales.
** Consisten en un descuento de una cantidad fija sobre el total de la cesta 
   siempre que este total supere un mínimo.

-------------------------------------------------------------------------------------------------------------------------------

*Aclaraciones*
Por simplicidad, no se considerarán las divisas en las cantidades monetarias.
Es decir, trabajaremos sin unidad guardando solo el número. 15€ son 15; 17$ será 17.

El lenguaje a usar es Python 3.x.
El estilo, las buenas prácticas, la organización del diseño y la pulcritud del código
no dependen del lenguaje de programación que se use ;)

*¿Qué se evaluará?*
* Tus conocimientos y habilidades de diseño y programación.

*¿Qué debes hacer?*
Diseñar e implementar una solución para representar el back-end de este e-commerce básico.
Junto a este enunciado se proporciona el fichero de tests de la funcionalidad. Para probarlo ejecuta:

```python3 -m unittest tests```

El objetivo es que este test pase. Para ello no puedes modificar el fichero de los tests, usar persistencia (ej.
base de datos, etc.) ni ningún framework (ej. Django, etc.). Aparte de estas restricciones, el diseño y la implementación
del código es totalmente libre.

Hazlo lo mejor que sepas y ¡lúcete!






