### Hexlet tests and linter status:
[![Python CI](https://github.com/dr-Panakhov/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/dr-Panakhov/python-project-50/actions/workflows/python-ci.yml)
[![hexlet-check](https://github.com/dr-Panakhov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dr-Panakhov/python-project-50/actions/workflows/hexlet-check.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dr-Panakhov_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=dr-Panakhov_python-project-50)
[![Test Coverage](https://sonarcloud.io/api/project_badges/measure?project=dr-Panakhov_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=dr-Panakhov_python-project-50)

---

# Gendiff / Вычислитель отличий

CLI-утилита, определяющая разницу между двумя структурами данных (конфигурационными файлами). Программа находит измененные, добавленные и удаленные ключи, работая в том числе с глубоко вложенными древовидными структурами. Разработана в рамках обучения на платформе Hexlet.

## Возможности:
*   **Мультиформатность:** Поддержка входных данных в форматах JSON и YAML/YML.
*   **Гибкий вывод:** Генерация отчетов в трех форматах: `stylish` (человекочитаемый вид), `plain` (плоский текст для логов) и `json`.
*   **Интерфейс командной строки:** Удобный CLI, реализованный через стандартный модуль `argparse`.

## Стек технологий и инженерные практики:
*   **Language:** Python 3.x
*   **Testing:** Автоматизированное тестирование на базе `pytest` с применением методологии TDD (Test-Driven Development).
*   **Алгоритмы:** Работа с вложенными структурами данных с помощью древовидной рекурсии.
*   **Project Manager:** `uv`
*   **Linter:** `ruff`

## Демонстрация работы (Asciinema):
*   **Демонстрация 1:** [![asciicast](https://asciinema.org/a/UAUdcS3VpgfBHL4S.svg)](https://asciinema.org/a/UAUdcS3VpgfBHL4S)
*   **Демонстрация 2:** [![asciicast](https://asciinema.org/a/tkaqAhFaBdJDAtzo.svg)](https://asciinema.org/a/tkaqAhFaBdJDAtzo)
*   **Демонстрация 3:** [![asciicast](https://asciinema.org/a/MEbhugHVJ69SIbpZ.svg)](https://asciinema.org/a/MEbhugHVJ69SIbpZ)
*   **Демонстрация 4:** [![asciicast](https://asciinema.org/a/6EbWKa5or0nLPav.svg)](https://asciinema.org/a/6EbWKa5or0nLPav)
*   **Демонстрация 5:** [![asciicast](https://asciinema.org/a/pR8V102DqHY80u5J.svg)](https://asciinema.org/a/pR8V102DqHY80u5J)

## Установка и запуск

Для работы проекта необходим установленный менеджер пакетов `uv`.

```bash
# Клонировать репозиторий
git clone [https://github.com/dr-Panakhov/python-project-50.git](https://github.com/dr-Panakhov/python-project-50.git)

# Перейти в директорию проекта
cd python-project-50

# Установить зависимости
uv sync
