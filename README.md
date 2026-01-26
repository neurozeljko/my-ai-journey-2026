# Google Cloud AI & Governance Portfolio 2026

![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-blue) ![Generative AI](https://img.shields.io/badge/GenAI-Agents_%26_RAG-purple) ![Security](https://img.shields.io/badge/AI_Security-Model_Armor-red) ![Status](https://img.shields.io/badge/Status-Production_Ready-green)

This repository serves as a technical portfolio demonstrating advanced implementations of **Generative AI**, **Multimodal Architectures**, and **AI Governance** within the Google Cloud ecosystem. 

It represents a rigorous transition from standard ML models to **Agentic Workflows** and **Secure Enterprise Systems**, specifically aligned with **IAPP AIGP** (AI Governance Professional) standards.

---

## 🏆 Verified Competencies & Badges (Jan 2026)
*Intensive specialization track completed via Google Cloud Skills Boost.*

### 🛡️ AI Governance & Security Specialization
*Critical for enterprise compliance and safe AI deployment.*
* **Security:** Model Armor: Securing AI Deployments | Introduction to Security in the World of AI
* **Responsible AI:** Privacy & Safety | Fairness & Bias | Interpretability & Transparency
* **Strategy:** Responsible AI for Digital Leaders | Applying AI Principles

### 🤖 Generative AI & Agentic Workflows
*Focus on building autonomous systems using Vertex AI Agent Builder.*
* **Agents:** Gen AI Agents: Transform Your Organization | Beyond the Chatbot
* **Applications:** Gen AI Apps: Transform Your Work | Prompt Design in Vertex AI
* **Core Models:** Introduction to Large Language Models | Introduction to Generative AI

### ⚙️ MLOps & Technical Architecture
*Backend engineering and model lifecycle management.*
* **MLOps:** MLOps for Generative AI | Model Evaluation with Vertex AI
* **RAG & Search:** Vector Search and Embeddings | Inspect Rich Documents with Multimodal RAG
* **Deep Learning:** Transformer Models & BERT | Encoder-Decoder Architecture | Attention Mechanism | Image Captioning & Generation

---

## 🤖 Agentic Workflows & Conversational AI
*Focus: Vertex AI Agent Builder, Generative Playbooks, and NLU.*

### ✈️ 1. Intelligent Flight Booking Agent
* **Folder:** `DialogFlowCX_Flight_Booker/`
* **Tech Stack:** Google Cloud Vertex AI Agent Builder (formerly Dialogflow CX).
* **Objective:** Building a stateful conversational agent capable of handling complex travel logistics.
* **Key Implementation:** * **Generative Playbooks:** Utilizing LLMs to interpret user intent and manage conversation flow dynamically, replacing rigid decision trees.
    * **Hybrid NLU:** Combining standard intent classification with generative fallbacks for robust user understanding.
    * **State Management:** Handling multi-turn conversations to extract entities (dates, locations) effectively.

---

## 🏗️ Core Architecture & Governance
*Focus: AI Safety, Compliance (GDPR/EU AI Act), and Privacy-Preserving ML.*

### 🛡️ 2. Enterprise AI Safety & Guardrails
* **File:** `04_enterprise_safety_guardrails.py`
* **Objective:** Implementing rigid safety barriers for LLMs in production environments.
* **Key Implementation:** Configuration of `SafetySettings` with granular thresholds (Hate Speech, Dangerous Content) to ensure corporate policy compliance. Crucial for mitigating risks in deployment.

### 🔒 3. Differential Privacy in Machine Learning
* **File:** `05_differential_privacy_model.py`
* **Objective:** Training ML models with mathematical guarantees of user privacy.
* **Key Implementation:** Utilizing **TensorFlow Privacy** to implement `DPKerasSGDOptimizer` and calculating privacy budgets (Epsilon), ensuring models do not memorize sensitive user data.

### 🧠 4. Multimodal RAG Pipeline
* **File:** `03_multimodal_rag_pipeline.py`
* **Objective:** Next-generation information retrieval understanding both text and images.
* **Key Implementation:** Generating multimodal embeddings (`MultiModalEmbeddingModel`) and simulating vector retrieval to power context-aware Generative AI applications.

---

## 🚀 Applied Generative AI Solutions
*Focus: Visual Reasoning, Structured Data Extraction, and Process Automation.*

### 🛒 5. Retail Recommendation Engine
* **File:** `02_retail_recommendation_engine.py`
* **Objective:** Automating visual inventory analysis for personalized customer recommendations.
* **Tech Stack:** Gemini Pro Vision + Structured JSON Output.
* **Outcome:** Converts an image of a room into a structured list of furniture recommendations based on design style analysis.

### 📄 6. Multimodal Document Analysis (OCR++)
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

### Note on Agent Import
The folder `DialogFlowCX_Flight_Booker` contains the exported agent structure. To test:
1. Go to **Google Cloud Console > Agent Builder**.
2. Create a new App.
3. Select **Restore** and upload the contents of the folder.
