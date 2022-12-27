def load_logins():
    logins = dict()
    with open('logins.txt') as logins_file:
        for line in logins_file:
            line = line.strip()
            # Проверяем, что строка не пустая
            if line:
                # Сначала разбиваем на части по точке с запятой
                login, password = line.split(';')
                # Потом каждую часть разбиваем по двоеточию и берем правую часть
                # (левую не учитываем, считаем что в строке всегда сначала логин, потом пароль)
                login = login.split(':')[1]
                password = password.split(':')[1]
                # Добавляем пару логин-пароль в словарь
                logins[login] = password

    return logins


logins = load_logins()

login = input("login: ")
password = input("password: ")

if login in logins and logins[login] == password:
    print("Вы успешно вошли в систему.")
else:
    print("Неверный логин или пароль.")
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.connect(('localhost', 55000))  # подключемся к серверному сокету

    sock.send(bytes('Hello, world', encoding='UTF-8'))  # отправляем сообщение
    data = sock.recv(1024)  # читаем ответ от серверного сокета
    sock.close()  # закрываем соединение
    print(data)