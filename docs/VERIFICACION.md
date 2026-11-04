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
