# Proyecto de Detección de Cartas de Blackjack con Red Neuronal Artificial (RNA)

## Introducción
Este proyecto utiliza una Red Neuronal Artificial (RNA) para detectar cartas de Blackjack en tiempo real utilizando una cámara web. El sistema identifica cada carta en la mano del jugador, calcula el valor total y determina si hay un Blackjack. Este sistema tiene aplicaciones potenciales en juegos de azar, educación y visión por computadora.

## Objetivos del Proyecto
- Detectar cartas de Blackjack usando una cámara en tiempo real.
- Calcular el valor total de la mano de Blackjack y determinar si es un Blackjack.

## Origen de los Datos
El modelo fue entrenado con el [Playing Cards Dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/1) que contiene imágenes de cartas de juego utilizadas para entrenar el modelo de detección YOLO.

## Créditos
Este proyecto se basó en ejemplos y tutoriales sobre detección de objetos con YOLO, incluyendo:
- Ejemplos de detección de cartas de juego
- Detección usando YOLO
- Curso: Object Detection 101

## Modificaciones Realizadas
- **Ajustes en el Modelo:** Mejoras en la precisión de detección de cartas.
- **Integración con OpenCV y cvzone:** Para visualización y procesamiento en tiempo real.
- **Cálculo del Valor de la Mano:** Lógica para calcular y verificar si es un Blackjack.

## Tecnologías Utilizadas
- **Python:** 3.11.7
- **Editor:** PyCharm
- **Librerías Principales:** `cvzone` (1.5.6), `ultralytics` (8.2.31), `opencv-python` (4.5.4.60)

## Requisitos
- **Hardware:** Cámara web y un sistema con potencia moderada.
- **Software:** Python 3.11.7 y las librerías mencionadas.
- **Conocimientos:** Familiaridad básica con Python y redes neuronales.

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone <https://github.com/ianhein/BlackjackDetector>
    ```
2. Instalar las dependencias:
    ```bash
    pip install cvzone ultralytics opencv-python
    ```

## Ejecución
1. Ejecutar el script principal:
    ```bash
    python main.py
    ```
2. Asegurarse de que la cámara esté conectada y accesible.

## Resultados y Pruebas
- **Pruebas en Diferentes Iluminaciones:** Detección precisa bajo distintas condiciones de luz.
- **Rendimiento en Tiempo Real:** Procesa cada cuadro en menos de 50 ms.
- **Cálculo Correcto de la Mano:** Incluye manejo de ases.
- **Identificación de Blackjack:** Detecta correctamente un Blackjack en la mano.
- ![Test - 1+](https://github.com/user-attachments/assets/cf924c4e-c592-4a27-bdbd-90fe46f1a47a)
- ![Test - 2+](https://github.com/user-attachments/assets/620f5c2f-0e68-440b-9608-c9102b48e33f)
- ![Test - 3+](https://github.com/user-attachments/assets/1ee3de9e-1fd5-4154-adf7-fd961ceecbec)





## Conclusiones
Este proyecto demuestra la capacidad de las redes neuronales y visión por computadora para aplicaciones de detección de cartas en tiempo real. Herramientas accesibles como Google Colab y datasets públicos permiten crear sistemas eficientes sin necesidad de grandes recursos.

## Autor
- Ian Edward Hein Prieto
