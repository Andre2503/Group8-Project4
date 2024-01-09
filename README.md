# Fake News Detection

## Project Overview
In the era of information overload, distinguishing between real and fake news has become increasingly challenging. This project aims to address this issue by employing machine learning techniques to accurately classify news articles. Our comprehensive approach involves experimenting with various models to discern which best understands the nuances of language indicative of fake news. The culmination of this project is an interactive application powered by Gradio, allowing users to input articles and receive real-time predictions.

## Features
- **Data Preprocessing:** Cleaning, tokenizing, and vectorizing text data for model ingestion.
    - The project explored two approaches to word embedding and vectorizing: Word2Vec and tensorflow.keras. 
- **Model Exploration:** Experimentation with Logistic Regression (Accuracy: 87%), Random Forests (Accuracy: 89%), Deep Neural Networks (Accuracy: 92%), and Convolutional Neural Networks to evaluate performance.
- **CNN Implementation:** Convolutional Neural Network used for deep learning analysis of text data processed using tensorflow.keras, achieving 94% accuracy.
- **Gradio App:** User-friendly interface for real-world testing and demonstration.

## Dataset
The initial dataset was sourced from Kaggle's [Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification), comprising various labeled news articles. 
- **Content:** News articles with binary labels indicating authenticity (1 for fake, 0 for real).
- The dataset is available on Google Drive in the `Resources` folder: [Google Drive Link](https://drive.google.com/drive/folders/1I8wobQdwvYev9w2sf_sMDh49NxGTsyUq?usp=drive_link)

## Data Cleaning and Preprocessing
Data cleaning and preprocessing were essential for preparing the dataset for modeling. The process is outlined in `01_Data_Processing_Team8_Prj4.ipynb`.

### Steps:
1. **Dataset Loading:** Loading data into a pandas DataFrame, examining the structure and contents.
2. **Data Cleaning:** Handling missing values, lowercasing, removing special characters, punctuation, and handling white spaces.
3. **Text Tokenization:** Splitting cleaned text into individual words or tokens.
4. **Stop Words Removal:** Removing common words with minimal meaning.
5. **Stemming/Lemmatization:** Reducing words to their root form.
6. **Vectorization:** Employing Word2Vec and tensorflow.keras for data vectorization.
7. **Final Application:** Test the model with your own data at [Gradio App](https://8b55359b3bd7326898.gradio.live)

### Directory Structure:
- `Database` - `Fake_News_DB_SourceCode`: SQL code for our schema.
- `FND_API`: API files.
- `Models`: Contains `CNNmodelV2.keras`, the selected model for our application which achieved a 94% accuracy. 
- `Notebooks`: Various notebooks for data processing, model exploration, and implementation using the different approaches to tokenisation. 

### Additional Models:
Other models are available on Google Drive in the `models` folder: [Google Drive Link](https://drive.google.com/drive/folders/1I8wobQdwvYev9w2sf_sMDh49NxGTsyUq?usp=drive_link)

## Acknowledgements
This project was made possible by our team and the invaluable support of our teaching staff.

### Team Members:
- Andrea Aurrecoechea Diaz
- Edrin Ngadze
- Nestor Padro

### Teaching Staff:
- **Mortaza Rezae:** Class teacher and guide.
- **Camilo Vargas** and **Jeffrey Chieh Liu:** Support staff.

### External Code and Resources:
- **ChatGPT-4 by OpenAI:** For code snippets and guidance.

### Tools and Libraries:
Thanks to TensorFlow, Keras, Pandas, NumPy, NLTK/SpaCy, and Gradio.

## Installations
Required libraries:
- Python 3.x
- TensorFlow 2.x
- Pandas
- NumPy
- Sklearn
- Gradio

