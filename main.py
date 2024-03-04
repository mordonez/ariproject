import cv2
import pandas as pd
import os

def extract_frames(video_path, csv_path, output_folder, size=None):
    # Leer el archivo CSV
    df = pd.read_csv(csv_path, delimiter=';', decimal=',')

    # Asegurarse de que la carpeta de salida existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abrir el video
    cap = cv2.VideoCapture(video_path)

    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Obtener el segundo del video
        second = row['Frame']

        # Calcular el frame correspondiente
        cap.set(cv2.CAP_PROP_POS_MSEC, second*1000)

        # Leer el frame
        ret, frame = cap.read()

        # Si el frame se leyó correctamente, guardarlo como imagen PNG
        if ret:
            # Obtener las dimensiones de la imagen
            height, width = frame.shape[:2]

            # Calcular la diferencia en tamaño para hacer la imagen cuadrada
            diff = abs(height - width)

            # Añadir bordes si es necesario
            if height > width:
                frame = cv2.copyMakeBorder(frame, 0, 0, diff // 2, diff // 2, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            elif width > height:
                frame = cv2.copyMakeBorder(frame, diff // 2, diff // 2, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])

            # Cambiar el tamaño de la imagen al tamaño especificado si se proporcionó un tamaño
            if size is not None:
                frame = cv2.resize(frame, (size, size))

            cv2.imwrite(os.path.join(output_folder, f'{second}.png'), frame)
            print(f"Done: {second}")

    # Liberar el video
    cap.release()

# Uso de la función

# Example with frames at original size
extract_frames('video.mp4', 'data.csv', 'frames')

# Example resize the frames to 600x600
#extract_frames('video.mp4', 'data.csv', 'frames', 600)
