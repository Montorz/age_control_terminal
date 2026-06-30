import cv2
import time
from config import Config

class AgeControlSystem:
    def __init__(self):
        print("СИСТЕМА КОНТРОЛЯ ВОЗРАСТА ДЛЯ ТЕРМИНАЛОВ")
        
        self.config = Config()
        self.is_running = False
        self.cap = None
        self.frame_count = 0
        self.fps = 0
        self.last_fps_time = time.time()
        self.fps_counter = 0

        print(f"[INFO] Режим GUI: {'ВКЛЮЧЁН' if self.config.GUI_MODE else 'ВЫКЛЮЧЁН'}")

    
    def start(self):
        print("[INFO] Подключение к камере...")
        print(f"[INFO] RTSP URL: {self.config.RTSP_URL}")
        
        # Подавляем вывод ошибок FFMPEG
        import warnings
        warnings.filterwarnings("ignore")
        
        # Подключаемся к камере
        self.cap = cv2.VideoCapture(self.config.RTSP_URL, cv2.CAP_FFMPEG)
        
        if not self.cap.isOpened():
            print("[ERROR] Не удалось подключиться к камере!")
            print("[ERROR] Проверьте:")
            print("  1. Запущен ли Webcam Streamer")
            print("  2. Правильная ли ссылка в config.py")
            print(f"  3. Текущая ссылка: {self.config.RTSP_URL}")
            return False
        
        # Настройка параметров
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, self.config.CAMERA_FPS)
        
        # Получаем информацию о потоке
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        
        print(f"[INFO] Подключение установлено!")
        print(f"[INFO] Разрешение: {width}x{height}")
        print(f"[INFO] FPS: {fps:.1f}")
        print("[INFO] Нажмите 'q' для выхода\n")
        
        self.is_running = True
        self._main_loop()
        return True
    
    def _main_loop(self):
        print("[INFO] Запуск основного цикла...\n")
        
        while self.is_running:
            # Захват кадра
            ret, frame = self.cap.read()
            
            if not ret:
                # Пропускаем пустые кадры без вывода ошибки
                continue
            
            # Зеркалируем для естественного отображения
            frame = cv2.flip(frame, 1)
            
            # Считаем FPS
            self.fps_counter += 1
            if time.time() - self.last_fps_time >= 1.0:
                self.fps = self.fps_counter
                self.fps_counter = 0
                self.last_fps_time = time.time()
            
            self.frame_count += 1
            
            # ОТЛАДОЧНЫЙ РЕЖИМ (GUI)
            if self.config.GUI_MODE:
                display_frame = frame.copy()
                
                # Информация на кадре
                info = f"Frame: {self.frame_count} | FPS: {self.fps} | RTSP: Connected"
                cv2.putText(display_frame, info, (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                # Статус подключения
                cv2.putText(display_frame, "STATUS: CONNECTED", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
                
                # Управление
                cv2.putText(display_frame, "Press 'q' to quit", (10, 90),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
                
                # Показываем кадр
                cv2.imshow('Age Control System (Debug)', display_frame)
                
                # Обработка клавиш
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("\n[INFO] Выход по запросу пользователя")
                    self.stop()
                    break
    
    def stop(self):
        if not self.is_running:
            return
        
        print("\n[INFO] Остановка системы...")
        self.is_running = False
        
        if self.cap is not None:
            self.cap.release()
            print("[INFO] Камера освобождена")
            self.cap = None
        
        cv2.destroyAllWindows()
        print("[INFO] Система остановлена")

def main():
    system = AgeControlSystem()
    try:
        system.start()
    except KeyboardInterrupt:
        print("\n[INFO] Прерывание пользователем (Ctrl+C)")
        system.stop()
    except Exception as e:
        print(f"[ERROR] Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        system.stop()

if __name__ == "__main__":
    main()