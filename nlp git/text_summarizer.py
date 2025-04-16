import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Basic Summarizer Function
def summarize_text(text, max_sentences=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    # Build frequency table
    freq_table = {}
    for word in words:
        if word not in stop_words and word not in string.punctuation:
            freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

    # Get top N sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    summary = ' '.join(summary_sentences)
    return summary
