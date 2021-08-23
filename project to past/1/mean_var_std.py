import numpy as np

def calculate(list):
  if len(list) < 9:
      raise ValueError('List must contain nine numbers.')
  np_list = np.array([list[0:3],list[3:6],list[6:10]])
  ar = np.array(list).reshape((3,3))
  print(np_list)
  calculations = dict()
  calculations['mean'] = [np_list.mean(axis=0).tolist(), np_list.mean(axis=1).tolist(), np_list.mean()]
  calculations['sum'] = [np_list.sum(axis=0).tolist(), np_list.sum(axis=1).tolist(), np_list.sum()]
  calculations['max'] = [np_list.max(axis=0).tolist(), np_list.max(axis=1).tolist(), np_list.max()]
  calculations['min'] = [np_list.min(axis=0).tolist(), np_list.min(axis=1).tolist(), np_list.min()]
  calculations['variance'] = [np_list.var(axis=0).tolist(), np_list.var(axis=1).tolist(), np_list.var()]
  calculations['standard deviation'] = [np_list.std(axis=0).tolist(), np_list.std(axis=1).tolist(), np_list.std()]
  return calculations