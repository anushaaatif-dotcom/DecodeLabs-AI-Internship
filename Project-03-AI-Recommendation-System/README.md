# Project 03 - AI Recommendation System

## Overview
This system implements a production-grade **Content-Based AI Recommendation System** constructed on an **Input-Process-Output (IPO) Model Architecture**. Instead of deploying bulky, opaque neural network models, this engine achieves precision tracking through transparent mathematical mapping via **Term Frequency-Inverse Document Frequency (TF-IDF)** and **Cosine Similarity** algorithms.

The engine successfully mitigates user-level choice overload by transforming qualitative textual choices into multi-dimensional vectors and comparing their angular alignment against item parameters.

## Core Features
- **Multi-Factor Ingestion Pipeline**: Collects a sequence of user interest criteria to construct an analytical profile.
- **Dynamic Vocabulary Vector Mapping**: Utilizes TF-IDF strategies to reward specialized descriptive properties while reducing the weight of generic terms.
- **Cosine Similarity Engine**: Evaluates orientation alignment across high-dimensional features using the standard formula:
  $$cos(\theta) = \frac{A \cdot B}{\vert{}\vert{}A\vert{}\vert{} \vert{}\vert{}B\vert{}\vert{}}$$
- **Cold Start Bypass Logic**: Detects low-density data interactions and dynamically defaults to pre-calculated baseline recommendation models.
- **Interactive Console Dashboard**: Clear visual tracking showing calculated precision percentage margins.

## Technologies Used
- **Python 3**
- **Pandas**: Structured dataset parsing matrix.
- **NumPy**: Vector math calculations.
- **Scikit-Learn**: Vectorization models and distance metrics computation matrices.

## How to Set Up and Run

1. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt