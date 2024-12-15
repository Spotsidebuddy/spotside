import math
import turtle

i = 0  #это счетчик, то есть оно выступает одновременно
        #как параметрр времени в уравнении
width_qf = float(3.2)  # the bigger - the wider, try playing with it

for i in range(2000):
    vt = i #это расстояние пройденное за время i = время умноженное на скорость
                #то естьб если спираль разогнуть - именно столько в пикселях
                #типо пройдет "стилус"
    x = vt * width_qf * math.cos(vt) #синус и косинус - это то что "крутит"
    y = vt * width_qf * math.sin(vt) #но изза увеличения vt еще и удаляется от точки оборота
    turtle.goto(x, y)
