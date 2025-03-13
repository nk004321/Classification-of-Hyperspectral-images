# Hyperspectral Image Classifier

## Overview
This project is a graphical user interface (GUI) application built using Tkinter for classifying hyperspectral images using either Support Vector Machine (SVM) or Multi-Layer Perceptron (MLP) models. It allows users to load hyperspectral image datasets, perform preprocessing, apply dimensionality reduction, train machine learning models, and visualize results.

## Features
- Load hyperspectral image datasets and ground truth from `.mat` files.
- Display ground truth images.
- Choose between SVM and MLP classifiers.
- Perform dataset splitting, PCA (Principal Component Analysis), and standardization.
- Train and test SVM and MLP models.
- Display classification accuracy.
- Reconstruct and visualize classified images.

## Requirements
Ensure you have the following Python libraries installed before running the script:

```bash
pip install numpy scipy scikit-learn pillow matplotlib
```

## How to Use
1. Run the script using Python:
   ```bash
   python script.py
   ```
2. Load a hyperspectral image dataset (`.mat` file) by clicking the **"Load mat file"** button.
3. Load the corresponding ground truth (`.mat` file) using the **"Load Ground Truth"** button.
4. Optionally, display the ground truth image by clicking **"Show Ground Truth"**.
5. Select a classification model (SVM or MLP) from the dropdown menu.
6. Click **"OK"** to confirm the model selection.
7. Based on the selected model:
   - For SVM:
     - Perform dataset splitting.
     - Apply PCA (optional).
     - Train the SVM model.
     - Test the model.
     - View accuracy.
   - For MLP:
     - Perform one-hot encoding and standardization.
     - Perform dataset splitting.
     - Apply PCA (optional).
     - Train the MLP model.
     - Test the model.
     - View accuracy.
     - Reconstruct and visualize the classification output.

## Code Structure
- `ldmatfile()`: Loads the hyperspectral dataset.
- `ldgtfile()`: Loads the ground truth and preprocesses the data.
- `shwgt()`: Displays the ground truth image.
- `ok()`: Handles model selection (SVM or MLP) and enables corresponding buttons.
- `svmdivntrn()`: Splits the dataset for SVM training and testing.
- `svmPca()`: Applies PCA for dimensionality reduction in SVM.
- `svmtraining()`: Trains the SVM model.
- `svmtesting()`: Tests the SVM model.
- `svmacc()`: Displays SVM model accuracy.
- `onehotenc()`: Applies one-hot encoding for MLP.
- `mlpdivntrn()`: Splits dataset for MLP.
- `mlpPca()`: Applies PCA for MLP.
- `mlptraining()`: Trains the MLP model.
- `mlptesting()`: Tests the MLP model.
- `mlpacc()`: Displays MLP model accuracy.
- `mlpresurect()`: Reconstructs classified image output.
- `mlpplot()`: Plots and visualizes classification results.

## Notes
- Ensure that the dataset and ground truth files are in `.mat` format.
- The application is designed for the **Indian Pines dataset**, but can be adapted for other datasets with similar structures.

## License
This project is open-source and can be modified and distributed freely.

---
Feel free to enhance or customize this README as needed!

