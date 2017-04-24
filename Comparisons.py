__author__ = "Kevin Gay"

from PIL import Image
import math

class Comparisons(object):
    """
    Creates an object where the arguments are two images. You can then call
    any of the functions to obtain the MSE, RMSE, or PSNR.
    """

    def __init__(self, image, noisyImage):
        """
        :param image: The path to the original image with no noise.
        :param noisyImage: The path to the noisy image.
        """

        self.image = image
        self. noisyImage = noisyImage


    def MSE(self):
        """
        Pre: image and noisy image are assumed to be of the same dimensions
        :return: The mean squared error as a float
        """
        im = Image.open(self.image).convert('L')
        width, height = im.size
        mat = im.load()

        noise = Image.open(self.noisyImage).convert('L')
        noiseMat = noise.load()

        squareDiff = []

        for i in range(width):
            for j in range(height):
                squareDiff.append(pow(mat[i, j] - noiseMat[i, j],2))

        meanSquaredError = sum(squareDiff) / len(squareDiff)
        return meanSquaredError

    def RMSE(self):
        """
        Pre: image and noisy image are assumed to be of the same dimensions
        :return: The root mean squared error as a float
        """
        mse = self.MSE()
        rmse = math.sqrt(mse)
        return rmse

    def PSNR(self):
        """
        Pre: image and noisy image are assumed to be of the same dimensions
        :return: the peak-signal-to-noise ratio between two images
        """
        mse = self.MSE()
        return 10.0 * math.log10(pow(255.0, 2) / mse)


def test():
    c = Comparisons('jaguar.jpg', 'jaguar-noise0.05.jpg')
    print c.RMSE()
    print c.PSNR()
