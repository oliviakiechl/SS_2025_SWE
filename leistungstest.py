from datetime import date
import numpy as np


def Test(first_experiment_id: int):

    try:
        first_experiment_id = int(first_experiment_id)
    except ValueError:
        print("Error: first_experiment_id muss eine ganze Zahl sein")
        return[]

    #Liste
    experiments = []

    #Dictionary
    for i in range(10):
        einträge = {
            "id" : first_experiment_id + i,  
            "name" : "Olivia Kiechl",
            "date" : date.today()
        }
        experiments.append(einträge)           
        
 
    #For - Schleife für die 5 Experimente
    for einträge in experiments[:5]:
        print(einträge)

    # Even or odd
    even_id = 0

    for einträge in experiments:
        if einträge["id"] % 2 == 0:
            even_id += 1
            print("even_id: ", even_id)
        else:
            print("first_experiment_id is odd")

print(Test(1000))
