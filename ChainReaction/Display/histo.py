from matplotlib import pyplot as plt

def print_hist(node_list):
  list1 = node_list
  plt.hist(list1, 10)#10 is the number of bins
  plt.show()
