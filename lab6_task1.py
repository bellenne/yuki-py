#⦁	Создайте запись для хранения информации о круге, в которой хранить радиус и координаты центра – при этом координаты центра – это тоже структура содержащее поле x и y.
class PointCoords:
    def __init__( self, x:int, y:int ):
        self.x = x
        self.y = y
class Circle:
    def __init__(self, radius:int, circleCenter:PointCoords):
        self.radius = radius
        self.circleCenter = circleCenter

#⦁	Создайте запись для хранения информации о прямоугольнике, в которой хранить целочисленные координаты левого верхнего и правого нижнего углов
class PointCoords:
    def __init__( self, x:int, y:int ):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, leftUpPointCoords:PointCoords, rightDownPointCoords:PointCoords):
        self.leftUpPointCoords = leftUpPointCoords
        self.rightDownPointCoords = rightDownPointCoords

#⦁	Создайте запись для хранения информации о простых дробях, в которой хранить числитель, знаменатель – это пара целых чисел
class Decimal:
    def __init__(self, numerator:int, denumerator:int):
        self.numerator = numerator
        self.denumerator = denumerator

#Создать запись позволяющую хранить всю информацию необходимую для построения приведенного изображения из примитивов:  эллипс, прямоугольник. Вариант 2
class PointCoords:
    def __init__( self, x:int, y:int ):
        self.x = x
        self.y = y
class Rectange:
    def __init__(self, leftUpPoint:PointCoords, rightDownPoint:PointCoords):
        self.leftUpPoint = leftUpPoint
        self.rightDownPoint = rightDownPoint
class Elipse:
    def __init__(self, center:PointCoords, Rx:int, Ry:int):
        self.center = center
        self.Rx = Rx
        self.Ry = Ry
class Circle:
    def __init__(self, center:PointCoords, radius:int):
        self.center = center
        self.radius = radius

class Eye:
    def __init__(self, eye:Circle, eyeball:Circle):
        self.eye = eye
        self.eyeball = eyeball

class Mouth:
    def __init__(self, mouth:Rectange=[7]):
        self.mouth = mouth

class Character:
    def __init__(self, head:Rectange, leftEye:Eye, rightEye:Eye, nose:Elipse, mouth:Mouth):        
        self.head = head
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.nose = nose       
        self.mouth = mouth       