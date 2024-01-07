from stressState import *
# import stressState

# Create and instance of the class and get principal stresses
stress_State = StressState(100, 20, 30)
print("Principal Stresses:", stress_State.principalStresses)