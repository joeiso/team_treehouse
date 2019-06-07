import numpy as np 
np.__version__

gpas_as_list = [4.0, 3.286, 3.5]

#can have elements appended to it
gpas_as_list.append(4.0)
#can have multiple datatypes in it.
gpas_as_list.insert(1, "whatevs")
gpas_as_list.pop(1)
gpas_as_list

gpas = np.array(gpas_as_list)

study_minutes = np.zeros(100, np.uint16)
study_minutes

#%whos
study_minutes[0] = 150
first_day_minutes = study_minutes[0]

study_minutes[1] = 60
study_minutes[2:6] = [80, 60, 30, 90]
print("{}".format(study_minutes))

students_gpas = np.array([
    [4.0, 3.286, 3.5, 4.0], 
    [3.2, 3.8, 4.0, 4.0], 
    [3.96, 3.92, 4.0, 3.6]
    ], np.float16)
print("{}", format(students_gpas))

students_gpas.ndim

students_gpas.shape

students_gpas.size
print("{}".format(np.info(students_gpas)))
print("{}".format(students_gpas[1][2]))