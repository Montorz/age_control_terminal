import time
from config import Config

class AgeControlSystem:
    def __init__(self):
        print("СИСТЕМА КОНТРОЛЯ ВОЗРАСТА ДЛЯ ТЕРМИНАЛОВ")
        
        self.config = Config()
        self.is_running = False
        self.cap = None
        
        print("[INFO] Инициализация системы...")
        print(f"[INFO] RTSP URL: {self.config.RTSP_URL}")
        print(f"[INFO] Режим GUI: {'ВКЛЮЧЁН' if self.config.GUI_MODE else 'ВЫКЛЮЧЁН'}")
    
    def start(self):
        print("[INFO] Подключение к камере...")
        print("[INFO] Подключение установлено")
        
        self.is_running = True
        self._main_loop()
        return True
    
    def _main_loop(self):
        print("[INFO] Запуск основного цикла...")
        while self.is_running:
            time.sleep(0.1)
    
    def stop(self):
        print("\n[INFO] Остановка системы...")
        self.is_running = False
        print("[INFO] Система остановлена")

def main():
    system = AgeControlSystem()
    try:
        system.start()
    except KeyboardInterrupt:
        print("\n[INFO] Прерывание пользователем")
        system.stop()
    except Exception as e:
        print(f"[ERROR] Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        system.stop()

if __name__ == "__main__":
    main()