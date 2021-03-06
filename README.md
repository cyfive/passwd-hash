# Скрипт для помощи в генерации хешированного пароля 
## Зависимости
Скрипт на bash использует для генерации хешированного пароля `openssl > 1.1`, поэтому соответствующий пакет должен бфть установлен и команда `openssl` должна быть доступна в `PATH`.
Скрипт на Python требует установленой версии `Python > 3`.

## Ограничения Python версии
* Игнорируется переменая окружения `SALT_LENGTH`, т.к. в модуле `crypt` всегда используется максимальная длинна соли для выбранного типа шифрования.
* `DEBUG > 1` имеет такое же поведение, как и `DEBUG = 1`, это обусловлено тем, что нет смысла выводить скрипт на экран, для его отладки лучше использовать какой нибудь отладчик.

## Настройки
Настройки производятся через установку переменных окружения перед запуском скрипта. Для установки доступны следующие переменные:

`DEBUG` - вывод отладочной информации, значение по умолчанию `0`, может принимать значения `1` - вывод значений переменных, `2` - трассировка выполнения скрипта.

`SALT_LENGTH` - длинна соли, значение по умолчанию `16`.

`CIPHER` - тип хеш функции, может принимать следующие значения `1` - MD5, `5` - SHA256, `6` - SHA512 (значение по умолчанию).

Все значения по умолчанию используются как в CentOS при хешировании пароля и при обычной эксплуатации не требуют изменений.

## Примеры запуска
### Обычный запуск скрипта
```
[semets@pc-emets passwd-hash]$ ./gen_passwd.sh 
Password: 
$6$hRGmGhbBXYu2H4ai$SeKOVSwvmJbWG2diymXsxOg6A9nNty82G/Je5m9rNzNrBJ5aeapfWkocbQLZ2AEnBpl80i7yIy/3Yi2RcZ.y21
[semets@pc-emets passwd-hash]$ 
```
### Запуск с отладкой, уровень 1
```
[semets@pc-emets passwd-hash]$ export DEBUG=1; ./gen_passwd.sh 
Salt lenght: 16
Chipher: -6
Random salt: 9k6FyocAgAY5Wg55
Password: 
$6$9k6FyocAgAY5Wg55$cdTJ9JE5NzwYQ83MJN/BypaupvHDl6.LJycXM4YGMb6mV6aTSAjuruJ/8ANiaSYdRWdpYnyvi8d2lwVpBuClc1
[semets@pc-emets passwd-hash]$
```
## Генерация MD5 хеша
```
[semets@pc-emets passwd-hash]$ export CIPHER=1; ./gen_passwd.sh 
Password: 
$1$K7g9yn3f$gdbDSeEukuHStvnfeCsrl/
[semets@pc-emets passwd-hash]$ 
```
