class Counter:
  def __init__(self):
    self._counter = 0

  def increment(self):
    self._counter += 1

  def reset(self):
    self._counter = 0

  def value(self):
    return self._counter
