 <h1 style="text-align: center;">Project NLP: Resume Extraction - Week 9 Deliverables
<br></br>

## NLP Interns at Data Glacier
BatchCode: LISUM20 

Group Name: TeamNLP 

|      Name      |            Email            | Country |            College/Company            | Specialization |
|:--------------:|:---------------------------:|:-------:|:--------------------------------------:|:--------------:|
|  Nilsu Bozan   |   bozannilsu@gmail.com      | Turkey  | Binghamton University/Istanbul Technical University |      NLP       |
|  Nishchay Vaid |     Nishchay89@gmail.com     |   USA   |            Rutgers University          |      NLP       |
|  Anish Mitra   | anishmitra9666@gmail.com    |   USA   |         Montana State University       |      NLP       |
| Sukriti Macker |    sm11017@nyu.edu           |   USA   |          New York University          |      NLP       |

<br></br>

## Problem Description
Resumes contain surfeit information that is not relevant for the HR/authority, and they have to manually process the resumes to shortlist the promising candidates for them. And, thus making the shortlisting task a herculean task for HR. By making use of the NER(Named Entity Recognition) model of NLP this problem can be solved by finding and classifying the entities that are present in each resume into predefined classes such as person name, college name, academics information, relevant experiences, skill set, etc.

## GitHub Link Repo
https://github.com/nishchayvaid/Resume-Extraction/tree/develop

## Data Cleansing & Transformation

### - Nischay
Importing libraries:
- import pandas as pd: Imports the pandas library for data manipulation and analysis.
- import re: Imports the re module for regular expression operations.
- import nltk: Imports the Natural Language Toolkit (NLTK) library for natural language processing.
- import spacy: Imports the Spacy library for advanced natural language processing.
- from num2words import num2words: Imports the num2words module for converting numbers to words.

Data preprocessing:
- Lowercasing the text using resume.lower().
- Removing newlines using re.sub("\n", ' ', resume).
- Removing special characters using re.sub(r'[,•()➢❑]', ' ', resume).
- Removing extra whitespaces, dashes, and dots using re.sub(r'\s\s+|\s-\s|\.\s', ' ', resume).
- Tokenizing the text into words using resume.split(" ").
- Converting digits to words using num2words(tokenized_words[i]).
- Removing stopwords using NLTK's stopwords and a custom implementation.
- Joining the tokens back into a string.
Reading and saving data:
- Reading a JSON file into a DataFrame using pd.read_json('Resume.json', lines=True).
- Saving the DataFrame to a CSV file using df.to_csv('dataframe.csv', index=None).
Vectorization and feature extraction:
- Using the Tf-Idf vectorizer from scikit-learn (sklearn.feature_extraction.text.TfidfVectorizer) to calculate the Tf-Idf values of words and collocations.
- Creating an instance of the Tf-Idf vectorizer with a specified ngram range using TfidfVectorizer(ngram_range=(1, 3)).
- Applying the Tf-Idf vectorizer to the text data using vect.fit_transform(content_resumes).
- Retrieving the terms (words and collocations) in the same order as they appear in the Tf-Idf matrix using vect.get_feature_names_out().

Part-of-speech tagging:
- Using NLTK's pos_tag function to assign part-of-speech tags to the terms obtained from the Tf-Idf matrix using nltk.pos_tag(terms).
- Using Spacy's language model to process the text and assign part-of-speech tags to each word using nlp(text) and word.pos_.

### By Anish

Importing libraries(block 1):
- Imported the necessary libraries(json, pandas, numpy and pickle).

Opening JSON file(block 2):
- Used the pickle module to convert the JSON file to a list as shown in one of the modules we completed individually.

Taking a high-level look at the raw data(block 3):
- Printed out each resume to see what the raw resumes looked like.

Creating dataframe(block 4):
- I created a dataframe with two separate columns(the annotations and lists).
- I printed out the dataframe 

Converting to list(block 5):
- I firstly converted the annotations dataframe to a list and printed it out.
- I then counted the number of values in the dataframe.
- Finally, I created a new list with just the information.

Converting new list to dataframe(block 6):
- I then converted the new list I created into a dataframe.

Creating lists for the row number, information and field asked(block 7):
- I used dictionaries to separate the information about the candidate to the field where the question was asked.
- I also printed out row numbers.

Counted the number of elements in each list and printed out the elements as well as their type(block 8):
- I counted the number of elements in the row number, candidate information and the field it is in.
- I then created a window function to group each candidate by the row number.

Created final csv(block 9):
- I created a dataframe based on the lists of row number, candidate number, candidate information and desired field.
- I converted this list to csv.
- I edited a few inconsistencies in excel like missing values and duplicate values.
- I printed out the csv. 

## By Nilsu

