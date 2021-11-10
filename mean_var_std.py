import numpy as np

def calculate(list):
  """
  list (input, list): List of 9 integers to be transformed into a 3x3 Numpy matrix and used for the calculations.

  calculations (output, dictionary): contains the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in the matrix.
  """
  # Raise value error if list does not contain exactly 9 variables
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  
  # Transform input list into 3 x 3 matrix
  arr = np.array([list[:3], list[3:6], list[6:]])

  # Dictionary of calculations
  calculations = {
    'mean': [np.mean(arr, axis = 0).tolist(), np.mean(arr, axis = 1).tolist(), np.mean(arr).tolist()],
    'variance': [np.var(arr, axis = 0).tolist(), np.var(arr, axis = 1).tolist(), np.var(arr).tolist()],
    'standard deviation': [np.std(arr, axis = 0).tolist(), np.std(arr, axis = 1).tolist(), np.std(arr).tolist()],
    'max': [np.max(arr, axis = 0).tolist(), np.max(arr, axis = 1).tolist(), np.max(arr).tolist()],
    'min': [np.min(arr, axis = 0).tolist(), np.min(arr, axis = 1).tolist(), np.min(arr).tolist()],
    'sum': [np.sum(arr, axis = 0).tolist(), np.sum(arr, axis = 1).tolist(), np.sum(arr).tolist()]
  }

  return calculations