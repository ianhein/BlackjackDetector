import cv2
import cvzone
import torch
from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO("playingCards.pt")

# Nombres de las clases de las cartas
classNames = ['10 de Trebol', '10 de Diamante', '10 de Corazon', '10 de Pica',
              '2 de Trebol', '2 de Diamante', '2 de Corazon', '2 de Pica',
              '3 de Trebol', '3 de Diamante', '3 de Corazon', '3 de Pica',
              '4 de Trebol', '4 de Diamante', '4 de Corazon', '4 de Pica',
              '5 de Trebol', '5 de Diamante', '5 de Corazon', '5 de Pica',
              '6 de Trebol', '6 de Diamante', '6 de Corazon', '6 de Pica',
              '7 de Trebol', '7 de Diamante', '7 de Corazon', '7 de Pica',
              '8 de Trebol', '8 de Diamante', '8 de Corazon', '8 de Pica',
              '9 de Trebol', '9 de Diamante', '9 de Corazon', '9 de Pica',
              'A de Trebol', 'A de Diamante', 'A de Corazon', 'A de Pica',
              'J de Trebol', 'J de Diamante', 'J de Corazon', 'J de Pica',
              'K de Trebol', 'K de Diamante', 'K de Corazon', 'K de Pica',
              'Q de Trebol', 'Q de Diamante', 'Q de Corazon', 'Q de Pica']

# Función para detectar cartas en la imagen
def detect_cards(image, model, classNames, threshold=0.5):
    results = model(image)
    cards = {}
    for r in results:
        for box in r.boxes:
            conf = box.conf[0].item()
            if conf > threshold:
                cls_id = int(box.cls[0])
                if cls_id < len(classNames):
                    bbox = box.xyxy[0].tolist()
                    x1, y1, x2, y2 = map(int, bbox)
                    w, h = x2 - x1, y2 - y1
                    if classNames[cls_id] in cards:
                        cards[classNames[cls_id]].append((x1, y1, w, h, conf))
                    else:
                        cards[classNames[cls_id]] = [(x1, y1, w, h, conf)]
    return cards



# Función para dibujar las detecciones
def draw_detections(image, detections):
    for card, bbox_list in detections.items():
        for bbox in bbox_list:
            x1, y1, w, h, conf = bbox
            image = cvzone.cornerRect(
                image,  # La imagen en la que se dibuja
                (x1, y1, w, h),  # Posición y dimensiones del rectángulo (x, y, ancho, alto)
                l=7,  # Longitud de los bordes de las esquinas
                t=2,  # Grosor de los bordes de las esquinas
                rt=1,  # Grosor del rectángulo
                colorR=(255, 0, 255),  # Color del rectángulo
                colorC=(0, 255, 0)  # Color de los bordes de las esquinas
            )
            cvzone.putTextRect(image, f'{card} {conf:.2f}', (x1, y1 - 10), scale=2.5, thickness=2, colorR=(0, 0, 0), colorT=(255, 255, 255))


# Función para calcular el valor de la mano de Blackjack
def calculate_hand_value(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    hand_value = 0
    ace_count = 0

    for card in hand:
        # Extraer solo el valor de la carta, que es el primer elemento antes del espacio
        card_value = card.split(' ')[0]
        hand_value += values[card_value]
        if card_value == 'A':
            ace_count += 1

    # Adjust for aces
    while hand_value > 21 and ace_count:
        hand_value -= 10
        ace_count -= 1

    return hand_value

# Función para verificar si la mano es un Blackjack
def is_blackjack(hand):
    return calculate_hand_value(hand) == 21 and len(hand) == 2

# Configuración de la captura de video
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Ancho de la ventana de captura
cap.set(4, 720)  # Altura de la ventana de captura

if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se puede leer el frame.")
        break

    # Detectar cartas
    detected_cards = detect_cards(frame, model, classNames)

    # Dibujar detecciones
    draw_detections(frame, detected_cards)

    # Calcular el valor de la mano
    hand = list(detected_cards.keys())
    hand_value = calculate_hand_value(hand)

    # Verificar si la mano es un Blackjack
    blackjack = is_blackjack(hand)

    # Mostrar el valor de la mano en la imagen
    if hand:  # Mostrar el texto solo si se detecta al menos una carta
        if blackjack:
            cvzone.putTextRect(frame, "Blackjack!", (300, 75), scale=3, thickness=5)
        else:
            cvzone.putTextRect(frame, f'Tu mano: {hand_value}', (300, 75), scale=3, thickness=5)

    cv2.imshow("IA TP2 RNA | Ian Hein", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
