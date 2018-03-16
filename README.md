# morphological_evolver
Evolves a list of morphological operators for SVM training on the CIFAR-10 dataset.
For this application, morphological operators (such as thinning, dilation, segmentation, etc.) are treated as genes.
A list, e.g. [m1, m2, ... , mN], of the genes is treated as the chromosome.
The "most fit" chromosomes are evolved until a fitness criteria is met. In this case, it means the evolution is finished when a Support Vector Machine (SVM) is trained on the CIFAR-10 dataset, after being modified by the list of operators, to a desirable accuracy. A SVM is trained on the CIFAR-10 dataset without any morphological operators being applied as a baseline for comparison.

For example, consider a list of operators such as the following: [m1, m2, m3], where m1 could be segmentation, m2 thinning, and m3 dilation. The first element, m1, is applied to an image in the dataset. Then the second element, m2, is applied, then the third (m3). This means the image was first segmented, then thinned, then dilated. An SVM is trained on this new image with the CIFAR-10 labels provided from the original dataset. The accuracy of this SVM is compared with the accuracy of an SVM trained on the original image (without any morphing).

The goal of this project is to determine if an optimal combination of morphological operators can be randomly determined using a genetic algorithm, such that the accuracy of the SVM trained on the morphed images is compared to a SVM trained on the original images.
