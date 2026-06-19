# Deep Learning Examples: Neural Networks, CNNs, and RNNs

This ZIP contains beginner-friendly deep learning examples with input files included.

## Folder Structure

1. `01_neural_networks_tabular_classification`
   - Uses a small customer churn CSV dataset.
   - Demonstrates a basic Artificial Neural Network using dense layers.

2. `02_cnn_image_classification`
   - Uses generated simple image data: circles and squares.
   - Demonstrates a Convolutional Neural Network.

3. `03_rnn_text_sentiment`
   - Uses a small sentiment dataset.
   - Demonstrates a basic RNN/LSTM for text classification.

## Installation

Create and activate virtual environment first.

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install tensorflow pandas numpy scikit-learn matplotlib pillow
```

## How to Run

Each folder contains:
- input files
- Python script
- Jupyter notebook
- README

Example:

```bash
cd 01_neural_networks_tabular_classification
python ann_customer_churn.py
```

These examples are intentionally simple for classroom/training use.
