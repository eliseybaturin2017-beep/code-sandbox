# импорт
import Cube_Animator
# координаты
Cube_Animator.left = 73
Cube_Animator.top = 73
Cube_Animator.x = 10
Cube_Animator.y = 10
# создание куба
Cube_Animator.cube('.') # или Cube_Animator.cube(10, 10, 73, 73, '.')

# анимации для них создание куба необязательно потому что он и так создается
# Cube_Animator.animatePulseZoomV1(2) в версии один всегда можно указать сколько раз повторить
# Cube_Animator.animatePulseZoomV2() отличия версии два то что туда не нужно указывать 
# сколько раз повторить он создан для того чтобы повторять анимацию бесконечно но чтобы он повторялся 
# бесконечно нужно указать бесконечный цикл
# Cube_Animator.animateLeft() сдвиг влево
# Cube_Animator.animateRight() сдвиг вправо
# Cube_Animator.animateTop() сдвиг вниз
# Cube_Animator.animateUp() сдвиг вверх
