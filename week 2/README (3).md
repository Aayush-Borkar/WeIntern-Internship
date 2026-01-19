
# 📩 Text Classification Model – Spam Detection

## 📌 Project Overview
This project implements a **Text Classification System** to classify SMS messages as **Spam** or **Ham (Not Spam)** using **Machine Learning** techniques. The model is trained on the **SMS Spam Collection Dataset** and uses **TF-IDF vectorization** with **Logistic Regression** for classification.

The project demonstrates a complete NLP pipeline including **text preprocessing, feature extraction, model training, evaluation, and testing on new unseen data**.

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Libraries & Tools:**
  - Scikit-learn
  - NLTK
  - Pandas
  - Matplotlib
  - Seaborn  

---

## 📂 Dataset
**SMS Spam Collection Dataset**
- Total messages: **5,572**
- Labels:
  - `ham` → Normal message
  - `spam` → Spam message
- Format: Tab-separated text file

Example:
```
ham	Hey, are we meeting today?
spam	Congratulations! You won a free prize!
```

---

## 🔄 Project Workflow
1. Load and explore the dataset  
2. Text preprocessing (lowercasing, punctuation removal, stopword removal)  
3. Feature extraction using **TF-IDF Vectorizer**  
4. Train-test split  
5. Model training using **Logistic Regression**  
6. Model evaluation using precision, recall, F1-score, and confusion matrix  
7. Testing the model on **new unseen messages**  

---

## 🧠 Model Used
- **Logistic Regression**
- `class_weight='balanced'` to handle class imbalance
- TF-IDF features (with optional n-grams)

---

## 📊 Model Evaluation

Accuracy achieved: **97%**

**Classification Summary:**
- Ham messages: Excellent recall (1.00)
- Spam messages: High precision (0.99)
- Balanced performance overall

---

## 🧪 Testing on New Data
Example predictions:
```
"Congratulations! You won a free ticket" → SPAM
"Hey, are we meeting for lunch?" → HAM
```

---

## 🚀 Future Improvements
- Use Naive Bayes or SVM
- Apply Word2Vec or GloVe embeddings
- Build a Streamlit Web App
- Multi-class classification
- Deploy as an API

---

## 📌 Use Cases
- Spam message filtering
- Email classification
- Sentiment analysis
- News categorization

---

## 👨‍💻 Author
**Aayush**

---

## ✅ Conclusion
This project successfully demonstrates an end-to-end **Text Classification Model** using NLP and Machine Learning. The model achieves high accuracy while maintaining strong precision and recall, making it suitable for real-world spam detection systems.
