import math
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap, rgb_to_hsv, hsv_to_rgb
from matplotlib import pyplot
import matplotlib as mpl
import json

def load_from_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data["number"], data["colors"],data["size"]

def get_scaled_size(image, new_dimension):
    #calculate scale factor and preserve aspect ratio
    scale_factor = 1 / math.sqrt(image.width*image.height/new_dimension)
    new_size = round(image.width * scale_factor), round(image.height*scale_factor)
    return new_size

def digits_to_int(digits):
    return int("".join(map(str,digits)))

def cluster_image(image, new_size, fit_to_original):

    # resize image
    resized_image = image.resize(new_size, resample=Image.BILINEAR)

    data = np.array(image).reshape(-1,3)
    data_resized = np.array(resized_image).reshape(-1,3)

    # cluster pixels according to RGB values into 10 groups
    kmeans = KMeans(n_clusters = 10, random_state=0)

    # choose to fit points in original image or resized image
    if(fit_to_original):
        kmeans.fit(data)
    else:
        kmeans.fit(data_resized)

    # shuffle cluster until first digit is non-zero
    while True:
        first_digit = kmeans.predict([data_resized[0]])[0]
        if(first_digit > 0):
            break
        else:
            np.random.shuffle(kmeans.cluster_centers_)

    # get color palette, normalize RGB values to [0,1]
    colors = kmeans.cluster_centers_ / 255

    # return cluster label of each pixel in resized image
    digits = kmeans.predict(data_resized)

    return digits,colors

def add_random_noise(num, noise_ratio, noise_count):

    digits = list(str(num))
    
    n = len(digits)

    if noise_count != None:
        n_noise = noise_count
    else:
        n_noise = round(n * noise_ratio)

    for _ in range(n_noise):
        i = int(np.random.randint(0,n))
        noise = np.random.randint(1,10)           

        digits[i] = str((int(digits[i]) + noise) % 10)

        # make first digit non-zero if necessary
        if(digits[i] == '0'):
            digits[i] = str(np.random.randint(1,10))

    return int(''.join(digits))

def get_possible_prime_variants(num):

    variants = []

    base = num - (num % 10)

    variants.append(base+1)
    variants.append(base+3)
    variants.append(base+7)
    variants.append(base+9)

    return variants

def get_contrasting_colors(colors):

    hsv_colors = rgb_to_hsv(colors)

    contrast_colors = []

    for c in hsv_colors:
        h,s,v = c
        if (v < 0.3):
            s = s*0.2
            v = 0.35
        else:
            if v + 0.15 > 1:
                v -= 0.1
            else:
                v += 0.1
        
        contrast_colors.append(hsv_to_rgb([h,s,v]))
    
    return contrast_colors

def plot_number(number, colors, size, annotate, show_colorbar = False):

    # configure figure size
    f = pyplot.gcf()
    m = max(size)
    pyplot.rcParams["figure.figsize"] = (m*20/f.dpi,m*20/f.dpi)
    
    w,h = size
    cmap = ListedColormap(colors)
    digits = list(map(int,str(number)))
    data = np.array(digits).reshape(size[::-1])

    f, ax = pyplot.subplots()
    ax.axis('off')
    ax.imshow(data,cmap=cmap)    
      
    if annotate:

        if show_colorbar:
            # show color palette
            p = ax.get_position().bounds
            fig_size = f.get_size_inches()
            ax_colors = f.add_axes([p[0]+p[2]+0.03, p[1]+p[3]-(2/fig_size[0]), (fig_size[1]/fig_size[0])*(.2/fig_size[0]), 2/fig_size[0]],label="colorbar")
            ax_colors.tick_params(labelsize='medium')
            ax_colors.get_xaxis().set_ticks([])
            ax_colors.get_yaxis().tick_right()
            ax_colors.get_yaxis().set_ticks(np.arange(0,10))
            ax_colors.imshow(np.arange(0,10).reshape(-1,1), cmap=cmap)

        contrast_colors = get_contrasting_colors(colors)
        for x in range(w):
            for y in range(h):
                c = contrast_colors[data[y,x]]
                ax.annotate(str(data[y,x]), xy=(x, y), color=c,size='small', ha="center",va="center")
                
                


    return f