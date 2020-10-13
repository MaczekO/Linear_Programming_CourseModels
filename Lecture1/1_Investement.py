from amplpy import AMPL, Environment
import os
experiment_name = "investement"
lecture_nr = 1

ampl = AMPL(Environment('C:\\Users\\cmata\\Desktop\\Linear Programming\\ampl.mswin64'))
ampl.read(os.path.join(os.getcwd(),'Lecture'+str(lecture_nr), experiment_name + '.mod'))
ampl.readData(os.path.join(os.getcwd(),'Lecture'+str(lecture_nr), experiment_name + '.dat'))
ampl.solve()


totalcost = ampl.getObjective('Total_gain')
print("Objective is:", totalcost.value())
x = ampl.getVariable('x')
x = x.getValues()
y = ampl.getVariable('y')
y = y.getValues()
print(x, y)