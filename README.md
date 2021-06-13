# image-to-prime

Convert an image to a prime number

Read Article: [https://cankut.github.io/posts/2020-05-12-image-to-prime.html](https://cankut.github.io/posts/2020-05-12-image-to-prime.html)

## usage
- use `main.py` to search for a prime (you can spawn multiple processes to speed up search.)
- use `json_to_image.py` to generate 1:1 size image of the number
- use `json_to_ann.py` to generate zoomed and annotated image of the number

```python
# SEARCH FOR PRIME
from PrimeSearcher import PrimeSearcher

ps = PrimeSearcher("./images/onez.jpg")
ps.rescale(60*60, fit_to_original=True)
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

### Original
![onez](images/onez.jpg)

### Annotated
<!-- ![Euler](results/euler/54x66/ann_prime_2020-05-11%20213910.json.png) -->

### JSON Result
```json
{
    "number": 2037111551117730886711559995551138831155999995551748615559999955117603715599999955176033711599995160000660000061570446603336637775717771631555951717155510315555517111555146715599171175551483715557315377734463733733336666644063333771733760044063777117736486444006377333042236044400633364849,
    // "colors": [
    //     [0.3479211214065086, 0.23347868013920475, 0.14823277849984912],
    //     [0.2815586707851046, 0.3773689510426217, 0.40126042338458856],
    //     [0.48717921743958276, 0.36338973145144743, 0.24840536512667527],
    //     [0.6182133503220937, 0.49793809220439744, 0.35050005561791925],
    //     [0.02654862493942841, 0.021978245399974602, 0.02203684767592213],
    //     [0.12655721332193415, 0.12490929843872685, 0.1102798499857489],
    //     [0.42733855768276996, 0.5973525554122767, 0.6064301381035793],
    //     [0.8546366380886893, 0.7648025887560214, 0.6236397562502932],
    //     [0.9376091452206143, 0.8917815563725646, 0.7817344515931582],
    //     [0.7420198057810117, 0.6295635170556594, 0.48933234964221195]
    // ],
    // "size": [54, 66]
}
```

