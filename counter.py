class Counter:
  def __init__(self):
    self.__counter = 0

  def increment(self):
    self.__counter += 1

  def reset(self):
    self.__counter = 0

  def value(self):
    return self.__counter
