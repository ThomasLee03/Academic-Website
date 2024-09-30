# Image Restoration using Imputation Techniques

## Description of the Project
This project focuses on restoring corrupted images represented as matrices with missing pixel values. We will explore various imputation techniques such as mean, median, mode, Singular Value Decomposition (SVD), and more advanced methods such as matrix factorization and deep learning (e.g., autoencoders). The goal is to fill the missing pixels and evaluate which method yields the best restoration based on both visual quality and quantitative metrics like Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM).

## Clear Goal(s)
- Successfully restore corrupted images by filling missing pixel values using various imputation techniques.
- Compare the effectiveness of basic statistical methods (mean, median, mode), matrix factorization, and autoencoders.
- Measure performance based on visual inspection and quantitative metrics (e.g., PSNR, SSIM).

## Data Collection
We will use publicly available image datasets such as CIFAR-10. To simulate corrupted images, we will randomly remove pixel values, replacing them with placeholders (e.g., `NaN`). These datasets will serve as our training and testing ground for the various imputation techniques.

## How We Plan on Modeling the Data
We will model the data using a combination of statistical imputation methods and machine learning techniques:

1. **Mean, Median, Mode Imputation**: Use simple statistical methods to fill missing pixels based on neighboring pixel values.
2. **Singular Value Decomposition (SVD)**: Use SVD to approximate missing pixel values based on the relationships between known pixel values.
3. **Matrix Factorization**: Implement matrix factorization, treating the image as a low-rank matrix. We will train the model to predict the missing pixel values based on the known ones.
4. **Autoencoders (Deep Learning)**: Train an autoencoder to reconstruct images by learning a compressed representation of the corrupted images and generating missing pixels as output.

The machine learning-based methods will require training on a portion of the dataset to learn patterns and relationships between pixel values.

## Data Visualization
We plan to visualize the results through:
- **Side-by-Side Image Comparisons**: Display the original, corrupted, and restored images for each imputation method.
- **Quantitative Metric Plots**: Plot PSNR and SSIM scores to compare the performance of different methods.
- **Heatmaps**: Visualize the locations of missing pixels and their imputed values.
- **Interactive Visualizations**: Create interactive plots to allow the user to explore the impact of different imputation methods.

## Test Plan
We will divide the dataset into training and testing sets:
- **80% for Training**: This will be used to train models like matrix factorization and autoencoders.
- **20% for Testing**: This will serve as our evaluation set for the imputation methods. The corrupted version of this test set will not have the same corruption pattern as the training data to test generalization.
  
We will use cross-validation for parameter tuning, particularly for the matrix factorization and autoencoder models, to ensure they generalize well to unseen data.

## Timeline
### Week 1 (10/1 - 10/7)
- Submit the project proposal.
- Begin collecting datasets (CIFAR-10, MNIST) and finalize the corruption process.

### Week 2 (10/8 - 10/14)
- Implement the data corruption process and prepare the dataset.
- Begin implementing basic imputation methods (mean, median, mode).

### Week 3 (10/15 - 10/21)
- Finalize the implementation of SVD imputation.
- Generate preliminary visualizations of corrupted and restored images.

### Week 4 (10/22 - 10/28)
- Implement matrix factorization for imputation.
- Continue refining visualizations and collect initial results.

### Week 5 (10/29 - 11/4)
- Implement autoencoder-based imputation.
- Prepare for the midterm report and presentation.

### Midterm Report (Due 11/5)
- Submit README.md with preliminary visualizations, descriptions of data processing, modeling methods used so far, and preliminary results.
- Record and upload a 5-minute presentation summarizing the project progress.

### Week 6-7 (11/6 - 11/18)
- Further refine matrix factorization and autoencoder models.
- Explore additional advanced techniques, if time permits.

### Week 8-9 (11/19 - 12/2)
- Test the models on the withheld test set.
- Finalize visualizations and prepare the final code repository.

### Week 10 (12/3 - 12/10)
- Finalize and submit the project report, including:
  - Instructions on how to build and run the code, using a `Makefile`.
  - Test code and a GitHub workflow for automating testing.
  - Final visualizations and results.

## Final Report (Due 12/10)
- Ensure that the `README.md` includes:
  - Instructions for building and running the project.
  - Testing code and automated workflow in the GitHub repo.
  - Detailed descriptions of the data processing and modeling steps.
  - Final visualizations and results demonstrating the success of the imputation methods.
