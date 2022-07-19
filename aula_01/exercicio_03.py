# height_in and weight_lb are available as regular lists

height_in = [3, 5, 7, 8, 10]

weight_lb = [100, 120, 111, 90, 150]

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_lb = np.array(weight_lb)
np_weight_kg = np_weight_lb * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)


