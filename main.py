from counter import Counter

if __name__ == "__main__":
  # Python encapsulation example

  counter = Counter()
  counter.increment()
  counter.increment()
  counter.increment()

  print(counter.value())

  counter.counter = -999
  print(counter.value())
