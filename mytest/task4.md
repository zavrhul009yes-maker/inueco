# Задание: Тестирование функции analyze_text_statistics

## Описание задачи

Вам необходимо создать файл `test_complex_func.py` с тестами для функции `analyze_text_statistics` используя библиотеку pytest.

## Требования

Создайте минимум **10 тестов**, которые проверяют различные аспекты работы функции:

### 1. Базовые тесты (обязательные)

#### test_basic_text_analysis
- Проверьте анализ простого текста: "Hello world! Python is great."
- Убедитесь, что `total_words` больше 0
- Проверьте, что `total_sentences` равно 2
- Убедитесь, что `longest_word` не None

#### test_empty_text_raises_error
- Проверьте, что пустая строка "" вызывает ValueError
- Используйте `pytest.raises(ValueError)`

#### test_whitespace_only_raises_error
- Проверьте, что строка только с пробелами "   " вызывает ValueError

#### test_invalid_type_raises_error
- Проверьте, что передача числа (123) вместо строки вызывает TypeError
- Также проверьте для списка ["test"]

### 2. Тесты подсчета слов и символов

#### test_word_count
- Текст: "One two three four five"
- Проверьте, что `total_words` == 5

#### test_character_count
- Текст: "Hello"
- Проверьте, что `total_characters` == 5

#### test_sentence_count
- Текст: "First! Second? Third."
- Проверьте, что `total_sentences` == 3

### 3. Тесты поиска слов

#### test_longest_and_shortest_word
- Текст: "I am programming in Python language"
- Проверьте, что `longest_word` == "programming"
- Проверьте, что `shortest_word` == "i"

### 4. Тесты частоты слов

#### test_word_frequency_with_min_length
- Текст: "cat dog cat bird cat dog"
- min_word_length = 3
- Проверьте, что в `word_frequency` есть 'cat' с count = 3
- Проверьте, что в `word_frequency` есть 'dog' с count = 2
- Проверьте, что 'cat' в `top_3_words`

#### test_top_3_words
- Текст: "apple banana apple cherry apple banana cherry cherry cherry"
- Проверьте, что первое слово в `top_3_words` это 'cherry' с count = 4
- Проверьте, что второе слово это 'apple' с count = 3
- Проверьте длину `top_3_words` == 3

### 5. Дополнительные тесты

#### test_unique_words_percentage
- Текст: "test test test unique"
- Проверьте, что `unique_words_count` == 2
- Проверьте, что `unique_words_percentage` == 50.0

#### test_average_word_length
- Текст: "ab abc abcd"
- Проверьте, что `average_word_length` примерно равна 3.0 (используйте округление)

#### test_text_with_punctuation
- Текст: "Hello, world! How are you?"
- Проверьте, что функция корректно обрабатывает знаки препинания
- Убедитесь, что `total_words` == 5

#### test_text_without_valid_words
- Текст: "!!! ??? ..."
- Проверьте, что `total_words` == 0
- Проверьте, что `longest_word` == None

#### test_custom_min_word_length
- Текст: "I am ok but you are great"
- min_word_length = 4
- Проверьте, что в `word_frequency` нет слов короче 4 символов
- Убедитесь, что 'great' присутствует в word_frequency

## Структура файла test_complex_func.py

```python
import pytest
from complex_func import analyze_text_statistics

def test_basic_text_analysis():
    # Ваш код здесь
    pass

def test_empty_text_raises_error():
    # Ваш код здесь
    pass

# ... остальные тесты
```

## Как запустить тесты

```bash
pytest test_complex_func.py -v
```

## Критерии оценки

- ✅ Все 10+ тестов написаны
- ✅ Используются assert для проверок
- ✅ Тесты покрывают разные сценарии (валидные данные, ошибки, граничные случаи)
- ✅ Используется pytest.raises для проверки исключений
- ✅ Тесты имеют понятные названия
- ✅ Все тесты проходят успешно

## Подсказки

1. Импортируйте pytest: `import pytest`
2. Для проверки исключений используйте:
   ```python
   with pytest.raises(ValueError):
       analyze_text_statistics("")
   ```
3. Для проверки примерного равенства float используйте:
   ```python
   assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)
   ```
4. Не забудьте проверить структуру возвращаемого словаря
5. Проверяйте как успешные сценарии, так и ошибочные

Удачи в тестировании! 🚀