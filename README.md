# GCP Data Engineer Course

## Introducción al Curso

Este curso integral de Google Cloud Professional Data Engineer te guía desde los fundamentos hasta las técnicas avanzadas de ingeniería de datos en la nube. Comenzamos configurando tu entorno de trabajo en GCP y aprendiendo a evitar errores costosos en Cloud Storage. Exploramos el uso de datasets públicos en BigQuery y construimos tu primer pipeline en Dataflow con Python y Apache Beam. A medida que avanzamos, automatizamos pipelines con Cloud Composer y dominamos la selección del sistema de almacenamiento adecuado según cada caso de uso. El curso cubre diseño de modelos de datos, implementación de Data Lakes, y arquitecturas modernas como Data Mesh con Dataplex. Aprendemos a preparar y compartir datos con seguridad, realizar feature engineering para Machine Learning, optimizar costos en BigQuery y Dataproc, y monitorear pipelines con herramientas nativas de GCP. Finalmente, abordamos diseño de sistemas tolerantes a fallos y culminamos con un portfolio completo en GitHub que demuestra tu capacidad para construir soluciones de datos escalables, eficientes y profesionales en Google Cloud Platform.

## Comandos Esenciales

1. git clone https://github.com/gsalfate-code/gcp-data-engineer-course.git
   - Descarga el repositorio completo a tu máquina local.
   - Crea una copia local de todos los archivos y código del curso.

2. gcloud auth application-default login
   - Autentica tu máquina local con Google Cloud usando credenciales por defecto.
   - Abre una ventana del navegador para iniciar sesión con tu cuenta de GCP.

3. gcloud config set project gcp-data-engineer-curso-481317
   - Configura el proyecto de Google Cloud que se usará por defecto.
   - Todas las operaciones posteriores se ejecutarán en este proyecto.

4. python create_bucket.py gcs-bucket-region-test
   - Ejecuta el script Python para crear un bucket en Cloud Storage.
   - "gcs-bucket-region-test" es el nombre único del bucket a crear.
   - Asegúrate de que el nombre sea único globalmente en GCP.

5. gsutil rm -r gs://gcs-bucket-region-test
   - Borra el bucket y todo su contenido de forma recursiva.
   - Advertencia: Esta acción es permanente e irreversible.
   - Asegúrate de tener backups si necesitas conservar los datos.

6. gcloud projects list
   - Lista todos los proyectos de Google Cloud asociados a tu cuenta.
   - Muestra ID del proyecto, nombre y número de proyecto.
   - Útil para verificar a qué proyectos tienes acceso.

7. gcloud projects delete thinking-anthem-474403-d5
   - Elimina permanentemente un proyecto de Google Cloud.
   - "thinking-anthem-474403-d5" es el ID del proyecto a eliminar.
   - **Advertencia**: Esta acción elimina todos los recursos del proyecto y es irreversible.

8. gcloud beta billing projects link gcp-dataflow-beam-pipeline --billing-account=01275F-58F205-2A181D
   - Asocia un proyecto de GCP con una cuenta de facturación específica.
   - Habilita la facturación para que el proyecto pueda consumir recursos.
   - "01275F-58F205-2A181D" es el ID de la cuenta de facturación.

9. gcloud beta billing projects describe gcp-dataflow-beam-pipeline
   - Muestra información sobre la configuración de facturación de un proyecto.
   - Verifica si el proyecto tiene facturación habilitada.
   - Muestra el ID de la cuenta de facturación asociada.

10. python create_bucket.py gcs-bucket-dataflow-beam
    - Ejecuta el script Python para crear un bucket específico para Dataflow y Apache Beam.
    - "gcs-bucket-dataflow-beam" debe ser un nombre único globalmente.
    - Este bucket se utilizará para almacenar datos temporales, plantillas y resultados de pipelines Dataflow.

11. gcloud billing projects unlink dataform-475303
    - Desasocia un proyecto de Google Cloud de su cuenta de facturación.
    - "dataform-475303" es el ID del proyecto a desvincular.
    - **Importante**: Esto deshabilita la facturación pero no elimina el proyecto.


12. pip install apache_beam
    - Instala la biblioteca Apache Beam para Python.
    - Necesario para desarrollar pipelines de procesamiento de datos en Dataflow.
    - Incluye todas las dependencias para ejecutar pipelines localmente y en GCP.