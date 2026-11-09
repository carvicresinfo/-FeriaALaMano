# Compilar Feria a la Mano sin Android Studio

1. Crea una cuenta gratuita en https://github.com y un repositorio llamado `FeriaALaMano`.
2. Descomprime el ZIP y sube **el contenido de la carpeta FeriaALaMano**, incluida la carpeta `.github` (está oculta en algunos exploradores), a la raíz del repositorio. En GitHub puedes usar Add file > Upload files desde un navegador en modo escritorio.
3. En el repositorio, abre Actions > Compilar APK de prueba > Run workflow.
4. Cuando termine con marca verde, abre la ejecución y descarga el artefacto `FeriaALaMano-APK-prueba`.
5. Descomprime ese artefacto: contiene `app-debug.apk`. Instálalo en Android autorizando instalación desde esa fuente si corresponde.

Si falla la compilación, abre la ejecución, selecciona el paso rojo y comparte el error para corregir el proyecto. La compilación no ha sido verificada aún.

NOTA: Esta versión es un prototipo con tres registros de muestra de Santiago, no un catálogo completo del Gran Santiago. El AAB firmado para Play Store es una fase posterior.
