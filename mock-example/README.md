# Пример мок-сервиса для habr статьи

## Запуск
```bash 
  python -m main
```

**Адрес Swagger: http://0.0.0.0:8000/docs**

## Модули
- mock-example/app/api/business - модуль с мок-ручками 
- mock-example/app/api/support - модуль для управлени моком из тестов
- mock-example/app/pkg/tables - сделано вместо базы данных/клика/etc, реализованная через ин-мемори словарь, сделано для нативности примера с хранилищем