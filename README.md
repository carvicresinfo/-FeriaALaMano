# Feria a la Mano — prototipo Android
Proyecto Kotlin + Jetpack Compose. Catálogo local JSON de ejemplo, basado en la página de la Municipalidad de Santiago (https://www.munistgo.cl/ferias/). Los tres registros son solo una muestra, no representan toda la cobertura del Gran Santiago. No se han verificado coordenadas, por eso Maps utiliza búsqueda de texto. El prototipo no incluye todavía notificaciones, política de privacidad publicada, selector claro/sistema ni persistencia de ajustes. La opción letras grandes es un control visual pendiente de aplicar al tema.

## Compilación
Abrir la carpeta en Android Studio, instalar Android SDK 35 y JDK 17, sincronizar Gradle, y ejecutar Build > Build APK(s). Para AAB: Build > Generate Signed Bundle / APK, crear y custodiar una clave de firma release. No se incluye gradle wrapper ni binarios precompilados.
