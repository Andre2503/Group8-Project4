# Fake News Detection

## Project Overview
In the era of information overload, distinguishing between real and fake news has become increasingly challenging. This project aims to address this issue by employing machine learning techniques to accurately classify news articles. Our comprehensive approach involves experimenting with various models to discern which best understands the nuances of language indicative of fake news. The culmination of this project is an interactive application powered by Gradio, allowing users to input articles and receive real-time predictions.

## Features
- **Data Preprocessing:** Cleaning, tokenizing, and vectorizing text data for model ingestion.
- **Model Exploration:** Experimenting with multiple machine learning models to evaluate performance.
- **CNN Implementation:** Employing a Convolutional Neural Network for deep learning analysis of text data.
- **Performance Comparison:** Analyzing and comparing model metrics to identify the best performer.
- **Gradio App:** Providing a user-friendly interface for real-world testing and demonstration.

## Dataset
The initial dataset for this project was sourced from Kaggle: [Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification). It comprises various news articles labeled as 'Fake' or 'Real'. 

- **Content:** The dataset includes news articles with associated binary labels indicating their authenticity (1 for fake, 0 for real).

## Data Cleaning and Preprocessing

Data cleaning and preprocessing were crucial for preparing the raw dataset for modeling. The notebook `01_Data_Processing_Team8_Prj4.ipynb` outlines the process we followed to clean and preprocess the data. Below are the key steps undertaken:

### 1. Initial Dataset Loading:
- **Load Data:** The raw dataset is loaded into a pandas DataFrame. This step involves reading the CSV file and examining the first few rows of the dataset to understand its structure and contents.

### 2. Data Cleaning:
- **Missing Values:** We checked for and handled missing values. This involved filling missing values with appropriate substitutes or dropping rows/columns.
- **Text Cleaning:** The text was cleaned to ensure consistency and effectiveness in analysis. This involved:
  - **Lowercasing:** Converting all text to lowercase to treat words like "The" and "the" as the same word.
  - **Removing Special Characters and Punctuation:** Stripping out unnecessary symbols, numbers, and punctuation marks.
  - **Handling White Spaces:** Removing extra white spaces, tabs, and new lines.

### 3. Text Tokenization:
- **Tokenization:** The cleaned text was then tokenized, splitting the text into individual words or tokens. This is a crucial step as most algorithms work on a per-word basis.

### 4. Stop Words Removal:
- **Removing Stop Words:** Common words like 'is', 'and', 'the', etc., which don't carry much meaning, were removed from the text. This helps reduce the dimensionality of the data and improves the focus on relevant words.

### 5. Stemming/Lemmatization:
- **Stemming/Lemmatization:** These techniques were used to reduce a word to its root form. Stemming might reduce 'running' to 'run', and lemmatization considers the context and converts 'ran' to 'run'. It helps reduce the complexity and variations in the text.

### 6. Vectorization: 
- **Preparing for Modeling:** Post-cleaning, texts were usually converted into a format suitable for machine learning models. We utilized techniques like Bag of Words, TF-IDF, and word embeddings.

### 7. Saving the Cleaned Data:
- **Storing Processed Data:** Finally, the cleaned and processed data was saved back as FakeNews_Processed_Data.csv, ensuring it's readily available for the next steps in the project without the need to redo the cleaning.

## Next Steps:
The cleaned and preprocessed data is now ready for exploratory data analysis, feature engineering, and modeling, which are covered in the relevant notebooks and sections. We used a separate notebook for each model.

## Acknowledgements

This project was made possible through the hard work and dedication of our team members and the invaluable support provided by our teaching staff. We'd like to take this opportunity to acknowledge each individual's contributions, namely:

### Team Members:
- **Andrea Aurrecoechea Diaz** 
- **Edrin Ngadze** 
- **Nestor Padro** 

### Teaching Staff:
Special thanks to the teaching staff who provided guidance, support, and expertise throughout the duration of this project:

- **Mortaza Rezae:** Our class teacher who also provided us with a high-level guide to approach the NLP project and invaluable help and guidance throughout. 
- **Camilo Vargas** and **Jeffrey Chieh Liu:** The support staff that provided us with help and troubleshooting support.

Their contributions were invaluable, and their willingness to share their knowledge and experience greatly enhanced the quality of our work.

### External Code and Resources:
We would also like to acknowledge the use of external code and resources that significantly contributed to the development of this project:

- **ChatGPT-4 by OpenAI:** For providing code snippets, explanations, and guidance on best practices in machine learning and data science.

### Tools and Libraries:
Special thanks to the developers and maintainers of the various tools and libraries we used, including TensorFlow, Keras, Pandas, NumPy, NLTK/SpaCy, and Gradio.

We are incredibly grateful to everyone who contributed to these amazing technologies that make projects like these possible. Thank you!

## Installations
This project requires the following libraries:
- Python 3.x
- TensorFlow 2.x
- Pandas
- NumPy
- Sklearn
- Gradio
