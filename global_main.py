from PrimeSearcher import PrimeSearcher
from hybrid import gen_key

class global_mainclass:
  def __init__(self,img):
    self.generated_keys = gen_key(img)
    print(self.generated_keys)

x = global_mainclass('/images/onez.jpg')