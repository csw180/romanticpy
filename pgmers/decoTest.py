from functools import wraps

def startMsg(func) :

  @wraps(func)
  def wrapper(*args, **kargs) :
      print(f'{func.__name__} start')
      value = func(*args, **kargs)
      return value
    
  return wrapper

@startMsg
def plusone(num) :
  return num+1

print(plusone(1))
print(plusone.__name__)