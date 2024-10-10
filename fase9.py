import cv2

# Inicializa a captura de vídeo (0 para a webcam padrão)
cap = cv2.VideoCapture(0)

# Verifica se a câmera abriu corretamente
if not cap.isOpened():
    print("Não foi possível acessar a câmera")
    exit()

# Captura um frame da câmera
ret, frame = cap.read()

# Se a captura foi bem-sucedida, salva a imagem
if ret:
    cv2.imwrite("captura.png", frame)
    print("Imagem capturada e salva como 'captura.png'")
else:
    print("Falha na captura da imagem")

# Libera a captura e fecha todas as janelas do OpenCV
cap.release()
cv2.destroyAllWindows()
