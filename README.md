Project Proposal: Image Restoration using Imputation Techniques


Description of the Project
This project focuses on restoring corrupted images represented as matrices with missing entries. The goal is to explore various imputation methods such as mean, median, mode, and Singular Value Decomposition (SVD) to fill in the missing values, and evaluate which method provides the best visual restoration. The project will involve collecting a dataset of images, corrupting them by removing random pixel values, and then applying different imputation techniques to recover the missing pixels.

Clear Goal(s)
The primary goal of this project is to successfully restore corrupted images by filling in missing pixels using different imputation methods. The performance of these methods will be evaluated based on how well they restore the images to their original form, using both visual inspection and quantitative metrics such as Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM).

Data Collection
The dataset will be collected from publicly available image databases such as CIFAR-10, MNIST, or ImageNet, depending on the project’s scope. The corruption process will be simulated by randomly removing pixel values from the images, representing these missing values with a placeholder (e.g., NaN).

How I Plan on Modeling the Data
The project will model the missing data using several imputation techniques:

Mean Imputation: Filling missing pixels with the mean value of neighboring pixels.
Median Imputation: Filling missing pixels with the median value of neighboring pixels.
Mode Imputation: Using the most frequent value from neighboring pixels to fill missing data.
SVD Imputation: Using Singular Value Decomposition to approximate missing pixel values based on the relationships between known pixel values.
The imputation methods may be extended with more advanced techniques (e.g., matrix factorization or deep learning models like autoencoders) if time permits.

Data Visualization
I will visualize the results using several methods:

Side-by-Side Image Comparisons: Display the original image, corrupted image, and restored image for each method.
Quantitative Metrics (e.g., PSNR, SSIM): These will be plotted to provide a numerical comparison of the performance of different imputation methods.
Interactive Heatmaps: To show the locations of the missing pixels and the values used for imputation.
Test Plan
The dataset will be divided into training and testing sets. Specifically, 80% of the images will be used for training the models and fine-tuning the imputation methods, while the remaining 20% will be used for testing and evaluation. The test set will not be corrupted in the same manner as the training set to ensure the model generalizes well to different types of missing data.

