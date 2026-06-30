class Config:
    # НАСТРОЙКИ КАМЕРЫ
    # RTSP URL для IP-камеры
    RTSP_URL = "rtsp://CecLImul:5W94kDad@127.0.0.1:8554/webcam0"
    
    # Разрешение видеопотока
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480
    
    # Частота кадров
    CAMERA_FPS = 30
    
    # НАСТРОЙКИ РАСПОЗНАВАНИЯ
    AGE_THRESHOLD = 18          # Порог совершеннолетия
    DETECTION_INTERVAL = 5      # Проверка каждые N кадров
    MIN_FACE_SIZE = 60          # Минимальный размер лица
    FACE_CONFIDENCE_THRESHOLD = 0.5  # Порог уверенности (0-1)
    REQUIRED_CONFIRMATIONS = 3  # Кол-во подтверждений для блокировки
    
    # НАСТРОЙКИ БЛОКИРОВКИ
    BLOCK_DURATION = 60         # Длительность блокировки (секунд)
    BLOCK_MESSAGE = "ДОСТУП ЗАПРЕЩЁН\nВозраст пользователя не соответствует требованиям.\nПовторите попытку через 60 секунд."
    
    # РЕЖИМ РАБОТЫ
    GUI_MODE = True             # True - отладка с видео, False - фоновый режим
    
    # ПУТИ К МОДЕЛЯМ
    MODEL_PATH = "models"
    FACE_PROTOTXT = "models/opencv_face_detector.pbtxt"
    FACE_MODEL = "models/opencv_face_detector_uint8.pb"
    AGE_PROTOTXT = "models/age_deploy.prototxt"
    AGE_MODEL = "models/age_net.caffemodel"