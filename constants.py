from math import pi

# pygame константи
FREQUENCY = 60
SAMPLE_TIME = 1/FREQUENCY
WINDOW_HEIGHT = 720
WINDOW_LENGTH = 1280
M2PIX = 1000
BLACK = 0, 0, 0
DARK_GRAY = 96, 96, 96
LIGHT_GRAY = 216, 216, 216
RED = 255, 0, 0
PIX_BORDER_GAP = 10
PIX_TAB_GAP = round(WINDOW_LENGTH*0.2)

# Конвертація одиниць виміру
KILO2GRAM = 1000.0
METRE2CENTI = 100.0
DRAG_B_SI2CGS = 10000000.0
RADIAN2DEGREES = 180.0/pi

# Фізичні межі та дельти
MAX_GRAVITY = 15 # м/с^2
MIN_GRAVITY = 0 # м/с^2
MAX_DRAG = 0.001 # N м / (1/с)^2
MIN_DRAG = 0.0 # N м / (1/с)^2
MAX_MASS = 0.100 # кг
MIN_MASS = 0.001 # кг
MAX_LENGTH = 0.50 # м
MIN_LENGTH = 0.01 # м
MAX_WIDTH = 0.50 # м
MIN_WIDTH = 0.001 # м
MAX_PIVOT_RATIO = 0.50
MIN_PIVOT_RATIO = 0.00
MAX_AMPLITUDE = pi # рад
MIN_AMPLITUDE = -pi # рад
DELTA = [0.05, 0.000001, 0.0005, 0.005, 0.0005, 0.005, 1.0/RADIAN2DEGREES] # сила тяжіння, опір, маса, довжина, ширина, поворот, амплітуда
