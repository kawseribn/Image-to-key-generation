from PrimeSearcher import PrimeSearcher

###
class Main_class:
  def __init__(self,image):
    ps = PrimeSearcher(image)
    ps.rescale(17*18, fit_to_original=True)
    x=ps.search(max_iterations=1000, noise_count=1, break_on_find=True)
    self.prime_numbers = x

 


