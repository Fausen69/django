# В папке templates/ хранятся HTML-шаблоны для всех приложений:
"templates/about/description.html"
"templates/homepage/index.html"
"templates/ice_cream/detail.html"
"templates/ice_cream/list.html"

# В перечисленных шаблонах есть повторяющиеся фрагменты кода.
# Это непрактично, нарушает принцип DRY и усложняет работу с проектом.
# Сделайте проект лучше: создайте базовый шаблон и шаблоны для шапки и подвала;
# подключите шапку и подвал к базовому шаблону; вынесите в эти шаблоны повторяющийся код.
# Создайте шаблоны:
"templates/includes/header.html,"
"templates/includes/footer.html"
"templates/base.html,"

# Содержимое тега <header> перенесите в файл header.html, содержимое тега <footer> — в файл footer.html. 
# Подключите файлы header.html и footer.html к шаблону base.html.
# В файл base.html вставьте два тега {% block %}:
# тег {% block %} с именем title — для содержимого HTML-тега <title>,
# тег {% block %} с именем content — для основного содержимого страницы.
# Шаблоны description.html, index.html, detail.html и list.html должны РАСШИРЯТЬ шаблон base.html;
# в этих же шаблонах должно храниться содержимое для блоков title и content.



# Подсказки
#  - Для работы потребуются теги extends, include и block.
#  - Создайте базовый шаблон base.html и сохраните его в корне папки templates/.
# Вынесите в него код, повторяющийся во всех шаблонах.
