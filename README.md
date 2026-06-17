# Cube Animator — проект для анимации кубов и создание кубов в терминале

кубы создаются послойно можно создать так и функцию для анимации и использовать встроенные функции. функция _clear_terminal используется для очищение всего терминала также её используют для покадровой анимации. Для каждого движения своей анимации используйте цикл 'for' или 'while'. вот пример анимации:
'def animateUp(posishon=-1):

    cube_animator_module._clear_terminal()
    
    cube_animator_module.top += posishon
    
    cube(cube_animator_module.x, cube_animator_module.y, cube_animator_module.left, cube_animator_module.top, '.')
    
    time.sleep(0.2)
    
    cube_animator_module._clear_terminal()'
    здесь нужно использовать и другие модули. cube_animator_module._clear_terminal() можно сократить с помощью 'as ca' ca необязателен можно по-другому называть. А если хотите скачать файл чтобы использовать в импорт то используете команду pip install git+https://github.com/eliseybaturin2017-beep/my_repository1.git
Test_Import_File файл наглядный пример кода.
Если файл Cube Animator находится в отдельной папке я советую вытащить её из папки если вы её используете в другом файле или просто засунуть файл в котором вы используете его в папку которой вы храните этот файл.
