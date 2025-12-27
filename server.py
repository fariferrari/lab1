import socket
import json

# Функция, которую будем вызывать удаленно
def add(a, b):
    return a + b

def start_server():
    # Создаем TCP сокет [cite: 99]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Слушаем на порту 5000 [cite: 49]
    server.bind(('0.0.0.0', 5000))
    server.listen(1)
    print("RPC Сервер запущен и ждет подключений на порту 5000...")

    while True:
        conn, addr = server.accept()
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data: continue

            # Декодирование (Unmarshalling) [cite: 9, 76]
            request = json.loads(data)
            print(f"Получен запрос ID {request['request_id']}: {request['method']}({request['params']})")

            # Выполнение функции [cite: 77]
            res = add(request['params']['a'], request['params']['b'])

            # Формирование ответа по структуре из задания [cite: 78, 80]
            response = {
                "request_id": request['request_id'],
                "result": res,
                "status": "OK"
            }
            conn.send(json.dumps(response).encode('utf-8'))
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()