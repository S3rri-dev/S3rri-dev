# Verificación de la presentación pública

4 de noviembre de 2026 · Europe/Madrid.

## Resultado observado

| Comprobación | Resultado |
| --- | --- |
| Perfil público sin cookies ni autenticación | HTTP 200; nombre profesional y enlaces a los dos casos presentes |
| Cuenta de publicación | S3rri-dev, verificada antes de las escrituras |
| Bio y contactos | Guardados; correo profesional y LinkedIn visibles |
| Estado público | Abierto a oportunidades · software y sistemas |
| Proyectos fijados | Nodal y Caudal, en ese orden |
| Tarjetas sociales | Perfil, Nodal y Caudal: personalizadas y HTTP 200 sin sesión |
| Presentación inglesa | Contenido, imágenes y enlaces de los dos casos representados en GitHub |
| Diagramas | Ambos Mermaid representados con nodos y conexiones en GitHub |
| Vista 390 × 844 | Ancho de documento 390; dos tablas con clientWidth y scrollWidth 308; sin desbordamiento |
| Imágenes de la portada | Las cuatro cargadas: cabecera, dos capturas y cierre |
| Sintaxis SVG y enlaces locales | xmllint y scripts/check_links.py correctos |
| Destinos remotos de los README/casos | 23 HTTP 200; LinkedIn se conserva como enlace profesional previamente configurado |

La vista de teléfono es una comprobación de tamaño de navegador, no una prueba en un teléfono físico. La revisión visual no constituye una auditoría completa de accesibilidad. El diseño general de GitHub y el tema elegido por cada visitante quedan bajo control de GitHub y del visitante.

Las capturas de evidencia están en output/, fuera de Git. Los recursos públicos y su procedencia se describen en [assets/README.md](../assets/README.md).

## Actualización de enlaces sociales

Instagram se añadió como segunda red pública, conservando LinkedIn. Se comprobó en Safari el icono nativo de Instagram y el enlace serri.18, además de los botones de LinkedIn, Instagram y correo en la portada real de GitHub.

Los README español e inglés incluyen los mismos destinos y botones locales, con etiqueta de correo traducida. Se revisaron ambos grupos en Safari dentro de un contenedor de 308 px; los tres botones caben en una fila y los símbolos y textos se dibujan sin recortes. Es una previsualización compacta de los componentes.

El perfil sin autenticación respondió HTTP 200 y contenía el enlace de Instagram y el nuevo marcado. Los cuatro recursos SVG publicados respondieron HTTP 200. scripts/check_links.py comprobó 30 enlaces locales y todos los SVG, incluidos los glifos anidados. Licencia MIT y procedencia incluidas en assets/icons/.

## Aplicaciones enlazadas

Nodal: 135 comprobaciones Swift y 50 JavaScript, compilación y auditoría de fuentes/bundle correctas. [Informe](https://github.com/S3rri-dev/nodal/blob/main/docs/VERIFICATION.md).

Caudal: 52 comprobaciones de datos, 64 de WebKit real, 11 de aislamiento, compilación y auditoría de fuentes/bundle correctas. [Informe](https://github.com/S3rri-dev/caudal/blob/main/docs/VERIFICACION.md).

Las ejecuciones remotas revisadas (Nodal 41837435429 y Caudal 41842987922) terminaron con resultado global failure y trabajos cancelled sin ejecutar pasos. Las anotaciones de GitHub informan de falta de adquisición y restricciones de capacidad para ejecutores macOS ARM64. La portada enlaza las evidencias de cada proyecto y no anuncia esas CI como superadas.

## Reproducir las comprobaciones del perfil

    python3 scripts/check_links.py
    xmllint --noout assets/header.svg assets/header.en.svg assets/footer.svg
    swift scripts/render_social.swift

Después de publicar, revisar el perfil en GitHub, sus enlaces de descarga, la versión inglesa y los casos [Nodal](../proyectos/nodal.md) y [Caudal](../proyectos/caudal.md). La representación real en GitHub es la referencia para las limitaciones de Markdown y HTML.

## Cabecera animada y calendario público

Se publican composiciones originales, sin dependencia de GitSkins: gato aprobado con barrido de 2,3 segundos, nombre con entrada progresiva y panel de contribuciones. Cada composición cuenta con versiones de escritorio/móvil, español/inglés y movimiento/estática. Ocho archivos estáticos no contienen keyframes. El PNG original del avatar no cambia; las cabeceras incorporan una miniatura PNG de 480 px, sin recursos anidados externos.

Comprobaciones realizadas:

- Seis pruebas de integridad superadas: calendario completo, separadores de millares, exclusión de futuros, rechazo de duplicados, huecos, etiquetas desconocidas, niveles incoherentes y totales incorrectos.
- Generación reproducible de las 16 tarjetas y del documento textual de actividad; XML y 50 referencias locales correctos. Los 16 SVG publicados responden HTTP 200 y coinciden con los generados.
- GitHub real, escritorio con ancho observado de 1163 px: cabecera, gato y contactos visibles. Todas las imágenes del README cargan.
- GitHub real, 390 px: documento y scrollWidth de 390; tablas de 308 px sin desbordamiento. Las imágenes de portada y calendario eligen las variantes móviles y cargan correctamente. También se comprueba la presentación inglesa.
- Inicio y final de la animación observados en navegador. Las variantes estáticas se representan correctamente; GitHub conserva los source/media para movimiento reducido. No se modifican preferencias del sistema ni se declara una prueba con la preferencia del sistema activada.
- Contraste sobre negro: marfil 19:1, dorado 8,55:1, texto secundario 10,56:1 y celda activa roja 4,07:1. La actividad también tiene totales y tabla textual accesibles en docs/ACTIVITY.md. Es una revisión limitada, no una auditoría completa WCAG.
- Primera ejecución de [actualización automática](https://github.com/S3rri-dev/S3rri-dev/actions/runs/41884194589): success, todos los pasos ejecutados. El bot publica adcd7a0 con captura de las 19:08 Europe/Madrid. No se atribuyen al titular los commits automáticos.

El workflow se programa diariamente a las 06:23 UTC; GitHub puede retrasarlo. Consulta solo el calendario anónimo público, sin tokens. Valida antes de guardar y no publica si cualquier comprobación falla. En ese caso se conserva la última captura válida, con su fecha visible. La fecha y los recuentos vigentes se consultan en [Actividad](ACTIVITY.md), sin duplicarlos aquí como un dato permanente.

Evidencia local en output/perfil-animado-publicado.jpg, output/perfil-animado-movil.jpg y output/actividad-publica-movil.jpg, excluida de Git. La vista móvil es un tamaño de navegador, no una prueba en teléfono físico. La CI de las aplicaciones no se ha modificado con este trabajo.
