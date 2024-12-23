import g4f

def gpt(message: str):
    # Включение логирования
    g4f.logging = True

    # Создание сообщения
    response = g4f.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
