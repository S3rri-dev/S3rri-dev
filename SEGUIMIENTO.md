# Seguimiento del perfil S3rri

## 4 de noviembre de 2026 — cabecera animada y actividad

Se implementa una cabecera original con el gato aprobado, barrido de revelado e introducción progresiva de S3rri.dev. Se generan composiciones específicas de escritorio y móvil, español e inglés, y alternativas estáticas por preferencia de movimiento reducido. El barrido dura 2,3 segundos contando el retardo; no se repite. El PNG original del avatar permanece intacto.

El panel utiliza 365 fechas del calendario anónimo público de GitHub, sin token ni acceso privado. La captura inicial contiene 17 contribuciones en un día activo; los valores y la fecha se generan desde data/activity.json. El documento docs/ACTIVITY.md ofrece totales y tabla textual accesibles. No se infieren horas ni calidad.

Se prepara actualización diaria mediante GitHub Actions en Ubuntu, Python estándar, acción checkout fijada por SHA e identidad github-actions[bot]. El proceso valida integridad antes de guardar y solo publica si terminan las comprobaciones. Publicado y comprobado en el perfil real. La primera ejecución remota, 41884194589, termina en success: descarga, seis pruebas, generación, validación y commit/publicación completados. El bot produce adcd7a0; la copia local se sincroniza mediante avance rápido.

Comprobaciones locales: seis pruebas de integridad de datos superadas; 50 referencias locales y SVG válidos; generación reproducible; ocho variantes estáticas sin keyframes. Contraste sobre negro: marfil 19:1, dorado 8,55:1, texto secundario 10,56:1; celda activa roja 4,07:1. Revisión visual del inicio y final de la animación, y composición móvil cargada con todos los recursos. En GitHub real se comprueban escritorio de 1163 px y móvil de 390 px, sin desbordamiento horizontal; ambas tablas miden 308 px en móvil. Las versiones móvil española e inglesa seleccionan los recursos correctos y cargan la cabecera y el panel. Los 16 SVG públicos responden HTTP 200 y coinciden con los locales. No se declara auditoría completa de accesibilidad ni prueba en teléfono físico.

## 4 de noviembre de 2026 — redes sociales

Se añade Instagram, con el enlace aportado por el titular, como segunda red en los campos públicos de GitHub. GitHub representa su icono junto al enlace. Se añaden botones con iconos de LinkedIn, Instagram y correo a la introducción y al contacto de los README español e inglés.

Los botones son SVG locales con colores del perfil y nombres accesibles. Tres glifos de Bootstrap Icons se conservan fijados por commit, con licencia MIT incluida; la composición se regenera mediante scripts/render_social_links.py.

Comprobaciones: 30 enlaces locales y SVG válidos; perfil público sin sesión HTTP 200, con Instagram y el nuevo marcado visibles; los cuatro SVG de botones responden HTTP 200. Revisión real de GitHub en Safari y previsualización de los componentes en un contenedor de 308 px, español e inglés, sin recortes. Capturas guardadas en output/, excluido de Git.

## 4 de noviembre de 2026

Publicado el repositorio especial S3rri-dev/S3rri-dev como portada del perfil. Enfoque elegido: desarrollo de software e integración de sistemas, con formación de Ingeniería Telemática y experiencia en aviónica de UAH MotorSport.

Identidad: avatar del gato angular aprobado, negro, rojo oscuro, marfil y dorado; cabeceras SVG editables y tres tarjetas sociales originales. La bio, el estado de contacto y los enlaces profesionales están guardados. Nodal y Caudal quedan fijadas en ese orden.

Contenido: presentación español/inglés, dos proyectos con capturas ficticias de demostración, casos técnicos con diagramas, enlaces al código, comprobaciones y descargas. Los README de ambas aplicaciones enlazan sus casos. Cada producto conserva su identidad.

Verificación: perfil accesible sin sesión por HTTP 200, nombre y dos casos visibles; tres tarjetas sociales personalizadas accesibles sin sesión por HTTP 200. Enlaces locales y SVG correctos; 23 destinos remotos de los README/casos respondieron HTTP 200. Revisión visual de escritorio, vista 390 × 844 sin desbordamientos, cuatro imágenes cargadas y dos diagramas Mermaid dibujados. Evidencia de pantalla en output/, excluida de Git.

Se repitieron las comprobaciones locales de las aplicaciones: Nodal, 135 Swift y 50 JavaScript más build/auditoría; Caudal, 52 de datos, 64 de UI, 11 de aislamiento más build/auditoría. Correctas. Los cambios en esos repositorios son documentales; no se sustituyen las releases.

La CI remota anterior de ambas aplicaciones no obtuvo ejecutores macOS y terminó sin ejecutar pasos. Su estado se conserva visible y está explicado en sus informes; las comprobaciones locales no se presentan como CI superada.

Mantenimiento: añadir futuros proyectos solo con código o artefactos revisables, casos concretos y estado real. Las descargas enlazan Releases/latest para evitar duplicar números de versión en el perfil.
