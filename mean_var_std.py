import numpy as np

def calculate(list):
   

   if (len(list) != 9):
     raise ValueError("List must contain nine numbers.")
  
   L=np.array(list)


   mean_rows=[L[[0,1,2]].mean(), L[[3,4,5]].mean(), L[[6,7,8]].mean()]
   mean_columns=[L[[0,3,6]].mean(), L[[1,4,7]].mean(), L[[2,5,8]].mean()]
   var_rows=[L[[0,1,2]].var(), L[[3,4,5]].var(), L[[6,7,8]].var()]
   var_columns=[L[[0,3,6]].var(), L[[1,4,7]].var(), L[[2,5,8]].var()]
   std_rows=[L[[0,1,2]].std(), L[[3,4,5]].std(), L[[6,7,8]].std()]
   std_columns=[L[[0,3,6]].std(), L[[1,4,7]].std(), L[[2,5,8]].std()]
   max_rows=[L[[0,1,2]].max(), L[[3,4,5]].max(), L[[6,7,8]].max()]
   max_columns=[L[[0,3,6]].max(), L[[1,4,7]].max(), L[[2,5,8]].max()]
   min_rows=[L[[0,1,2]].min(), L[[3,4,5]].min(), L[[6,7,8]].min()]
   min_columns=[L[[0,3,6]].min(), L[[1,4,7]].min(), L[[2,5,8]].min()]
   sum_rows=[L[[0,1,2]].sum(), L[[3,4,5]].sum(), L[[6,7,8]].sum()]
   sum_columns=[L[[0,3,6]].sum(), L[[1,4,7]].sum(), L[[2,5,8]].sum()]

   return {
  'mean': [mean_columns, mean_rows, L.mean()],
  'variance': [var_columns, var_rows, L.var()],
  'standard deviation': [std_columns, std_rows, L.std()],
  'max': [max_columns, max_rows, L.max()],
  'min': [min_columns, min_rows, L.min()],
  'sum': [sum_columns, sum_rows, L.sum()]
    }