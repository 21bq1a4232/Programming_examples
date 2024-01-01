def water_jug_problem():
    jug_4 = 0
    jug_3 = 0
    jug_3 = 3
    jug_4 = jug_3
    jug_3 = jug_3 - jug_4
    jug_4 = 0
    jug_4 = jug_3
    jug_3 = 0
    jug_3 = 3
    jug_4 = jug_3
    jug_3 = jug_3 - (4 - jug_4)
    jug_4 = jug_3
    return jug_4
result = water_jug_problem()
print("The 4-gallon jug has", result, "gallons of water.")