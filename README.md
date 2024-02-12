# AriProject

Este script de Python utiliza OpenCV para extraer fotogramas específicos de un video. Los segundos de los fotogramas a extraer se especifican en un archivo CSV en la columna Frame

## Dependencias

El script depende de las siguientes bibliotecas de Python:

- OpenCV (cv2)
- pandas
- os

## Uso

El script define una función `extract_frames` que toma tres argumentos:

- `video_path`: la ruta al archivo de video del que se extraerán los fotogramas.
- `csv_path`: la ruta a un archivo CSV que contiene los segundos de los fotogramas a extraer. El archivo CSV debe tener una columna llamada 'Frame' que contiene los segundos.
- `output_folder`: la ruta a la carpeta donde se guardarán los fotogramas extraídos. Si la carpeta no existe, se creará.

La función `extract_frames` abre el video, lee el archivo CSV y extrae el fotograma correspondiente a cada segundo especificado en el CSV. Cada fotograma se guarda como una imagen PNG en la carpeta de salida.

## Ejemplo de uso

```
extract_frames('video.mp4', 'data.csv', 'frames')
```

En este ejemplo, el script extraerá los fotogramas especificados en 'data.csv' del video 'video.mp4' y guardará las imágenes en la carpeta 'frames'.