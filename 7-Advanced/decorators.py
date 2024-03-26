import time;


def time_this(func):
  def wrapper(*args, **kwargs):
    t0 = time.time()
    func(*args, **kwargs)
    t1 = time.time()-t0
    print(f"{func} took {t1} seconds")
  return wrapper


@time_this
def linear_search(list1d, item):
  indexes = []
  for i,elem in enumerate(list1d):
    if(elem == item):
      indexes.append(i)

  return indexes
    

list1d = [chr(x) for x in range(65,91)]

linear_search(list1d,"z")






