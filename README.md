# image-to-key-generation

Image to key generation from prime numbers

<!-- Read Article: [https://cankut.github.io/posts/2020-05-12-image-to-prime.html](https://cankut.github.io/posts/2020-05-12-image-to-prime.html) -->

## usage
- use `main.py` to search for prime numbers (Searching time will depend on the resolution of the image)
- use `json_to_image.py` to generate 1:1 size image of the number
- use `json_to_ann.py` to generate zoomed and annotated image of the number
- use `global_main.py` to generate the public and private key from the prime number

```python
# SEARCH FOR PRIME
from PrimeSearcher import PrimeSearcher

ps = PrimeSearcher("./images/onez.jpg")
ps.rescale(17*18, fit_to_original=True)
ps.search(max_iterations=1000, noise_count=1, break_on_find=False)
```

```python
# GENERATE ANNOTATED IMAGE OF PRIME
import Utils, os, numpy as np
from PIL import Image


imgFile = "results/onez/65x63/clustered.png"

num, colors, size = Utils.load_from_file(jsonFile)
f = Utils.plot_number(num, colors, size, True, True)
f.savefig(imgFile, bbox_inches='tight')
```
---

### Input
![onez](images/onez.jpg)

<!-- ![Euler](results/euler/54x66/ann_prime_2020-05-11%20213910.json.png) -->

### Resulting Prime Number
```json
{
    "number": 2037111551117730886711559995551138831155999995551748615559999955117603715599999955176033711599995160000660000061570446603336637775717771631555951717155510315555517111555146715599171175551483715557315377734463733733336666644063333771733760044063777117736486444006377333042236044400633364849,
}
```
### Generated Public & Private Key
    "Public key": (0x7516f8c8bd5c1b68f9834ff8dfbcd6eafe51ca9d348ae5b73472824a75da2ffa83237356f9060900b980459891a2f2b961560a86f4481908efcf53ea2dd0e7959249315331d095a5935ca5c3a58c29df7804db9e033cc105f96a8615970a0209b41ed1b96e9b7c20f0c0f914569da2ad63c83beec6fe0d18b355faed72dad319e3ee0caf4281b9e507c407554e502b8131ed4587195ef109f5bab715f1599f127174b3681528baaa2381cbcaa3460798dd1ec89a3c93bd2446a00cbd58158e9956ddf733bbfd4a47d530f6d294090ab594a513fa6c2a0d2e49fe6f290842606ee7ebfda5a1a813fb8981f99005df647,
    0xb2fa2ed02609778319a6f275585e0371fecb1b03cfc8dbbfe810bb685817c260b3a1fd47ecb300662a8f84409722336bc55bd12da17b5bf3573b0eaee5550e1e18b4be54b1ab95ced484247443c38da70889d11b006722edd2d9c3c8bbccdadc785b88d3699f69982325b5e2d82c75f89d0041a38fb331c454bbfe20a2c9eba49d43a154851cfc1c62f933eb5158f109ee5179d928d7b10f29b036204c7d4e4f6ba25f6f15e694eba53825908096ee23610dbd7b52db2434afd12a4764573d0ba237bb7aeab6250282659a6078fcc4c0418a4c93a4fd5cc835b9097ed180d62a981e4e240a279ec65af38e61f258865)
    "Private Key": (0x525efd9affc871748e55a04a4ea36709de43586f29f57df49df6acfc772691fee9f5e13b13724582dce6b9fd62d704a2aba7152e0266be3283e4d0e733dc221d76fed76ce18d70fa077666ad025411b528f234af2b1e6f3bab9659323ba50814a123d73c25818a47e3a782a0bf852d247f3a4dbcf42079f6669e9d2147c53d83fadd1226a51e766ac065b8fdaa45603baa3542febbd543135a51bc71fd80b9ee480761dabd5d513a8a4d654561cfb220d5751323eacd35ad25b6a44632648574ae123b194fc42d35b269b1b7cd8c2ef06b756a5b95e0f66105ca90553076cc14eecd3ba1f061cd889d4a32d92182a5b,
    0xb2fa2ed02609778319a6f275585e0371fecb1b03cfc8dbbfe810bb685817c260b3a1fd47ecb300662a8f84409722336bc55bd12da17b5bf3573b0eaee5550e1e18b4be54b1ab95ced484247443c38da70889d11b006722edd2d9c3c8bbccdadc785b88d3699f69982325b5e2d82c75f89d0041a38fb331c454bbfe20a2c9eba49d43a154851cfc1c62f933eb5158f109ee5179d928d7b10f29b036204c7d4e4f6ba25f6f15e694eba53825908096ee23610dbd7b52db2434afd12a4764573d0ba237bb7aeab6250282659a6078fcc4c0418a4c93a4fd5cc835b9097ed180d62a981e4e240a279ec65af38e61f258865)

### Reference
- [https://cankut.github.io/posts/2020-05-12-image-to-prime.html](https://cankut.github.io/posts/2020-05-12-image-to-prime.html)
- 