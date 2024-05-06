class Counter:
  def __init__(self):
    self.counter = 0

  def increment(self):
    self.counter += 1

  def reset(self):
    self.counter = 0

  def value(self):
    return self.counter
