import numpy as np

# Define the StressState class
class StressState:

    def __init__(self, sxx, syy, sxy):
        self.stressTensor = np.array([
            [sxx, sxy],
            [sxy, syy],
            ])

    @property
    def principalStresses(self):
        # Calculate and return principal stress values
        eigenValues = np.linalg.eig(self.stressTensor)
        return np.sort(eigenValues[0])[::-1]

    @property
    def center(self):
        return (self.stressTensor[0,0] + self.stressTensor[1,1]) / 2


    @property
    def radius(self):
        return (self.principalStresses[0] - self.principalStresses[1]) / 2