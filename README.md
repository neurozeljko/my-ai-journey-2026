# Google Cloud AI & Governance Portfolio 2026

![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-yellow) ![TensorFlow](https://img.shields.io/badge/TensorFlow-Privacy-orange) ![Status](https://img.shields.io/badge/Status-Production_Ready-green)

This repository serves as a technical portfolio demonstrating advanced implementations of **Generative AI**, **Multimodal Architectures**, and **AI Governance** within the Google Cloud ecosystem. 

It represents a transition from standard ML models to **Agentic Workflows** and **Secure Enterprise Systems**, specifically aligned with **IAPP AIGP** (AI Governance Professional) standards.

---

## 🏗️ Core Architecture & Governance
*Focus: AI Safety, Compliance (GDPR/EU AI Act), and Privacy-Preserving ML.*

### 🛡️ 1. Enterprise AI Safety & Guardrails
* **File:** `04_enterprise_safety_guardrails.py`
* **Objective:** Implementing rigid safety barriers for LLMs in production environments.
* **Key Implementation:** Configuration of `SafetySettings` with granular thresholds (Hate Speech, Dangerous Content) to ensure corporate policy compliance. Crucial for mitigating risks in deployment.

### 🔒 2. Differential Privacy in Machine Learning
* **File:** `05_differential_privacy_model.py`
* **Objective:** Training ML models with mathematical guarantees of user privacy.
* **Key Implementation:** Utilizing **TensorFlow Privacy** to implement `DPKerasSGDOptimizer` and calculating privacy budgets (Epsilon), ensuring models do not memorize sensitive user data.

### 🧠 3. Multimodal RAG Pipeline
* **File:** `03_multimodal_rag_pipeline.py`
* **Objective:** Next-generation information retrieval understanding both text and images.
* **Key Implementation:** Generating multimodal embeddings (`MultiModalEmbeddingModel`) and simulating vector retrieval to power context-aware Generative AI applications.

---

## 🚀 Applied Generative AI Solutions
*Focus: Visual Reasoning, Structured Data Extraction, and Process Automation.*

### 🛒 4. Retail Recommendation Engine
* **File:** `02_retail_recommendation_engine.py`
* **Objective:** Automating visual inventory analysis for personalized customer recommendations.
* **Tech Stack:** Gemini Pro Vision + Structured JSON Output.
* **Outcome:** Converts an image of a room into a structured list of furniture recommendations based on design style analysis.

### ✈️ 5. Multimodal Document Analysis (OCR++)
* **File:** `01_gemini_multimodal_core.py` & `flight_schedule_analysis.py`
* **Objective:** Extracting structured data from complex visual documents (e.g., flight timetables).
* **Outcome:** Solves the "unstructured data" problem by converting visual tables into machine-readable JSON formats for backend integration.

---

## 💼 Industry Specific Use Cases

### 🏥 Insurance Risk Assessment
* **File:** `insurance_risk_assessment.py`
* **Domain:** FinTech / InsurTech.
* **Function:** Analyzes unstructured insurance claim text to extract entities (Policy #, Date) and calculate a "Risk Score" for fraud detection.

### 🎨 Creative Content Factory
* **File:** `challenge_tagline_generator.py`
* **Domain:** Marketing & AdTech.
* **Function:** Generates targeted marketing assets (taglines, hashtags) based on product images and brand tone analysis.

---

## 🛠️ Setup & Execution

### Prerequisites
* Google Cloud Project with Vertex AI API enabled.
* Python 3.9+

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/google-cloud-ai-portfolio-2026.git](https://github.com/YOUR_USERNAME/google-cloud-ai-portfolio-2026.git)
