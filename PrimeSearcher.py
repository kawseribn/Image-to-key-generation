from PrimeChecker import is_prime
from PIL import Image
from matplotlib import pyplot
from matplotlib.colors import ListedColormap
import os, time, json
import Utils
import numpy as np

class PrimeSearcher:

    def __init__(self, image_file):
        self.__image = Image.open(image_file)
        self.__image_name = os.path.basename(self.__image.filename).split('.')[0]

    def __get_save_folder(self):
        size_name = str(self.__new_size[0])+"x"+str(self.__new_size[1])
        save_folder = "results/{}/{}/".format(self.__image_name, size_name)
        return save_folder

    def __save_number_image(self, name, number, annotate):
        os.makedirs(self.__save_folder, exist_ok=True)
        f = Utils.plot_number(number, self.__colors, self.__new_size, annotate)
        f.savefig(self.__save_folder+name)

    def __save_prime(self, num):

        timestamp = time.strftime("%Y-%m-%d %H%M%S")

        logData = {
            "number" : num,
            "colors": self.__colors.tolist(),
            "size": self.__new_size
        }

        self.__save_number_image("prime_" + timestamp + ".png", num, annotate=False)

        logFile = self.__save_folder + "prime_" + timestamp + ".json"
        with open(logFile, "w") as outfile:
            json.dump(logData, outfile)

    def rescale(self, dimension, fit_to_original):

        # get new size fitting to new dimension
        self.__new_size = Utils.get_scaled_size(self.__image, dimension)
        self.__save_folder = self.__get_save_folder()

        digits, colors = Utils.cluster_image(self.__image, self.__new_size, fit_to_original=fit_to_original)

        self.__colors = colors
        self.__seed_num = Utils.digits_to_int(digits)

        self.__save_number_image("clustered.png", self.__seed_num, annotate=False)
        self.__save_number_image("clustered_ann.png", self.__seed_num, annotate=True)

    def search(self, max_iterations, noise_ratio = 0.005, noise_count = None, break_on_find = True):

        iteration=0
        found_primes = []
        num = self.__seed_num
        explored_variant=[]


        while True:

            print("Iterarion #{}".format(iteration))

            variants1 = Utils.get_possible_prime_variants(num)
            variants2 = Utils.get_possible_prime_variants(num)
            variants3 = Utils.get_possible_prime_variants(num)
            variants=[]
            variants.append(variants1)
            variants.append(variants2[::-1])
            variants.append(variants3[::-1])
            for i in range(len(variants)):
                for v in variants[i]:
                    if v not in explored_variant:
                        if is_prime(v):
                            found_primes.append(v)
                            explored_variant.append(v)
                            print("Found prime! Count={}".format(len(found_primes)))
                            self.__save_prime(v)
                            if(break_on_find):
                                break

            if break_on_find and len(found_primes) > 2:
                break
            else:
                num = Utils.add_random_noise(self.__seed_num, noise_ratio, noise_count)

            iteration+=1
            if iteration > max_iterations:
                break

        return found_primes
