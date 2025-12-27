import socket
import json
import uuid
import time

# ЗАМЕНИТЕ ЭТОТ IP НА IP ВАШЕГО СЕРВЕРА
SERVER_IP = "98.92.45.7" 
PORT = 5000

def call_rpc(a, b):
    # Создаем структуру запроса (Marshalling) [cite: 9, 61, 68]
    request = {
        "request_id": str(uuid.uuid4()), # Уникальный ID [cite: 63]
        "method": "add",
        "params": {"a": a, "b": b}
    }

    # Повторные попытки (Retry logic - Task 3) [cite: 87, 109]
    for attempt in range(3):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0) # Таймаут 2 секунды [cite: 85]
            
            print(f"Попытка {attempt+1}: Отправка запроса на сервер...")
            s.connect((SERVER_IP, PORT))
            s.send(json.dumps(request).encode('utf-8'))
            
            response = json.loads(s.recv(1024).decode('utf-8'))
            print(f"Успех! Результат: {response['result']} (ID: {response['request_id']})")
            s.close()
            return
        except Exception as e:
            print(f"Ошибка/Таймаут на попытке {attempt+1}: {e}")
            time.sleep(1)
    
    print("Сервер не ответил после 3 попыток.")

if __name__ == "__main__":
    call_rpc(5, 7) # Пример вызова [cite: 72]