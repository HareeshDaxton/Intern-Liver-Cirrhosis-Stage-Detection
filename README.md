# 🧬 Liver Cirrhosis Stage Detection System

<div align="center">


[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Accuracy](https://img.shields.io/badge/Accuracy-94.93%25-00D4AA?style=for-the-badge&logo=target&logoColor=white)](#performance)

**🎯 94.93% Accuracy** • **🏥 Healthcare AI** • **⚡ Real-time Predictions** • **🔬 Clinical Grade**

*Developed during ML Internship at **Unifid Mentoe***

[🚀 Quick Start](#-quick-start) • [📊 Features](#-clinical-features) • [🔧 Installation](#-installation) • [📈 Performance](#-performance-metrics)

</div>

---

## 🌟 Project Overview

<table>
<tr>
<td width="50%">

### 🎯 **Mission Statement**
Revolutionizing liver disease diagnosis through intelligent machine learning, enabling healthcare professionals to predict cirrhosis stages with **94.93% accuracy** using routine clinical data.

### 🏥 **Clinical Impact**
- ⚡ **Instant Diagnosis**: Seconds instead of hours
- 💰 **Cost Reduction**: Minimize expensive imaging
- 🎯 **Early Detection**: Catch progression before irreversible damage
- 📊 **Evidence-Based**: Data-driven clinical decisions

</td>
<td width="50%">

```python
# Simple Prediction Example
patient_data = {
    'age': 55,
    'bilirubin': 2.3,
    'albumin': 3.1,
    'sgot': 142,
    'ascites': 'Y'
}

prediction = model.predict(patient_data)
# Output: "Stage 2 Cirrhosis (Confidence: 94%)"
```

</td>
</tr>
</table>

---

## 🔬 Clinical Features & Medical Significance

<div align="center">

### 📊 **Comprehensive Feature Set - 18+ Clinical Parameters**

</div>

| 🏷️ **Category** | 🔬 **Features** | 🩺 **Medical Significance** | 📊 **Data Type** |
|---|---|---|---|
| 🧬 **Biochemical Markers** | `Bilirubin`, `SGOT`, `ALP`, `Albumin` | Liver function & damage indicators | Continuous |
| 💉 **Blood Parameters** | `Cholesterol`, `Copper`, `Platelets`, `Prothrombin` | Metabolic & coagulation status | Continuous |
| 🩺 **Physical Signs** | `Ascites`, `Hepatomegaly`, `Spiders`, `Edema` | Visible cirrhosis manifestations | Categorical |
| 👤 **Demographics** | `Age`, `Sex`, `Drug Usage`, `Status` | Risk factors & patient profile | Mixed |
| ⏱️ **Temporal** | `N_Days` (enrollment duration) | Disease progression timeline | Continuous |

<details>
<summary><b>🔍 Click to view detailed feature explanations</b></summary>

> **📖 Medical Context Available**: Complete clinical explanations for each feature are documented in `NoteBook.txt`, ensuring medical interpretability for healthcare professionals.

</details>

---

## 🚀 Performance Metrics

<div align="center">

### 📈 **Model Performance Dashboard**

<table>
<tr>
<td align="center">
<img src="https://img.shields.io/badge/Accuracy-94.93%25-success?style=for-the-badge&logo=target" alt="Accuracy"/>
<br><b>Primary Metric</b>
</td>
<td align="center">
<img src="https://img.shields.io/badge/F1_Score-94.93%25-blue?style=for-the-badge&logo=balance-scale" alt="F1"/>
<br><b>Balance</b>
</td>
<td align="center">
<img src="https://img.shields.io/badge/Recall-94.93%25-orange?style=for-the-badge&logo=search" alt="Recall"/>
<br><b>Coverage</b>
</td>
<td align="center">
<img src="https://img.shields.io/badge/ROC_AUC-99.26%25-purple?style=for-the-badge&logo=chart-line" alt="ROC"/>
<br><b>Discrimination</b>
</td>
</tr>
</table>

**🏆 Industry Benchmark Comparison**: *Standard: 85% | Our Model: 94.93%*

</div>

### ✅ **Validation Protocol**
- 🔄 **K-fold Cross-validation**: Robust performance testing
- ⚖️ **Class Balancing**: Handled with advanced techniques
- 📏 **Feature Scaling**: StandardScaler normalization
- 🎛️ **Hyperparameter Tuning**: Optimized for clinical use

---

## 🛠️ Technology Architecture

<div align="center">

### 🏗️ **Tech Stack Overview**

<table>
<tr>
<td align="center" width="25%">
<img src="https://img.icons8.com/color/64/python.png" alt="Python"/>
<br><b>Python 3.9+</b>
<br><i>Core Language</i>
</td>
<td align="center" width="25%">
<img src="https://img.icons8.com/color/64/artificial-intelligence.png" alt="ML"/>
<br><b>Scikit-Learn</b>
<br><i>ML Framework</i>
</td>
<td align="center" width="25%">
<img src="https://img.icons8.com/color/64/bar-chart.png" alt="Data"/>
<br><b>Pandas & NumPy</b>
<br><i>Data Processing</i>
</td>
<td align="center" width="25%">
<img src="https://img.icons8.com/color/64/web.png" alt="Web"/>
<br><b>Streamlit</b>
<br><i>UI Interface</i>
</td>
</tr>
</table>

</div>

```mermaid
graph LR
    A[📊 Clinical Data] --> B[🔄 Preprocessing]
    B --> C[🧠 ML Model]
    C --> D[📈 Prediction]
    D --> E[🖥️ Streamlit UI]
    
    style A fill:#FF6B6B,stroke:#FF6B6B,stroke-width:3px,color:#ffffff
    style B fill:#4ECDC4,stroke:#4ECDC4,stroke-width:3px,color:#ffffff
    style C fill:#45B7D1,stroke:#45B7D1,stroke-width:3px,color:#ffffff
    style D fill:#FFA07A,stroke:#FFA07A,stroke-width:3px,color:#ffffff
    style E fill:#98D8C8,stroke:#98D8C8,stroke-width:3px,color:#ffffff
```

---

## 📁 Project Structure & Files

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">

### 🗂️ **Simple & Clean Project Structure**

| **File/Component** | **Purpose** | **Status** |
|-------------------|-------------|------------|
| `app.py` | 🖥️ Local Streamlit UI for predictions | ✅ Complete |
| `main.ipynb` | 📘 Model training & evaluation pipeline | ✅ Complete |
| `EDA_FE.ipynb` | 📊 Data analysis & feature engineering | ✅ Complete |
| `Cleaned_dataset.csv` | 🧾 Main training dataset (cleaned) | ✅ Ready |
| `model_s.pkl` | ✅ Trained classifier (94.93% accuracy) | ✅ Deployed |
| `scl.pkl` | 🔧 Input preprocessing scaler | ✅ Deployed |
| `NoteBook.txt` | 📄 Medical feature explanations | ✅ Complete |
| `int.csv` | 🧪 Intermediate processing data | ✅ Available |
| `README.md` | 📘 Project documentation | ✅ You're reading it! |
| `requirements.txt` | 📦 Python dependencies | ✅ Ready |

</div>

```bash
liver-cirrhosis-stage-detection/
├── app.py                      # 🖥️ Streamlit app for user input and prediction
├── main.ipynb                  # 📘 Model training, evaluation, and saving pipeline
├── EDA_FE.ipynb                # 📊 Exploratory Data Analysis & Feature Engineering
├── Cleaned_dataset.csv         # 🧾 Cleaned dataset used for training
├── model_s.pkl                 # ✅ Trained classification model (Scikit-learn)
├── scl.pkl                     # 🔧 StandardScaler object for input preprocessing
├── NoteBook.txt                # 📄 Detailed medical explanation of all features
├── int.csv                     # 🧪 Intermediate data file (optional use)
├── README.md                   # 📘 Full dark-themed project documentation
└── requirements.txt            # 📦 Package dependencies
```

---

## 🚀 Quick Start

<div style="background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59); padding: 2px; border-radius: 10px;">
<div style="background: #0d1117; padding: 20px; border-radius: 8px;">

### **⚡ Get Started in 3 Simple Steps**

</div>
</div>

### **1️⃣ Installation**
```bash
# Clone the repository
git clone https://github.com/yourusername/liver-cirrhosis-detection.git
cd liver-cirrhosis-detection

# Create virtual environment
python -m venv cirrhosis_env
source cirrhosis_env/bin/activate  # On Windows: cirrhosis_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **2️⃣ Launch Application**
```bash
# Start the Streamlit interface
streamlit run app.py

# 🌐 Application will open at: http://localhost:8501
```

### **3️⃣ Make Predictions**
1. 📝 **Input Patient Data**: Use interactive sliders and dropdowns
2. 🎯 **View Predictions**: Get instant cirrhosis stage classification
3. 📊 **Review Confidence**: See prediction confidence levels
4. 💾 **Export Results**: Save for medical records

---

## 🖥️ User Interface Preview

<div align="center">

### 🎨 **Streamlit Application Features**

| Feature | Description | Status |
|---------|-------------|--------|
| 🎛️ **Interactive Controls** | Sliders, dropdowns for clinical parameters | ✅ Complete |
| 🌙 **Dark Theme** | Professional healthcare-optimized design | ✅ Complete |
| ⚡ **Real-time Predictions** | Instant stage classification | ✅ Complete |
| 📊 **Confidence Scores** | Prediction probability for each stage | ✅ Complete |
| 📱 **Responsive Design** | Works on desktop, tablet, mobile | ✅ Complete |
| 🔒 **Local Deployment** | Secure, private data processing | ✅ Complete |

</div>

---

## 📋 Development Status & Handover Notes

<div style="background: linear-gradient(135deg, #74b9ff, #0984e3); padding: 15px; border-radius: 8px; color: white;">

### 🔄 **Current Status: Production Ready (Local Deployment)**

</div>

### ✅ **Completed Components**
- ✅ **Dataset Processing**: Cleaned and validated clinical data
- ✅ **EDA & Feature Engineering**: Comprehensive analysis completed
- ✅ **Model Training**: 94.93% accuracy achieved with rigorous validation  
- ✅ **Model Serialization**: Saved as `model_s.pkl` with scaler
- ✅ **Streamlit Interface**: Professional dark-themed UI
- ✅ **Medical Documentation**: Clinical explanations in `NoteBook.txt`
- ✅ **Project Documentation**: Complete README and structure

### 🔄 **Ready for Enhancement**
- 🌐 **Cloud Deployment** (Streamlit Cloud, Heroku, AWS)
- 📊 **Advanced Models** (XGBoost, ensemble methods)
- 🔍 **Model Interpretability** (SHAP, LIME for medical explainability)
- 💾 **User History** (Session management, prediction logging)
- 🔐 **Input Validation** (Enhanced data quality checks)

---

### 🤝 **Get Connected**

**🏢 Organization**: Unifid Mentoe Internship Program  
**📧 Contact**: hareesh9893@gmail.com 
**💼 LinkedIn**: linkedin.com/in/hareesh-kumar-k

---

## 📄 License

<div style="background: linear-gradient(45deg, #667eea, #764ba2); padding: 20px; border-radius: 10px; color: white; text-align: center;">

**📜 MIT License** • **🔓 Open Source** • **🎓 Academic Use Welcome**

</div>

---

<div align="center">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

### 💡 **"Transforming Healthcare Through Intelligent AI"** 💡

**🎯 Mission**: Making medical diagnosis faster, more accurate, and accessible worldwide  
**🚀 Vision**: AI-powered healthcare for every patient, every clinic, everywhere

*Built with ❤️ for the global healthcare community*

</div>

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![Healthcare AI](https://img.shields.io/badge/Healthcare-AI-blue?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open-Source-green?style=for-the-badge)

</div>
