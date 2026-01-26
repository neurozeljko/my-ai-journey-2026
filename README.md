# Google Cloud AI & Governance Portfolio 2026

This repository showcases advanced implementations of **Agentic AI**, **Multimodal Architectures**, and **AI Governance** utilizing the Google Cloud Vertex AI stack. It represents a journey from foundational generative models to secure, enterprise-grade AI systems.

**Primary Tech Stack:** Google Vertex AI (Gemini Pro/Vision), TensorFlow Privacy, Python, Vector Search.

---

## 📂 Core Architecture & Governance
*Focus: AI Safety, Compliance (AIGP), and Privacy-Preserving ML.*

### 1. Enterprise AI Safety & Guardrails
* **File:** `04_enterprise_safety_guardrails.py`
* **Objective:** Implementing rigid safety barriers for LLMs in production environments.
* **Key Implementation:** Configuration of `SafetySettings` with granular thresholds (Hate Speech, Harassment) to align with corporate risk policies.

### 2. Differential Privacy in Machine Learning
* **File:** `05_differential_privacy_model.py`
* **Objective:** Training ML models with mathematical guarantees of user privacy (GDPR/CCPA compliance).
* **Key Implementation:** Utilizing **TensorFlow Privacy** to implement `DPKerasSGDOptimizer` and calculating privacy budgets (Epsilon).

---

## 📂 Applied Generative AI Solutions
*Focus: Multimodal Reasoning and Business Process Automation.*

### 3. Multimodal RAG Pipeline
* **File:** `03_multimodal_rag_pipeline.py`
* **Objective:** Building next-gen retrieval systems that understand both text and images.
* **Key Implementation:** Generating multimodal embeddings and simulating vector retrieval for context-aware generation using Gemini Pro Vision.

### 4. Retail Recommendation Engine
* **File:** `02_retail_recommendation_engine.py`
* **Objective:** Automating visual inventory analysis for personalized customer recommendations.
* **Key Implementation:** Zero-shot image reasoning to analyze interior design styles and generate structured JSON outputs for inventory systems.

### 5. Multimodal Document Analysis
* **File:** `01_gemini_multimodal_core.py` (and `flight_schedule_analysis.py`)
* **Objective:** Extracting structured data from complex visual documents (e.g., flight timetables).
* **Key Implementation:** Multimodal prompting to convert unstructured visual data into machine-readable formats.

---

## 📂 Industry Specific Use Cases
*Practical applications for Insurance and Marketing sectors.*

* **Insurance Automation:** (`insurance_risk_assessment.py`) - Automating risk factor identification from unstructured claims.
* **Creative Content Factory:** (`challenge_tagline_generator.py`) - Generating marketing assets at scale using visual context.

---

## 🛠️ Setup & Usage

1. **Install Dependencies:**
   ```bash
   pip install google-cloud-aiplatform tensorflow-privacy
