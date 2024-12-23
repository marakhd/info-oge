class NumOne:
    @staticmethod
    def calculate_size_page_kb(pages, lines_per_page, chars_per_line, bits_per_char):
        """
        Функция для вычисления объема информации в Кбайтах.

        :param pages: количество страниц
        :param lines_per_page: количество строк на каждой странице
        :param chars_per_line: количество символов в каждой строке
        :param bits_per_char: количество бит на символ (в зависимости от кодировки)
        :return: объем информации в Кбайтах
        """
        # Общее количество символов
        total_chars = pages * lines_per_page * chars_per_line
        
        # Объем в байтах (бит на символ разделить на 8 для перевода в байты)
        total_bytes = total_chars * (bits_per_char / 8)
        
        # Переводим в Кбайты
        total_kb = total_bytes / 1024
        
        print(total_kb)

    @staticmethod
    def find_removed_word(text_before, removed_bytes, encoding_bits):
        """
        Функция для нахождения вычеркнутого слова на основе разницы в байтах.

        :param text_before: текст до изменений
        :param removed_bytes: количество байт, на которые уменьшился текст
        :param encoding_bits: количество бит на символ (например, для UTF-32 это 32)
        :return: вычеркнутое слово
        """
        # Количество байт на один символ
        bytes_per_char = encoding_bits / 8
        
        # Пробуем удалить каждое слово и вычислить разницу
        words_before = text_before.split(", ")

        for word in words_before:
            # Проверяем, если разница в байтах соответствует удалённым байтам
            if (len(word.replace("­", "")) * bytes_per_char) - (removed_bytes - 2)  == 0:
                print(word.replace("­", ""))
                return word.replace("­", "")
