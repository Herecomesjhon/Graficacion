#!/usr/bin/env python3
"""Genera las dos investigaciones en Word."""

from doc_tools import (
    FIG,
    H,
    MUTED,
    P,
    Paper,
    bullet,
    contenido,
    cover,
    new_document,
    open_body,
)
import figuras

OUT = FIG.parent


def doc_empresas():
    doc = new_document(
        "Empresas e instituciones que utilizan sistemas operativos libres",
        "Investigación 1. Taller de sistemas operativos.",
    )
    cover(
        doc,
        "INVESTIGACIÓN 1",
        "Empresas e instituciones que utilizan sistemas operativos libres",
        "Dónde los usan, con qué sistema y qué resultado quedó escrito",
    )
    open_body(
        doc,
        "Muñoz Hinojosa, C.  ·  Investigación 1",
        "Taller de sistemas operativos  ·  Investigación 1",
    )
    paper = Paper(doc)
    contenido(
        doc,
        [
            (1, "1. Introducción"),
            (2, "1.1 Pregunta"),
            (2, "1.2 Objetivos"),
            (2, "1.3 Método y alcance"),
            (1, "2. Qué cuenta como sistema operativo libre"),
            (1, "3. La adopción, sector por sector"),
            (1, "4. Empresas"),
            (2, "4.1 Google"),
            (2, "4.2 Amazon"),
            (2, "4.3 Microsoft, el caso mixto"),
            (2, "4.4 IBM y Red Hat"),
            (2, "4.5 Quienes venden el sistema"),
            (2, "4.6 El dispositivo: Valve y Samsung"),
            (1, "5. Casos con nombre y cifra"),
            (2, "5.1 GendBuntu, en la Gendarmería francesa"),
            (2, "5.2 Netflix y FreeBSD"),
            (2, "5.3 La lista TOP500 de noviembre de 2025"),
            (2, "5.4 Schleswig-Holstein"),
            (2, "5.5 Las laptops de la estación espacial"),
            (1, "6. Cuando la migración regresa: Múnich"),
            (1, "7. Motivo y límite"),
            (1, "8. Conclusiones"),
            (1, "Referencias"),
        ],
    )

    H(doc, "1. Introducción")
    P(
        doc,
        "Un sistema operativo libre se puede ejecutar, estudiar, copiar y modificar, y el código fuente es la condición de las dos libertades que lo exigen: estudiarlo y publicar los cambios. Con esa definición, preguntar qué empresas lo utilizan deja de ser una lista de logotipos. La pregunta útil es otra: en qué parte del trabajo diario se apoyan sobre un sistema así, qué familia eligieron y qué resultado quedó documentado con una cifra.",
    )
    P(
        doc,
        "La respuesta tiene tres pisos, y mezclarlos es lo que vuelve confusa la conversación. En las supercomputadoras, en la nube y en una parte grande de los servidores de la web, la familia Linux es la base habitual. En el teléfono, el núcleo Linux llega a la mayoría de las personas dentro de Android, un producto que ya no cumple las cuatro libertades. En el escritorio de oficina, Windows sigue siendo el sistema mayoritario. Las empresas no «se pasaron a Linux». Lo usan en la capa donde les resuelve un problema y lo dejan donde no.",
    )
    P(
        doc,
        "Este trabajo recorre ese mapa con fuentes fechadas. Primero fija qué cuenta como sistema operativo libre. Después mide la adopción con porcentajes que no se pueden sumar, porque cada uno tiene su propio universo. Luego entra a Google, Amazon, Microsoft, IBM, Netflix y Valve, y a dos instituciones públicas que sí cambiaron escritorios: la Gendarmería nacional de Francia y el estado alemán de Schleswig-Holstein. Cierra con Múnich, que volvió atrás. Una investigación que solo cuenta éxitos no alcanza para decidir.",
    )

    H(doc, "1.1 Pregunta", 2)
    P(
        doc,
        "¿Qué empresas e instituciones utilizan sistemas operativos libres, en qué capa de su operación, con qué sistema concreto, y qué resultado se puede sostener con una fuente pública?",
    )

    H(doc, "1.2 Objetivos", 2)
    P(doc, "Objetivo general.", bold=True, indent=0, after=4)
    P(
        doc,
        "Describir, con casos documentados, el uso real de sistemas operativos libres en empresas e instituciones, separando el servidor, el teléfono, el escritorio y el cómputo científico.",
        indent=0,
    )
    P(doc, "Objetivos específicos.", bold=True, indent=0, after=4)
    bullet(doc, "Distinguir software libre, código abierto práctico y software gratuito, y ubicar GNU/Linux, BSD y los derivados de uso masivo.")
    bullet(doc, "Leer las cifras de adopción de 2025 y 2026 sin sumar mediciones que no comparten denominador.")
    bullet(doc, "Reconstruir cinco casos con nombre, sistema y cifra: GendBuntu, Netflix, el TOP500, Schleswig-Holstein y la estación espacial.")
    bullet(doc, "Registrar el límite de cada motivo de adopción, incluido el caso en el que la migración de escritorio se deshizo.")

    H(doc, "1.3 Método y alcance", 2)
    P(
        doc,
        "Es una investigación documental. La fecha de corte es el 20 de noviembre de 2026. Las cifras de supercomputadoras salen de la lista TOP500 de noviembre de 2025. Las de escritorio, telefonía y web corresponden a las lecturas de julio y agosto de 2026 que una síntesis técnica dejó asentadas a partir de StatCounter y de W3Techs; se cita esa síntesis porque los tableros vivos cambian de mes a mes y la lectura necesita una fecha. Los casos institucionales salen de comunicados oficiales, de la ficha pública de Netflix Open Connect y de la cronología reunida del proyecto GendBuntu.",
    )
    P(
        doc,
        "No se auditó el centro de datos de ninguna empresa. Cuando una compañía dice que «usa Linux» y no publica en qué capa, el trabajo lo trata como un indicio, no como un caso. Tampoco se iguala «usar un programa libre» con «correr un sistema operativo libre»: casi todo el mundo usa OpenSSH y eso no convierte a su sistema en OpenBSD.",
    )

    H(doc, "2. Qué cuenta como sistema operativo libre")
    P(
        doc,
        "La Free Software Foundation define el software libre por cuatro libertades. La libertad 0 permite ejecutar el programa para cualquier propósito. La libertad 1 permite estudiar cómo funciona y cambiarlo. La libertad 2 permite redistribuir copias. La libertad 3 permite publicar las versiones modificadas. La 1 y la 3 exigen el código fuente. Sin código, las otras dos pueden existir en un programa cerrado que simplemente no cobra.",
    )
    P(
        doc,
        "De ahí salen tres palabras que en la publicidad se usan como si fueran la misma. Libre describe esas cuatro libertades. Abierto, en el uso de la industria, suele describir un código que se puede leer y un desarrollo público, aunque el producto completo arrastre piezas que no se pueden modificar. Gratuito describe un precio de cero. Un sistema puede ser gratuito y prohibir la copia. Un sistema libre puede cobrarse: se paga el disco, el soporte o el trabajo de instalarlo, y las libertades siguen intactas.",
    )
    P(
        doc,
        "En la práctica hay tres familias. GNU/Linux junta el núcleo Linux, publicado bajo la licencia GPL-2.0, con las herramientas GNU y el resto del espacio de usuario. BSD —FreeBSD, OpenBSD y NetBSD— distribuye núcleo y utilidades juntos, con una licencia permisiva que no obliga a publicar los cambios. Los derivados de uso masivo, como Android, ChromeOS, Tizen o SteamOS, parten de un núcleo libre y le suman capas que ya no lo son. Llevan Linux por dentro y, como producto que la persona recibe, no son un sistema operativo libre completo.",
    )
    paper.figure(
        "02-familias.png",
        "Familias que conviene separar antes de decir que una empresa «usa Linux».",
    )
    P(
        doc,
        "Una distribución tampoco tiene una sola licencia. Debian, Ubuntu, Fedora o Alpine reúnen miles de programas. El núcleo puede ir bajo GPL-2.0, la biblioteca C bajo LGPL y un servidor web bajo BSD. El requisito, para poder repartir el conjunto, es que esas licencias no se contradigan. Por eso una empresa puede usar el sistema, pagar una suscripción de soporte y seguir cumpliendo las libertades del código: la suscripción cobra el servicio, no el permiso de ejecutar.",
    )
    paper.callout(
        "Cómo leer la palabra Linux en un comunicado",
        "Puede nombrar el núcleo, una distribución completa, un contenedor, el teléfono Android o solo la parte del servidor. En este trabajo, cada caso dice cuál de esos cinco significados es el que la fuente sostiene.",
    )

    H(doc, "3. La adopción, sector por sector")
    P(
        doc,
        "La figura 2 junta seis porcentajes que se citan juntos y no miden lo mismo. El 100 % del TOP500 es la familia Linux sobre las 500 supercomputadoras de la lista. El 96 % es la porción de clústeres Kubernetes de producción, en la encuesta de la Cloud Native Computing Foundation de 2025, cuyo nodo corre Linux. El 68 % es la porción de sesiones móviles que StatCounter atribuye a Android en julio de 2026. El 62 % es la porción de sitios web con sistema identificado que W3Techs atribuye a Linux el 17 de agosto de 2026. El 7,5 % y el 4,0 % son, en ese mismo julio, el escritorio medido por StatCounter y los equipos de Steam. Sumarlos produciría un número sin sentido.",
    )
    paper.figure(
        "01-adopcion-por-sector.png",
        "Adopción de la familia Linux según el universo que mide cada fuente. Las barras no se suman. Fuentes: TOP500 (noviembre de 2025), encuesta CNCF 2025, StatCounter (julio de 2026) y W3Techs (17 de agosto de 2026).",
    )
    P(
        doc,
        "El piso alto está en el cómputo científico. Desde la lista de noviembre de 2017, el TOP500 registra familia Linux en los 500 sistemas. La edición de noviembre de 2025 mantiene ese resultado e incluye cuatro máquinas en la frontera del exaflop o por encima: El Capitan, Frontier, Aurora y JUPITER Booster (TOP500, 2025). Ahí el sistema libre no es una alternativa. Es el supuesto sobre el que se diseña el equipo.",
    )
    P(
        doc,
        "En la web, W3Techs medía Linux en el 62,1 % de los sitios cuyo sistema operativo se pudo identificar, y a la familia Unix —Linux más variantes BSD y otros Unix— en el 92 %. Windows Server quedaba en el 8,2 % de ese mismo corte (lectura del 17 de agosto de 2026, recogida en Ramírez, 2026). En los clústeres de producción de la encuesta CNCF 2025, el 96 % de los nodos corre Linux. La nube pública se apoya en esa misma base: Amazon Web Services, Google Cloud y Microsoft Azure ofrecen, como imágenes normales de trabajo, distribuciones Linux.",
    )
    P(
        doc,
        "El piso bajo está en el escritorio personal y en el juego de PC. Un 7,53 % de sesiones de escritorio y un 4,01 % de equipos en Steam, ambos en julio de 2026, son cuotas reales y minoritarias (Ramírez, 2026, a partir de StatCounter y de la encuesta de Steam). Android cambia el relato del teléfono y no cambia la definición: el núcleo es Linux, y el producto que se compra en la tienda de aplicaciones no es un sistema libre. La conclusión de la figura es esa distancia. Las empresas viven en ella. Eligen la capa.",
    )

    H(doc, "4. Empresas")
    P(
        doc,
        "La tabla 1 condensa el mapa. Las secciones que siguen desarrollan los casos en los que la fuente permite decir algo más que el nombre. El orden no es un ranking de pureza. Es el orden en el que el caso enseña una distinción distinta.",
    )
    paper.table(
        ["Organización", "Dónde", "Qué sistema", "Límite del caso"],
        [
            [
                "Google",
                "Servidores, nube, teléfonos y Chromebooks",
                "Linux en la infraestructura. Android y ChromeOS en el dispositivo",
                "Android no es un sistema libre completo",
            ],
            [
                "Amazon",
                "AWS y los aparatos Fire",
                "Amazon Linux 2023 y otras imágenes Linux. Fire OS, derivado de Android",
                "El dato público es la oferta de la nube, no el escritorio interno",
            ],
            [
                "Microsoft",
                "Azure, el subsistema Linux de Windows y el núcleo al que contribuye",
                "Linux en la nube. Windows en el escritorio que vende",
                "Usar Linux en Azure no convierte a Windows en libre",
            ],
            [
                "IBM y Red Hat",
                "Empresas, mainframes y supercomputadoras",
                "Red Hat Enterprise Linux y derivados como Rocky o TOSS",
                "El código es libre y la suscripción de soporte se paga",
            ],
            [
                "Netflix",
                "Aparatos Open Connect, dentro de la red del proveedor",
                "FreeBSD-CURRENT, NGINX y BIRD",
                "La aplicación del teléfono y el catálogo no son el sistema",
            ],
            [
                "Valve",
                "Steam Deck y la parte Linux de Steam",
                "SteamOS, basado en Arch Linux",
                "La tienda vende juegos cerrados. La libertad 0 lo permite",
            ],
            [
                "Gendarmería francesa",
                "Escritorios del cuerpo",
                "GendBuntu, Ubuntu adaptado",
                "Quedan puestos con programas de trabajo especializados",
            ],
            [
                "Schleswig-Holstein",
                "Oficina, correo y, desde 2026, la cancillería",
                "LibreOffice, Open-Xchange y Linux",
                "El resto de ministerios va después de la cancillería",
            ],
        ],
        [1.35, 1.7, 1.85, 1.6],
        "Mapa de los casos de esta investigación. Cada fila nombra la capa, el sistema y el límite.",
    )

    H(doc, "4.1 Google", 2)
    P(
        doc,
        "Google opera su infraestructura de producción sobre Linux y ofrece Google Cloud con imágenes Linux como camino normal de trabajo. En el dispositivo tiene dos sistemas propios de uso masivo. ChromeOS, el sistema de los Chromebooks, está construido sobre Linux. Android también: la documentación de arquitectura del proyecto publica el núcleo Linux como la base del sistema (Android Open Source Project, s. f.).",
    )
    P(
        doc,
        "Android es el caso que más se presta a una frase falsa. Decir que «el teléfono del mundo corre un sistema operativo libre» usa el núcleo y esconde el producto. Los fabricantes publican el código del núcleo porque la GPL-2.0 los obliga cuando distribuyen un núcleo modificado. No están obligados a publicar las aplicaciones, la tienda ni los controladores que viven fuera de ese límite. El resultado es un teléfono con un corazón libre y un producto que la persona no puede reconstruir pieza por pieza. Google, además, escribe núcleo: en los ciclos recientes aparece entre los contribuidores corporativos, junto con Intel, AMD y Red Hat (Ramírez, 2026, a partir de los análisis de LWN del ciclo 6.15).",
    )

    H(doc, "4.2 Amazon", 2)
    P(
        doc,
        "Amazon Web Services es, por volumen, una de las mayores operaciones de Linux del mundo, aunque la empresa no publique un censo de sus propios escritorios. Lo que sí publica es la oferta. Amazon Linux 2023 es la distribución que Amazon mantiene para sus clientes de AWS, con un calendario propio de versiones. Junto a ella, el catálogo de imágenes incluye Ubuntu, Red Hat Enterprise Linux, SUSE y otras. El cliente que «sube un servidor a la nube» aterriza, en el caso habitual, sobre un sistema de la familia Linux.",
    )
    P(
        doc,
        "En el otro extremo del catálogo, los aparatos Fire usan Fire OS, derivado de Android, y por tanto repiten el mismo límite del apartado anterior: núcleo Linux, producto que no es libre completo. Conviene no fundir las dos capas. La nube de Amazon es un caso de sistema operativo de servidor. El control remoto Fire es un caso de derivado.",
    )

    H(doc, "4.3 Microsoft, el caso mixto", 2)
    P(
        doc,
        "Microsoft es el caso que desordena el relato de «empresas de un bando y empresas del otro». Su producto de escritorio sigue siendo Windows. Al mismo tiempo, Azure ofrece Linux como sistema de primera clase, la empresa envía cambios al núcleo Linux y Windows incluye un subsistema para correr un espacio de usuario Linux. Desde finales de la década de 2010, Microsoft dijo en público que cerca de la mitad, y después más de la mitad, de las máquinas virtuales de Azure ejecutaban Linux. No hace falta una cifra nueva de 2026 para sostener el argumento: el escritorio que la empresa vende y la nube que la empresa opera ya no son el mismo sistema.",
    )
    P(
        doc,
        "La lista TOP500 de noviembre de 2025 le pone un nombre a esa nube. Eagle, un clúster alojado en Microsoft Azure, ocupa el puesto 5, con un Rmax de 561,20 PFlop/s (TOP500, 2025). Una supercomputadora de la lista corre, por la regla de esa lista, un sistema de la familia Linux, y corre dentro de la nube de la empresa que vende Windows. El caso sirve para leer cualquier comunicado futuro: hay que preguntar la capa.",
    )

    H(doc, "4.4 IBM y Red Hat", 2)
    P(
        doc,
        "IBM cerró la compra de Red Hat en 2019. Red Hat Enterprise Linux es, desde mucho antes, el sistema con el que una parte grande de la industria contrata soporte, certificaciones y un ciclo de parches con responsable. El código de RHEL está publicado bajo licencias libres. Lo que se paga es la suscripción: el derecho a los binarios certificados, a las actualizaciones por un canal empresarial y a que alguien conteste cuando el sistema se detiene un viernes.",
    )
    P(
        doc,
        "Esa distinción produjo sistemas derivados. Rocky Linux y AlmaLinux reconstruyen un sistema compatible a partir de las fuentes, para quien necesita el comportamiento de RHEL y organiza el soporte de otra manera. En cómputo científico la misma familia aparece con nombre propio. En la lista de noviembre de 2025, JUPITER Booster publica Red Hat Enterprise Linux, HPC6 publica RHEL 8.9 y El Capitan publica TOSS, el sistema de los laboratorios del Departamento de Energía de Estados Unidos, derivado de esa familia (TOP500, 2025). IBM, además, mantiene Linux en sus mainframes de la línea LinuxONE. El patrón es estable: el código sigue libre y la operación seria se contrata.",
    )

    H(doc, "4.5 Quienes venden el sistema", 2)
    P(
        doc,
        "Canonical, SUSE y Oracle forman otro grupo. Su negocio es el propio sistema. Canonical publica Ubuntu y ofrece Ubuntu Pro como suscripción de mantenimiento. SUSE publica SUSE Linux Enterprise, muy presente donde el sistema tiene que convivir con aplicaciones empresariales de ciclo largo. Oracle publica Oracle Linux, reconstruido sobre la línea de fuentes de RHEL, y lo usa en su nube. Aquí la empresa no es solo usuaria. Es la que convierte un proyecto libre en un producto con teléfono de soporte. Para el cliente, el requisito deja de ser «conseguir el ISO» y pasa a ser «decidir si el soporte lo da la propia plantilla o un contrato».",
    )

    H(doc, "4.6 El dispositivo: Valve y Samsung", 2)
    P(
        doc,
        "Valve hizo el intento más visible de los últimos años en el escritorio de entretenimiento. SteamOS, el sistema del Steam Deck, está basado en Arch Linux. Proton permite correr en ese sistema una parte de los juegos publicados para Windows. En la encuesta de Steam de julio de 2026, Linux llegó al 4,01 % de los equipos, y dentro de ese grupo SteamOS Holo era el 22,24 %. CachyOS, la distribución basada en Arch que este taller usó en la práctica 4 para armar una VPN con WireGuard, aparecía en segundo lugar entre los usuarios Linux de esa encuesta, con 14,31 % (Ramírez, 2026). El dato local y el dato global se tocan: el escritorio Linux de 2026 ya no es una sola distribución.",
    )
    P(
        doc,
        "La tienda de Steam vende, en su mayoría, juegos cerrados. Eso no rompe la definición del sistema. La libertad 0 permite ejecutar el sistema para cualquier propósito, incluido vender un programa que no es libre encima de él. Confundir las dos capas —el sistema y el catálogo— es el mismo error que confundir Android con el núcleo.",
    )
    P(
        doc,
        "Samsung reparte el mismo doble uso en productos distintos. Sus teléfonos usan Android. Sus televisores y varios relojes usan Tizen, un sistema basado en Linux alojado como proyecto de la Linux Foundation. Otra vez: el núcleo compartido no vuelve equivalentes a los productos.",
    )

    H(doc, "5. Casos con nombre y cifra")
    P(
        doc,
        "Los apartados anteriores dicen quién usa qué. Estos cinco dicen cómo se ve cuando hay una cifra, una fecha y una decisión que se puede contar. Tres son de escritorio o de aparato dedicado. Uno es de cómputo científico. Uno es histórico y sirve por la razón, no por el volumen.",
    )

    H(doc, "5.1 GendBuntu, en la Gendarmería francesa", 2)
    P(
        doc,
        "La Gendarmería nacional de Francia es el caso grande de escritorio que sí se sostuvo. No empezó por el sistema operativo. En 2004 sustituyó Microsoft Office por OpenOffice.org. En 2006 movió el navegador a Firefox y el correo a Thunderbird. En 2008 decidió GendBuntu, una adaptación de Ubuntu, y la instaló primero en unos 5 000 equipos de prueba. La migración grande cerró en 2014, con 65 000 computadoras en GendBuntu 12.04, sobre un parque de unas 77 000. En 2019 rondaba el 90 %. En junio de 2024, la cronología pública del proyecto cuenta 103 164 estaciones, el 97 % del parque, y en diciembre de 2024 el sistema pasó a la base 24.04 (cronología reunida en GendBuntu, 2024).",
    )
    paper.figure(
        "03-gendbuntu.png",
        "Orden real de la migración francesa: primero la oficina y el navegador, años después el sistema operativo.",
    )
    P(
        doc,
        "El orden es la enseñanza. Cambiar el sistema al final, cuando la suite, el navegador y el correo ya eran otros, evitó pedirle a la plantilla un salto único. En 2013, con el parque a medio migrar, el Open Source Observatory recogió una baja de alrededor del 40 % en el costo total de propiedad. La prensa que ha vuelto sobre el caso en 2026 habla de un ahorro de licencias del orden de dos millones de euros al año. Esa segunda cifra circula en notas secundarias y no está en el reporte de 2013: aquí se registra como estimación difundida, no como una auditoría leída de primera mano.",
    )
    P(
        doc,
        "Tampoco es un parque puro. La propia cronología deja una fracción de puestos fuera, atados a programas de trabajo que no se pudieron mover. GendBuntu es Ubuntu adaptado, con las piezas no libres que Ubuntu admite cuando el hardware las pide. Cumple como caso de adopción institucional. No cumple como ejemplo de distribución estrictamente libre en el sentido de la Free Software Foundation. Las dos frases pueden ser verdaderas a la vez.",
    )

    H(doc, "5.2 Netflix y FreeBSD", 2)
    P(
        doc,
        "Netflix reparte el video de su catálogo con Open Connect, una red de aparatos colocados dentro de la red del proveedor de internet o junto a un punto de intercambio. El aparato no transcodifica. Sirve archivos que ya vienen codificados para cada calidad, por HTTP, lo más cerca posible de quien está mirando. El sistema operativo de ese aparato es FreeBSD-CURRENT. El servidor web es NGINX. El demonio de rutas es BIRD. Netflix lo escribe en su propia ficha técnica y explica por qué eligió FreeBSD: equilibrio entre estabilidad y funciones, comunidad de desarrollo y gente del equipo que ya sabía trabajar ahí. Las mejoras vuelven al proyecto por medio de los committers de FreeBSD que forman parte del equipo (Netflix, s. f.).",
    )
    paper.figure(
        "04-netflix.png",
        "Recorrido de una película hasta el aparato Open Connect, y las cuatro piezas libres que hay dentro.",
    )
    P(
        doc,
        "En una charla de 2023, Drew Gallatin resumió la decisión en una frase que conviene citar porque separa la licencia del rendimiento: llegaron por la licencia y se quedaron por la eficiencia. La licencia BSD permite incorporar cambios en un producto sin la obligación de publicarlos. Netflix, pudiendo no hacerlo, devuelve trabajo del núcleo. Las diapositivas del mismo equipo marcan hitos de caudal del aparato: 100 Gb/s en 2017, 200 Gb/s en 2020 y 400 Gb/s en 2021, con TLS hecho en el núcleo para no sacar los datos del camino rápido de sendfile (Gallatin, 2023).",
    )
    P(
        doc,
        "El caso corrige dos atajos. El primero: no todo sistema libre de una empresa grande es Linux. FreeBSD es libre, es otro núcleo y otra licencia, y hay una razón de negocio para preferirla. El segundo: la aplicación con la que una persona abre Netflix en el teléfono no es este sistema. El sistema libre está en el aparato de la red, no en el ícono.",
    )

    H(doc, "5.3 La lista TOP500 de noviembre de 2025", 2)
    P(
        doc,
        "La lista de noviembre de 2025 permite bajar del «100 % Linux» a nombres de máquinas y de sistemas. El Capitan, en Lawrence Livermore, encabeza la lista con un Rmax de 1 809 PFlop/s y el sistema TOSS. Frontier, en Oak Ridge, marca 1 353 PFlop/s con HPE Cray OS y fue la primera máquina exaescala en operar en esta lista. Aurora, en Argonne, marca 1 012 PFlop/s; su ficha pública no fija una sola distribución comercial, y entra en el resultado de familia. JUPITER Booster, en el centro de Jülich, marca 1 000 PFlop/s con Red Hat Enterprise Linux y es, en esa edición, la primera máquina europea de la lista en llegar a esa cota (TOP500, 2025).",
    )
    paper.figure(
        "05-top500.png",
        "Los cuatro primeros sistemas de la lista TOP500 de noviembre de 2025 y el sistema operativo que cada ficha publica.",
    )
    P(
        doc,
        "Más abajo de los cuatro primeros, la lista deja de hablar de «Linux» a secas y empieza a nombrar distribuciones. HPC6, de la energética Eni, publica RHEL 8.9. ABCI 3.0, en Japón, publica Rocky Linux 9. ISEG2 publica Ubuntu 22.04. CHIE-4 publica Ubuntu 24.04.2 LTS (TOP500, 2025). El 100 % de la familia es compatible con una diversidad real de distribuciones. Quien elige un sistema para un clúster no elige «Linux»: elige un ciclo de parches, un proveedor y un conjunto de controladores.",
    )

    H(doc, "5.4 Schleswig-Holstein", 2)
    P(
        doc,
        "El estado alemán de Schleswig-Holstein es el caso público más reciente con comunicados propios, y conviene contarlo en el orden en que ocurrió, no en el orden de un titular. El 2 de octubre de 2025 terminó el cambio del correo: más de 40 000 buzones salieron de Exchange y Outlook hacia Open-Xchange y Thunderbird. El 4 de diciembre de 2025 el gobierno declaró LibreOffice como estándar de oficina, con cerca del 80 % de los puestos —fuera de la administración fiscal— ya migrados, y estimó un ahorro de licencias de más de 15 millones de euros, frente a 9 millones de inversión prevista para 2026 en la migración y en el desarrollo de las herramientas libres (Schleswig-Holstein, 2025a, 2025b).",
    )
    P(
        doc,
        "El sistema operativo llegó después, y todavía no llega a todo el estado. El 19 de septiembre de 2026, en las jornadas de código abierto de Kiel, el ministerio de digitalización anunció que la cancillería del estado ya trabaja sobre Linux: más de 200 personas, con alrededor de 20 puestos todavía en Windows por dependencias de programas especializados. El mismo comunicado dice que los demás ministerios y organismos siguen en la planeación del despliegue (Schleswig-Holstein, 2026). Es un caso en marcha, no una foto final. Se parece a la Gendarmería en el método —primero las aplicaciones, después el sistema— y se diferencia en la escala: aquí el escritorio Linux, a la fecha de corte de este trabajo, está en la cancillería y no en los 40 000 puestos del correo.",
    )

    H(doc, "5.5 Las laptops de la estación espacial", 2)
    P(
        doc,
        "Hacia 2013, Keith Chuvala, del contratista United Space Alliance, contó a la Linux Foundation por qué las laptops de operación de la Estación Espacial Internacional estaban dejando Windows. El equipo necesitaba un sistema estable y, sobre todo, un sistema que pudieran parchar ellos mismos: el soporte técnico queda a 400 kilómetros. Habían usado Scientific Linux y se apoyaban en Debian. El mismo relato incluye a Robonaut, el robot humanoide de la estación, también sobre Linux (Linux Foundation, 2013). El caso es pequeño en número de usuarios —la tripulación cabe en una sola mesa— y grande en la razón. Cuando el fabricante no puede llegar, el control del sistema deja de ser una preferencia y se vuelve el requisito.",
    )
    P(
        doc,
        "No se afirma aquí que en 2026 esas laptops sigan en la misma versión. La fuente es de 2013 y este trabajo no la actualiza con un inventario nuevo de la NASA. Se usa por la decisión y por el criterio, que siguen siendo legibles.",
    )

    H(doc, "6. Cuando la migración regresa: Múnich")
    P(
        doc,
        "Múnich sirve porque la migración se deshizo. El proyecto LiMux llevó durante años una distribución propia, de familia Debian, a la administración de la ciudad. En 2017 el ayuntamiento decidió volver a un entorno Windows, y el regreso se ejecutó en los años siguientes. Las razones que se discutieron en público fueron las de siempre en un escritorio de oficina: programas de trabajo que no tenían equivalente, quejas de uso y un costo de ida y vuelta que cada parte contaba de una forma distinta (LiMux, s. f.).",
    )
    P(
        doc,
        "Leído junto a la Gendarmería, el caso no dice «Linux no sirve en el escritorio». Dice que el escritorio se cae cuando las aplicaciones de línea y las personas no viajan con el sistema. La Gendarmería pasó una década cambiando la suite, el navegador y el correo antes de dar por cerrada la migración del sistema. Múnich cargó el peso en la distribución propia y, al final, deshizo el camino. Schleswig-Holstein, en 2025 y 2026, está copiando el primer método, no el segundo: oficina y correo primero, sistema después, y con puestos de excepción reconocidos desde el comunicado.",
    )

    H(doc, "7. Motivo y límite")
    P(
        doc,
        "Los casos ya contados caben en cinco motivos. Cada motivo tiene un límite que aparece en el mismo expediente. El costo de licencia baja cuando el sistema es Debian, Ubuntu de comunidad o FreeBSD, y reaparece como suscripción en cuanto se quiere un RHEL, un SUSE o un Ubuntu Pro con responsable. El control existe si hay quien parchee: la estación espacial lo necesitaba y por eso migró; sin esa gente, el control es una frase. La seguridad mejora cuando el código se puede auditar, y auditarlo es trabajo, no una propiedad mágica del archivo. La escala está ganada en servidores y supercomputadoras, y sigue siendo el punto débil del escritorio, que es donde Múnich volvió atrás. La soberanía —la razón que Schleswig-Holstein escribe en sus comunicados— reduce la dependencia de un fabricante, hasta que un programa especializado no tiene con qué sustituirse. Esos cerca de 20 puestos que la cancillería dejó fuera son el límite, dicho con un número chico y honesto.",
    )
    paper.figure(
        "06-motivo-limite.png",
        "Cinco motivos de adopción y el límite que los casos de este trabajo ya mostraron.",
    )

    H(doc, "8. Conclusiones")
    P(
        doc,
        "Las empresas y las instituciones sí utilizan sistemas operativos libres, y lo hacen sobre todo donde el sistema se administra en serie: servidores, nube, aparatos de red y cómputo científico. En noviembre de 2025 esa preferencia es total en el TOP500. En agosto de 2026 es mayoritaria en los sitios web cuyo sistema se pudo identificar. En los clústeres de producción medidos por la CNCF en 2025, el nodo Linux es la norma.",
    )
    P(
        doc,
        "El teléfono no debe contarse en esa misma frase. Android lleva núcleo Linux y no es un sistema operativo libre completo. SteamOS y Tizen acercan la familia al dispositivo, y el catálogo que venden encima puede ser cerrado sin que el sistema deje de ser libre. La libertad 0 cubre ese uso.",
    )
    P(
        doc,
        "Microsoft es el recordatorio de método. Vende Windows y opera Linux en Azure, al punto de aparecer con el clúster Eagle dentro del TOP500. Cualquier lista de «empresas que usan Linux» que no diga la capa está mal hecha.",
    )
    P(
        doc,
        "Donde el escritorio sí cambió, el orden fue de aplicaciones hacia el sistema, con años de por medio y con una plantilla propia. Así avanzó la Gendarmería desde 2004 y así está avanzando Schleswig-Holstein entre 2025 y 2026. Donde ese acompañamiento faltó, como en Múnich, la migración se pudo deshacer. El código libre no sustituye esa parte.",
    )
    P(
        doc,
        "Queda, para el taller, una lectura concreta. En la práctica 4 el sistema del equipo fue CachyOS, de familia Arch, y alcanzó para terminar una VPN con WireGuard. En la práctica 6 el sistema pedido fue Ubuntu, porque la nube privada de la guía está armada para esa distribución. Las dos elecciones caben en este mapa: una distribución libre de uso general en el escritorio personal, y una distribución con un canal de paquetes concreto cuando la carga de trabajo —aquí, OpenStack— lo exige. Ninguna de las dos es, por sí sola, el 100 % del TOP500 ni el 7 % del escritorio mundial. Son la capa que tocaba usar.",
    )

    H(doc, "Referencias")
    P(
        doc,
        "Las referencias siguen el orden de APA. Cuando un porcentaje de cuota depende de un tablero que cambia cada mes, se cita la síntesis que dejó la lectura fechada y, en el texto, el instrumento original.",
        size=11, italic=True, indent=0, color=MUTED,
    )
    refs = [
        "Android Open Source Project. (s. f.). Kernel. https://source.android.com/docs/core/architecture/kernel",
        "Gallatin, D. (2023). The magical mystery merge: Why we run FreeBSD-current at Netflix [presentación]. OpenFest. https://people.freebsd.org/~gallatin/talks/OpenFest2023.pdf",
        "GendBuntu. (2024). En Wikipedia. https://en.wikipedia.org/wiki/GendBuntu",
        "LiMux. (s. f.). En Wikipedia. https://en.wikipedia.org/wiki/LiMux",
        "Linux Foundation. (2013). Linux Foundation training prepares the International Space Station for Linux migration. https://www.linuxfoundation.org/blog/blog/linux-foundation-training-prepares-the-international-space-station-for-linux-migration",
        "Muñoz Hinojosa, C. (2026). Práctica 4. Creación de una red privada virtual con WireGuard en CachyOS. Taller de sistemas operativos, Instituto Tecnológico de Morelia.",
        "Muñoz Hinojosa, C. (2026). Práctica 6. Implementación de nubes privadas con MicroStack en Ubuntu. Taller de sistemas operativos, Instituto Tecnológico de Morelia.",
        "Netflix. (s. f.). Open Connect appliances. https://openconnect.netflix.com/en/appliances/",
        "Ramírez, S. (2026, 20 de agosto). Linux statistics 2026: Desktop, server, cloud trends. SQ Magazine. https://sqmagazine.co.uk/linux-statistics/",
        "Schleswig-Holstein. (2025a, 6 de octubre). Mailsystem der Landesverwaltung komplett auf Open Source umgestellt. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2025/cds/251006_cds_ox",
        "Schleswig-Holstein. (2025b, 4 de diciembre). LibreOffice ersetzt Microsoft. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2025/cds/251204_cds_open-source",
        "Schleswig-Holstein. (2026, 19 de septiembre). Staatskanzlei nutzt Linux. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2026/cds/260919_cds_linux_stk",
        "TOP500. (2025). TOP500 list — November 2025. https://top500.org/lists/top500/list/2025/11/",
    ]
    for ref in refs:
        paper.reference(ref)
    path = OUT / "Investigacion-1-Empresas-SO-libres-CristianMunoz-23121073.docx"
    doc.save(path)
    print(path)
    return path


def doc_requisitos():
    doc = new_document(
        "Requisitos de los sistemas operativos libres",
        "Investigación 2. Taller de sistemas operativos.",
    )
    cover(
        doc,
        "INVESTIGACIÓN 2",
        "Requisitos de los sistemas operativos libres",
        "Libertades, licencias, arquitectura y hardware, con ejemplos",
    )
    open_body(
        doc,
        "Muñoz Hinojosa, C.  ·  Investigación 2",
        "Taller de sistemas operativos  ·  Investigación 2",
    )
    paper = Paper(doc)
    contenido(
        doc,
        [
            (1, "1. Introducción"),
            (2, "1.1 Pregunta"),
            (2, "1.2 Objetivos"),
            (2, "1.3 Método"),
            (1, "2. El requisito de definición: las cuatro libertades"),
            (1, "3. El requisito jurídico: las licencias"),
            (1, "4. El requisito de una distribución libre"),
            (1, "5. El requisito de arquitectura"),
            (1, "6. El requisito de hardware"),
            (1, "7. El requisito de una organización"),
            (1, "8. Ejemplos resueltos"),
            (2, "8.1 Tres equipos"),
            (2, "8.2 Comprobar el sistema en la terminal"),
            (2, "8.3 La práctica 4 y la práctica 6"),
            (2, "8.4 Lista de comprobación antes de instalar"),
            (1, "9. Conclusiones"),
            (1, "Referencias"),
        ],
    )

    H(doc, "1. Introducción")
    P(
        doc,
        "«Requisitos de un sistema operativo libre» es una frase que esconde cuatro preguntas distintas. La primera es de definición: qué tiene que cumplir para que la palabra libre sea exacta. La segunda es jurídica: con qué licencia se puede estudiar, copiar y volver a publicar. La tercera es de arquitectura: qué piezas tiene que traer una máquina para que ese sistema arranque y se pueda administrar. La cuarta es de hardware: cuánta memoria, cuánto disco y qué procesador pide cada edición. Una guía de instalación solo contesta la cuarta. Un folleto de la comunidad solo contesta la primera. Este trabajo las separa y las vuelve a juntar en ejemplos.",
    )
    P(
        doc,
        "Hay una quinta pregunta, y es la que decide en una escuela o en una empresa: qué tiene que existir alrededor del sistema para que alguien lo use el lunes. Personas que lo administren, un canal de actualizaciones, y programas de trabajo que existan para ese sistema. Sin esa quinta, las otras cuatro producen un ISO correcto y una migración fracasada.",
    )

    H(doc, "1.1 Pregunta", 2)
    P(
        doc,
        "¿Qué requisitos —de definición, de licencia, de arquitectura, de hardware y de organización— tiene que cumplir un sistema operativo libre para serlo y para poder instalarse y operarse en un caso real?",
    )

    H(doc, "1.2 Objetivos", 2)
    P(doc, "Objetivo general.", bold=True, indent=0, after=4)
    P(
        doc,
        "Distinguir y documentar los requisitos de los sistemas operativos libres, desde la definición de la Free Software Foundation hasta la memoria que pide una carga de trabajo concreta.",
        indent=0,
    )
    P(doc, "Objetivos específicos.", bold=True, indent=0, after=4)
    bullet(doc, "Enunciar las cuatro libertades y mostrarlas sobre un programa real, NGINX, con licencia BSD.")
    bullet(doc, "Clasificar las licencias libres que de verdad aparecen en un sistema: copyleft fuerte, copyleft débil y permisivas.")
    bullet(doc, "Explicar la lista de la FSF para distribuciones y el caso de Ubuntu frente a Trisquel.")
    bullet(doc, "Comparar los requisitos de hardware publicados de Debian 12, Ubuntu 24.04, FreeBSD y Alpine, y contrastarlos con la práctica 6 del taller.")

    H(doc, "1.3 Método", 2)
    P(
        doc,
        "Investigación documental, con fecha de corte del 20 de noviembre de 2026. Las libertades y la lista de distribuciones se toman de los textos de la Free Software Foundation. Las cifras de memoria y disco se toman de la guía de instalación de Debian 12, de la documentación de Ubuntu Server 24.04, de la guía comunitaria de Ubuntu Desktop y del manual de FreeBSD en la serie 12, que es donde el mínimo de hardware quedó escrito con números. Los ejemplos del taller salen de las prácticas 4 y 6 de esta asignatura. No se inventan precios de licencias ni se presenta como medición propia un requisito que la guía marca como punto ideal.",
    )

    H(doc, "2. El requisito de definición: las cuatro libertades")
    P(
        doc,
        "La Free Software Foundation numera las libertades desde cero. La libertad 0 es ejecutar el programa para cualquier propósito, sin pedir permiso y sin que la licencia separe un uso comercial de un uso escolar. La libertad 1 es estudiar el programa y modificarlo para que haga lo que se necesita. La libertad 2 es redistribuir copias. La libertad 3 es distribuir la versión modificada. La definición lo dice con claridad: el acceso al código fuente es la condición previa de la libertad 1 y de la libertad 3 (Free Software Foundation, s. f.-a).",
    )
    paper.figure(
        "07-libertades.png",
        "Las cuatro libertades. La numeración empieza en cero porque ejecutar el programa es la base de las otras tres.",
    )
    P(
        doc,
        "Conviene enunciarlas con verbos de taller, no solo con la fórmula. Ejecutar significa instalar el sistema en el laboratorio sin escribirle al autor. Estudiar significa abrir el código del programa que falla, no conformarse con el manual. Redistribuir significa que la escuela puede clonar la misma imagen en veinte máquinas. Publicar mejoras significa que un parche útil puede salir del salón y volver al proyecto, o puede quedarse en una derivación con nombre propio. Las distribuciones existen por la libertad 3.",
    )

    H(doc, "2.1 Ejemplo. NGINX y las cuatro libertades", 2)
    P(
        doc,
        "NGINX es el servidor web de los aparatos con los que Netflix entrega video en su red Open Connect. Su licencia es BSD de dos cláusulas. Aplicada a ese caso, cada libertad se puede señalar con el dedo.",
    )
    bullet(doc, "Libertad 0. Netflix ejecuta NGINX para un fin comercial, servir video a millones de personas, sin una autorización especial del autor.")
    bullet(doc, "Libertad 1. El equipo puede leer el código y combinarlo con FreeBSD, que es el sistema del aparato.")
    bullet(doc, "Libertad 2. El programa viaja dentro del aparato que se instala en la red del proveedor. La licencia pide conservar el aviso de autor, no pide un pago por copia.")
    bullet(doc, "Libertad 3. Pueden modificarlo. La licencia BSD no los obliga a publicar las modificaciones. Aun así, el equipo devuelve al proyecto FreeBSD mejoras del núcleo, como el TLS hecho en el kernel y el sendfile asíncrono (Netflix, s. f.; Gallatin, 2023).")
    P(
        doc,
        "La última viñeta es el punto fino. La libertad permite no publicar. La práctica de esta empresa fue publicar una parte. Si el aparato corriera un núcleo Linux modificado y Netflix lo distribuyera, la GPL-2.0 del núcleo sí exigiría ofrecer el código correspondiente de ese núcleo. Es lo que hacen los fabricantes de teléfonos Android: publican el núcleo y no publican el resto del producto. La libertad se cobra en la obra que se distribuye, no en todo lo que la empresa tenga en sus repositorios privados.",
    )

    H(doc, "3. El requisito jurídico: las licencias")
    P(
        doc,
        "Las cuatro libertades se escriben en una licencia. Sin ese texto, el permiso es una cortesía que el autor puede retirar. En los sistemas que este trabajo estudia aparecen tres familias de licencia. Las tres permiten usar, estudiar, copiar y modificar. Difieren en lo que una persona puede cerrar después.",
    )
    paper.figure(
        "09-licencias.png",
        "Copyleft fuerte, copyleft débil y licencias permisivas, con programas que sí están en un sistema real.",
    )
    P(
        doc,
        "El copyleft fuerte, el de la GPL-2.0 y la GPL-3.0, ata la obra derivada a la misma licencia. El núcleo Linux es GPL-2.0. Las coreutils y Bash son GPL-3.0. Quien distribuye una versión modificada de esos programas distribuye también el código, bajo la misma licencia. El copyleft débil protege la biblioteca o el archivo, y deja que otro programa la use sin volverse libre: glibc es LGPL, systemd es LGPL-2.1 y Firefox usa la MPL-2.0, que aplica el copyleft por archivo. Las licencias permisivas —BSD de dos cláusulas en FreeBSD y en NGINX, MIT en la biblioteca musl, Apache-2.0 en una cantidad grande de software de servidores— permiten meter el código en un producto cerrado. Se conserva el aviso de autor. Apache añade una cláusula de patentes para que quien contribuye no demande después por una patente que el propio código estaba usando.",
    )
    P(
        doc,
        "Un sistema completo es un conjunto de esas licencias, y el conjunto tiene que poder repartirse sin contradicción. Hay un límite que evita un choque famoso: el núcleo Linux, GPL-2.0, y un programa de espacio de usuario con GPL-3.0 no se funden en un solo binario. Se hablan por la interfaz de llamadas al sistema. Por eso una distribución puede traer los dos sin convertir el núcleo en GPL-3.0. El requisito jurídico no es «una licencia para todo el ISO». Es que cada pieza tenga una licencia libre y que la suma se pueda entregar.",
    )
    paper.callout(
        "Libre y de pago caben en la misma frase",
        "Red Hat Enterprise Linux publica el código bajo licencias libres y cobra la suscripción de soporte, los binarios certificados y el canal de parches. La libertad describe el permiso sobre el código. La suscripción describe el servicio. Quien necesita el comportamiento de RHEL y no quiere esa suscripción tiene reconstrucciones como Rocky Linux y AlmaLinux, que existen precisamente porque las fuentes se pueden usar.",
    )

    H(doc, "4. El requisito de una distribución libre")
    P(
        doc,
        "Con las cuatro libertades se puede armar un sistema que, en la instalación de todos los días, ya las rompe. Basta con incluir un controlador cerrado, un firmware que no se puede estudiar o un menú que recomienda instalarlo. La Free Software Foundation publicó por eso unas directrices para distribuciones de sistemas libres. No bastan para un programa suelto. Fijan cuándo el conjunto que se instala merece el adjetivo (Free Software Foundation, s. f.-b).",
    )
    paper.figure(
        "10-fsdg.png",
        "Seis condiciones de las directrices de la FSF para considerar libre una distribución completa.",
    )
    P(
        doc,
        "El código fuente correspondiente tiene que estar al alcance de quien recibe el sistema. La instalación no trae programas privativos ni blobs de firmware. La documentación y los menús no empujan hacia un repositorio cerrado. Los manuales se pueden copiar y modificar. Una marca registrada no puede servir de candado para impedir que alguien publique una versión modificada. El sistema no incluye un candado digital que le quite al usuario las libertades anteriores. Han figurado en la lista de distribuciones que cumplen esas directrices Trisquel, PureOS, Parabola GNU/Linux-libre, GNU Guix System e Hyperbola. La lista cambia y conviene mirarla en la fuente, no memorizarla como un póster.",
    )

    H(doc, "4.1 Ubuntu y Trisquel, el mismo origen", 2)
    P(
        doc,
        "Trisquel se construye sobre una base Ubuntu LTS y le quita lo que esas directrices no aceptan. La comparación sirve porque las dos se pueden describir sin insultar a ninguna. Ubuntu es el sistema que una empresa, una escuela o una laptop nueva pueden instalar el mismo día, con firmware para el Wi-Fi y, si hace falta, el controlador cerrado de NVIDIA. Su componente main es software libre. Los componentes restricted y multiverse no lo son, y la tienda Snap puede distribuir programas cerrados. Trisquel usa linux-libre, el núcleo sin esos blobs, y no deja activo un repositorio privativo. Si la tarjeta de red solo funciona con firmware cerrado, en Trisquel esa red no aparece.",
    )
    paper.figure(
        "11-ubuntu-trisquel.png",
        "Ubuntu y Trisquel comparten origen. Solo una de las dos entra en la lista estricta de la FSF.",
    )
    P(
        doc,
        "Debian ocupa un lugar intermedio que conviene dejar escrito. Su contrato social pone el software libre en el centro. En 2022, el proyecto decidió que el instalador pudiera ofrecer firmware no libre, para que una máquina actual arrancara con red y con video. Por esa razón Debian, como imagen que la mayoría de la gente instala, tampoco está en la lista estricta. La decisión es un requisito chocando con otro: la libertad del firmware contra el requisito físico de que la laptop encienda el Wi-Fi.",
    )
    paper.callout(
        "Ejemplo de escritorio",
        "Una laptop de laboratorio con Wi-Fi Intel o Realtek suele necesitar un archivo de firmware que no tiene fuentes. Ubuntu la deja en línea el mismo día. Trisquel puede dejarla sin red inalámbrica y con red de cable, o sin video acelerado. Las dos respuestas son coherentes con su requisito. La elección depende de qué requisito manda en esa mesa: la definición estricta o la clase del lunes a las 7.",
    )

    H(doc, "5. El requisito de arquitectura")
    P(
        doc,
        "Un núcleo suelto no es un sistema operativo. Hace falta una pila, y cada piso agrega un requisito. Abajo está el hardware. Encima, el firmware, que a menudo es el piso que no es libre. Después el núcleo, Linux o un núcleo BSD, que administra procesos, memoria, archivos, red y controladores. Después las bibliotecas y las utilidades —glibc o musl, coreutils, un shell— sin las cuales el núcleo no tiene con qué hablarle a una persona. Después el sistema de inicio y los servicios: systemd en la mayoría de las distribuciones Linux actuales, OpenRC en Alpine y en algunas otras, el rc propio de BSD. Arriba, las aplicaciones, cada una con su licencia.",
    )
    paper.figure(
        "08-capas.png",
        "Capas que un sistema operativo libre tiene que poder entregar. Se lee de abajo hacia arriba.",
    )
    P(
        doc,
        "El firmware es el requisito que más se discute y el que más se esconde en una laptop nueva. El núcleo puede ser libre y, aun así, la tarjeta de Wi-Fi, la GPU o el controlador de disco pueden negarse a funcionar hasta recibir un blob del fabricante. Ese blob se carga, no se estudia y no se modifica. Una distribución estricta lo deja fuera. Una distribución de uso general lo empaqueta, a veces en un repositorio aparte, y lo instala. Las dos están documentando el mismo hecho del hardware.",
    )
    P(
        doc,
        "El arranque agrega otro requisito de máquina nueva. Muchas laptops solo encienden con UEFI y con el arranque seguro activo. El arranque seguro exige un cargador firmado. Ubuntu y otras distribuciones grandes resuelven el trámite con un cargador inicial firmado, el shim, y la máquina arranca sin tocar la BIOS. Una distribución que rechaza ese camino puede pedir que se desactive el arranque seguro o que la persona inscriba su propia llave. Es un requisito de instalación. No es una de las cuatro libertades, aunque en la mesa de trabajo se sienta igual de bloqueante.",
    )
    P(
        doc,
        "Conviene no convertir en requisito de libertad lo que es una preferencia de administración. Systemd no es una condición para que un sistema sea libre. Devuan existe como una Debian sin systemd. Alpine usa OpenRC y es una base habitual de contenedores. FreeBSD usa su propio sistema de arranque. El requisito de esta capa es otro: que exista un modo de levantar servicios, de crear usuarios, de guardar registros y de instalar actualizaciones de seguridad. Cuál herramienta lo haga es una decisión del proyecto.",
    )
    P(
        doc,
        "También hay un requisito de empaquetado. Un sistema libre de uso real necesita un modo de instalar, actualizar y retirar programas sin copiar carpetas a mano: apt en Debian y Ubuntu, dnf en Fedora y en la familia Red Hat, pacman en Arch y en CachyOS, apk en Alpine, pkg en FreeBSD. El requisito no es el nombre del comando. Es que las actualizaciones de seguridad puedan llegar después del día de la instalación. Un sistema que se instala y no se actualiza deja de cumplir, en la práctica, el cuidado que la libertad 1 haría posible.",
    )

    H(doc, "6. El requisito de hardware")
    P(
        doc,
        "Aquí las cifras importan, y la primera regla es no pedirlas «para Linux». Se piden para una edición, en una versión, con o sin escritorio. Debian 12 lo escribe en su guía de instalación. Sin escritorio, la memoria mínima de referencia es 256 MB y la recomendada 512 MB, con 4 GB de disco. Con escritorio, 1 GB mínimo, 2 GB recomendados y 10 GB de disco. El instalador gráfico, además, pide del orden de 780 MB de memoria y 1 160 MB de disco solo para poder instalar: el instalador puede exigir más que el sistema ya instalado (Debian, s. f.).",
    )
    P(
        doc,
        "Ubuntu separa el escritorio del servidor, y no publica las dos listas con el mismo detalle. El tutorial oficial de Ubuntu Desktop 24.04 pide una máquina con al menos 25 GB de almacenamiento y una memoria USB de 8 GB o más para el instalador. En esa página no fija una cifra de RAM (Canonical, s. f.-a). Para este trabajo se usan 4 GB como referencia práctica de una sesión con el escritorio GNOME y un navegador: no es un mínimo oficial, y por debajo de eso la máquina se queda corta. Ubuntu Server 24.04 sí publica números: mínimo 1,5 GB de RAM para la imagen ISO y 1 GB para imágenes de nube, con 3 GB o más como sugerencia; mínimo 5 GB de disco en la ISO y 25 GB o más como sugerencia. La misma página lista las arquitecturas: amd64, arm64, armhf, ppc64el, riscv64 y s390x (Canonical, s. f.-b). El requisito de arquitectura va antes que el de la memoria: una imagen amd64 no arranca en un procesador ARM.",
    )
    P(
        doc,
        "FreeBSD, en el manual de la serie 12, documenta un mínimo de 96 MB de RAM y 1,5 GB de disco, y advierte que esas cifras solo sirven para un aparato embebido a la medida. Para un escritorio de propósito general el mismo manual propone, como punto de partida, 2 a 4 GB de RAM y al menos 8 GB de disco (FreeBSD, 2021). Alpine se usa mucho donde el sistema debe ser pequeño: la documentación comunitaria habla de un servidor sin interfaz gráfica a partir de unos 128 MB de RAM y cerca de 1 GB de disco. En este trabajo esa cifra se usa como orden de magnitud, no como una promesa de la instalación gráfica.",
    )
    paper.table(
        ["Sistema y edición", "Memoria de referencia", "Disco", "De dónde sale"],
        [
            ["Debian 12, sin escritorio", "256 MB mínimo, 512 MB recomendados", "4 GB", "Guía de instalación de Bookworm"],
            ["Debian 12, con escritorio", "1 GB mínimo, 2 GB recomendados", "10 GB", "La misma guía"],
            ["Instalador gráfico de Debian 12", "Unos 780 MB para poder instalar", "Unos 1,2 GB para instalar", "Sección de memoria del instalador"],
            ["Ubuntu Desktop 24.04", "El tutorial no publica RAM. 4 GB es referencia práctica de este trabajo", "25 GB, y USB de 8 GB", "Tutorial oficial de instalación"],
            ["Ubuntu Server 24.04", "1,5 GB mínimo en ISO; 3 GB sugeridos", "5 GB mínimo; 25 GB sugeridos", "Documentación de Canonical"],
            ["FreeBSD, escritorio", "2 a 4 GB como punto de partida", "8 GB o más", "Manual de la serie 12"],
            ["FreeBSD, embebido", "96 MB en ese manual", "1,5 GB", "El mismo manual, para un aparato a la medida"],
            ["Alpine, servidor sin interfaz", "Del orden de 128 MB", "Del orden de 1 GB", "Documentación comunitaria"],
            ["Práctica 6, MicroStack", "16 GB como punto ideal de la guía", "40 GB o más", "Guía de la práctica, no de Ubuntu"],
        ],
        [1.9, 1.85, 1.45, 1.3],
        "Requisitos de memoria y disco. Cada fila es una edición distinta. No existe «el requisito de Linux».",
    )
    paper.figure(
        "12-ram.png",
        "Memoria de referencia en gigabytes. La barra de MicroStack es el punto ideal de la práctica 6, no el mínimo de Ubuntu. Los 4 GB del escritorio Ubuntu son referencia práctica de este trabajo; el resto de las barras sale de las guías citadas en el texto.",
    )
    P(
        doc,
        "La figura se lee de un vistazo y se interpreta con cuidado. Alpine y Debian sin escritorio casi no se ven junto a los 16 GB, y ese es el dato. El apellido Linux no fija la memoria. La fija la edición y, sobre todo, lo que se le va a pedir al equipo. Los 16 GB no son un requisito de Ubuntu Server, cuya propia documentación sugiere 3 GB. Son el punto ideal que la guía de la práctica 6 marca para levantar MicroStack, una nube privada de OpenStack, dentro de una máquina virtual (Muñoz Hinojosa, 2026b).",
    )

    H(doc, "6.1 Una PC de 2015 frente a dos sistemas", 2)
    P(
        doc,
        "Sirve un ejemplo con números cerrados. Una computadora de laboratorio de 2015, con procesador de dos núcleos, 4 GB de RAM y un disco de 128 GB, se compara con dos listas. Windows 11 pide un procesador de 64 bits compatible a 1 GHz con dos o más núcleos, 4 GB de RAM, 64 GB de almacenamiento, firmware UEFI con arranque seguro y TPM 2.0 (Microsoft, s. f.). Muchas máquinas de 2015 cumplen la memoria y el disco, y fallan en el TPM o en el procesador, porque muchos modelos de ese año no están en la lista de compatibilidad. El disco de 128 GB sí cubre los 25 GB que el tutorial de Ubuntu Desktop 24.04 exige. La memoria es el punto justo: 4 GB alcanzan para abrir el sistema y se quedan cortos cuando conviven el escritorio GNOME y el navegador. Debian con un escritorio ligero —Xfce, por ejemplo— está descrito para esa memoria: la propia guía dice que, por debajo de GNOME o KDE, conviene un gestor de ventanas más sobrio (Debian, s. f.).",
    )
    P(
        doc,
        "El requisito, en esa mesa, no es de ideología. Es de ajuste. El sistema libre que corresponde a esa PC es el que deja memoria para el navegador, no el que gana una comparativa de capturas de pantalla.",
    )

    H(doc, "7. El requisito de una organización")
    P(
        doc,
        "Una organización que va a vivir sobre el sistema tiene requisitos que ninguna tabla de RAM lista. Hace falta al menos una persona que sepa instalar, actualizar y recuperar un equipo. Hace falta un inventario de los programas de trabajo: los que ya tienen versión libre, los que corren igual, y los que solo existen para Windows y van a quedarse en un puesto de excepción. Hace falta una política de actualizaciones, aunque sea «el primer lunes del mes». Y hace falta decidir el orden. La Gendarmería francesa cambió la suite de oficina en 2004, el navegador y el correo en 2006, y dio por cerrada la migración del sistema años después. Schleswig-Holstein, entre 2025 y 2026, repitió ese orden: LibreOffice y el correo primero, Linux en la cancillería después, con puestos que se quedan fuera por un programa especializado (Schleswig-Holstein, 2026).",
    )
    P(
        doc,
        "El requisito económico se enuncia sin una tabla de precios inventada. Se deja de pagar la licencia del sistema por equipo. Se empieza a pagar, si se quiere un compromiso de respuesta, la suscripción de quien da soporte, y se paga siempre el tiempo de quien administra. Un laboratorio de veinte máquinas no necesita un contrato empresarial: le basta una imagen y una persona que sepa reinstalarla. Un clúster que aparece en el TOP500 con RHEL sí está comprando ese compromiso. Las dos decisiones cumplen los requisitos. No son la misma decisión.",
    )

    H(doc, "8. Ejemplos resueltos")
    P(
        doc,
        "Los tres ejemplos que siguen usan solo cifras que ya están en las guías citadas. No son una recomendación de compra. Son el modo de aplicar la tabla 1 a un equipo que existe.",
    )

    H(doc, "8.1 Tres equipos", 2)
    paper.figure(
        "13-escenarios.png",
        "El mismo método —mirar la carga antes que el nombre del sistema— en tres equipos distintos.",
    )
    P(
        doc,
        "En el laboratorio de 2015, con 4 GB de RAM, la edición que cabe con holgura es Debian o una derivada con escritorio Xfce. Ubuntu Desktop cubre el disco —128 GB frente a los 25 GB del tutorial— y en la memoria queda al límite: GNOME y el navegador se pisan. El requisito que manda, en estas máquinas, es la memoria, no el disco.",
    )
    P(
        doc,
        "En un sitio web pequeño del grupo, metido en una máquina virtual de 1 GB de RAM y 10 GB de disco, el escritorio estorba. Debian sin escritorio recomienda 512 MB y 4 GB de disco. Alpine está en un orden de magnitud todavía menor. El sistema sobra. Lo que puede no caber es la aplicación: un sitio de páginas fijas cabe, una base de datos grande no. El requisito que hay que escribir en el informe es el de la aplicación, y al lado, en una línea, el del sistema.",
    )
    P(
        doc,
        "En la práctica 6 la guía pide Ubuntu, virtualización anidada, y como punto ideal 4 CPU, 16 GB de RAM y 40 GB o más de disco (Muñoz Hinojosa, 2026b). Llegar a la práctica con el mínimo de Ubuntu Server —1,5 GB de RAM y 5 GB de disco— produce una instalación que «cumple el requisito de Ubuntu» y no cumple el requisito de OpenStack. Las dos listas tienen que estar en la misma página del reporte de práctica.",
    )

    H(doc, "8.2 Comprobar el sistema en la terminal", 2)
    P(
        doc,
        "Parte del requisito se puede leer en el equipo, no solo en la guía. Dos comandos dicen qué núcleo corre y qué distribución lo empaqueta. La salida de abajo es un ejemplo recortado, del estilo de Ubuntu 24.04, no el volcado de una máquina concreta.",
    )
    paper.code(
        """
$ uname -srm
Linux 6.8.0-45-generic x86_64

$ cat /etc/os-release
NAME="Ubuntu"
VERSION="24.04.1 LTS (Noble Numbat)"
ID=ubuntu
"""
    )
    P(
        doc,
        "uname dice el núcleo, la revisión y la arquitectura. os-release dice la distribución. Con las dos líneas se evita el error de llamar «Linux» a secas a lo que en el informe debe decir Ubuntu 24.04 sobre un núcleo 6.8, en amd64. Para el requisito de firmware, en Debian y Ubuntu se puede preguntar si el paquete de blobs está instalado:",
    )
    paper.code(
        """
$ dpkg -l linux-firmware 2>/dev/null | awk '/^ii/ {print $2, $3}'
linux-firmware 20240318.git3b128b60-0ubuntu2.x
"""
    )
    P(
        doc,
        "Si ese paquete está instalado, el sistema incluye firmware que no cumple la lista estricta de la FSF, aunque el núcleo siga siendo GPL-2.0. La salida no condena la instalación. La clasifica. En un informe de práctica basta una frase: «se usó Ubuntu, con firmware no libre, porque el equipo necesitaba la red». Esa frase cumple el requisito de honestidad que la definición pide.",
    )

    H(doc, "8.3 La práctica 4 y la práctica 6", 2)
    P(
        doc,
        "La práctica 4 de este taller armó una VPN con WireGuard sobre CachyOS, una distribución basada en Arch (Muñoz Hinojosa, 2026a). El requisito técnico era concreto. WireGuard vive en el núcleo Linux desde hace años, así que hacía falta un núcleo que lo trajera, el paquete wireguard-tools, systemd para dejar el túnel levantado, y una red entre los dos extremos. CachyOS los cumplía. El requisito de definición estricta es otra casilla: CachyOS, como Arch, ofrece firmware y programas que no son libres dentro de sus repositorios oficiales. La práctica podía terminar bien y, a la vez, no servir como ejemplo de distribución de la lista de la FSF. Separar las casillas es el objetivo de este trabajo.",
    )
    P(
        doc,
        "La práctica 6 cambia de distribución por un requisito de empaquetado, no por un requisito de libertad. MicroStack se distribuye como snap y la guía está escrita para Ubuntu. CachyOS no era el sistema de esa guía. El requisito aquí es de procedimiento: usar el sistema para el que está probada la herramienta, con el punto ideal de CPU, memoria y disco que la propia guía escribe. Mezclar las dos prácticas en una frase del tipo «usamos Linux» borra justo lo que había que reportar.",
    )

    H(doc, "8.4 Lista de comprobación antes de instalar", 2)
    P(
        doc,
        "La lista cabe en una página y recoge los requisitos de este trabajo en el orden en que se atropellan cuando alguien instala con prisa.",
    )
    bullet(doc, "Arquitectura del procesador, y una imagen hecha para esa arquitectura.", numbered=1)
    bullet(doc, "Memoria y disco comparados con la edición, no con la palabra Linux. Si hay una carga distinta —un escritorio pesado, una base de datos, OpenStack—, se anota esa carga al lado.", numbered=2)
    bullet(doc, "Modo de arranque: UEFI o legado, y si el arranque seguro está activo.", numbered=3)
    bullet(doc, "Copia de lo que ya vive en el disco, antes de elegir «borrar e instalar».", numbered=4)
    bullet(doc, "Firmware. Si el Wi-Fi o el video exigen un blob, se decide si se acepta Ubuntu, Debian con firmware o una distribución estricta.", numbered=5)
    bullet(doc, "Quién instala las actualizaciones el mes que viene. Si la respuesta es nadie, el requisito de empaquetado está sin cumplir.", numbered=6)
    bullet(doc, "Programas de trabajo. Los que no existen para el sistema nuevo se quedan nombrados, en un puesto de excepción, no escondidos.", numbered=7)

    H(doc, "9. Conclusiones")
    P(
        doc,
        "Un sistema operativo libre tiene requisitos de distinta naturaleza, y tratarlos como una sola lista produce errores de informe. El requisito de definición son las cuatro libertades, con el código fuente como condición de estudiar y de publicar cambios. El requisito jurídico es una licencia libre por cada pieza, y un conjunto que se pueda redistribuir. El requisito de la distribución completa, en la lista de la FSF, excluye el firmware cerrado y los repositorios que empujan hacia él. Ubuntu, Debian en su imagen habitual y CachyOS fallan esa lista y siguen siendo sistemas utilizables, mayoritariamente abiertos y suficientes para las prácticas de este taller.",
    )
    P(
        doc,
        "El requisito de arquitectura pide núcleo, espacio de usuario, arranque, servicios, empaquetado y un firmware que el hardware a veces impone. El requisito de hardware no es único: Debian 12 sin escritorio recomienda 512 MB, Ubuntu Server sugiere 3 GB y una sesión de escritorio con GNOME, en la práctica, pide unos 4 GB. La práctica 6 sube a 16 GB porque OpenStack no es el sistema: es la carga. El requisito de una organización pide personas, orden de migración y una lista honesta de los programas que no se van a mover.",
    )
    P(
        doc,
        "La frase que resume las dos investigaciones del taller es corta. Libre no es sinónimo de gratuito, ni de «trae núcleo Linux», ni de «corre en cualquier PC vieja». Es un permiso sobre el código, más una pila que arranca, más un ajuste al equipo que se tiene enfrente. Los ejemplos de NGINX, de Trisquel, del laboratorio de 2015 y de las prácticas 4 y 6 muestran las cuatro lecturas sobre objetos que se pueden señalar.",
    )

    H(doc, "Referencias")
    refs = [
        "Canonical. (s. f.-a). Install Ubuntu Desktop. https://ubuntu.com/desktop/docs/en/24.04/tutorial/install-ubuntu-desktop/",
        "Canonical. (s. f.-b). Ubuntu Server system requirements. https://ubuntu.com/server/docs/reference/installation/system-requirements/",
        "Debian. (s. f.). Debian GNU/Linux installation guide. Bookworm, arquitectura amd64. https://www.debian.org/releases/bookworm/amd64/",
        "Free Software Foundation. (s. f.-a). ¿Qué es el software libre? Proyecto GNU. https://www.gnu.org/philosophy/free-sw.es.html",
        "Free Software Foundation. (s. f.-b). Directrices para distribuciones de sistemas libres. https://www.gnu.org/distros/free-system-distribution-guidelines.es.html",
        "FreeBSD. (2021). Handbook, serie 12.2. Requisitos mínimos de hardware. https://docs-archive.freebsd.org/doc/12.2-RELEASE/usr/local/share/doc/freebsd/en/books/handbook/bsdinstall-hardware.html",
        "Gallatin, D. (2023). The magical mystery merge: Why we run FreeBSD-current at Netflix [presentación]. OpenFest. https://people.freebsd.org/~gallatin/talks/OpenFest2023.pdf",
        "Microsoft. (s. f.). Windows 11 requirements. https://learn.microsoft.com/en-us/windows/whats-new/windows-11-requirements",
        "Muñoz Hinojosa, C. (2026a). Práctica 4. Creación de una red privada virtual con WireGuard en CachyOS. Taller de sistemas operativos, Instituto Tecnológico de Morelia.",
        "Muñoz Hinojosa, C. (2026b). Práctica 6. Implementación de nubes privadas con MicroStack en Ubuntu. Taller de sistemas operativos, Instituto Tecnológico de Morelia.",
        "Netflix. (s. f.). Open Connect appliances. https://openconnect.netflix.com/en/appliances/",
        "Schleswig-Holstein. (2026, 19 de septiembre). Staatskanzlei nutzt Linux. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2026/cds/260919_cds_linux_stk",
        ]
    for ref in refs:
        paper.reference(ref)
    path = OUT / "Investigacion-2-Requisitos-SO-libres-CristianMunoz-23121073.docx"
    doc.save(path)
    print(path)
    return path


def main():
    figuras.main()
    doc_empresas()
    doc_requisitos()


if __name__ == "__main__":
    main()
