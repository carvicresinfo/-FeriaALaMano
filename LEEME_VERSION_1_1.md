# Feria a la Mano v1.1 — Catálogo Gran Santiago

Este proyecto compila un APK Android con GitHub Actions. **En cada compilación** descarga un CSV público derivado de datos ODEPA, filtra comunas del Gran Santiago y genera `app/src/main/assets/ferias.json` antes de compilar. Por tanto, la APK resultante contiene el catálogo descargado y funciona sin conexión para búsquedas. La versión ZIP incluye tres registros iniciales solo como respaldo de desarrollo; **no son el catálogo ampliado**.

## Uso
Subir el contenido de la carpeta `FeriaALaMano` a la raíz del repositorio GitHub, incluida `.github/workflows/android-apk.yml`. En Actions > Compilar APK de prueba > Run workflow, esperar a que termine y descargar el artefacto `FeriaALaMano-APK-prueba`. Si falla la importación, revisar el registro de ejecución: el proceso falla en lugar de generar una APK que aparente tener cobertura completa.

Fuente de datos: https://github.com/geoidegeoidal/ferias-chile (datos recopilados de ODEPA). Información sujeta a cambios; los horarios y tramos deben contrastarse con los municipios. Algunas comunas pueden no tener registros en el conjunto publicado. No implica cobertura exhaustiva ni actualizaciones automáticas de la app instalada.

Para instalar como actualización sobre la versión anterior, la APK debe tener el mismo identificador de aplicación y una firma compatible. Una APK de depuración compilada en otro entorno puede usar una clave diferente, en cuyo caso Android exigirá desinstalar la anterior (se pierden los datos locales de esa instalación).
