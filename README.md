# Google Cloud AI & Governance Portfolio 2026

![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-yellow) ![Dialogflow CX](https://img.shields.io/badge/Dialogflow-CX-orange) ![Status](https://img.shields.io/badge/Status-Production_Ready-green)

This repository serves as a technical portfolio demonstrating advanced implementations of **Generative AI**, **Multimodal Architectures**, and **AI Governance** within the Google Cloud ecosystem. 

It represents a transition from standard ML models to **Agentic Workflows** and **Secure Enterprise Systems**, specifically aligned with **IAPP AIGP** (AI Governance Professional) standards.

---

## Agentic Workflows & Conversational AI
*Focus: Vertex AI Agent Builder, Generative Playbooks, and NLU.*

### 1. Intelligent Flight Booking Agent
* **Folder:** `DialogFlowCX_Flight_Booker/`
* **Tech Stack:** Google Cloud Vertex AI Agent Builder (formerly Dialogflow CX).
* **Objective:** Building a stateful conversational agent capable of handling complex travel logistics.
* **Key Implementation:** * **Generative Playbooks:** Utilizing LLMs to interpret user intent and manage conversation flow dynamically, replacing rigid decision trees.
    * **Hybrid NLU:** Combining standard intent classification with generative fallbacks for robust user understanding.
    * **State Management:** Handling multi-turn conversations to extract entities (dates, locations) effectively.

---

## Core Architecture & Governance
*Focus: AI Safety, Compliance (GDPR/EU AI Act), and Privacy-Preserving ML.*

### 2. Enterprise AI Safety & Guardrails
* **File:** `04_enterprise_safety_guardrails.py`
* **Objective:** Implementing rigid safety barriers for LLMs in production environments.
* **Key Implementation:** Configuration of `SafetySettings` with granular thresholds (Hate Speech, Dangerous Content) to ensure corporate policy compliance. Crucial for mitigating risks in deployment.

### 3. Differential Privacy in Machine Learning
* **File:** `05_differential_privacy_model.py`
* **Objective:** Training ML models with mathematical guarantees of user privacy.
* **Key Implementation:** Utilizing **TensorFlow Privacy** to implement `DPKerasSGDOptimizer` and calculating privacy budgets (Epsilon), ensuring models do not memorize sensitive user data.

### 4. Multimodal RAG Pipeline
* **File:** `03_multimodal_rag_pipeline.py`
* **Objective:** Next-generation information retrieval understanding both text and images.
* **Key Implementation:** Generating multimodal embeddings (`MultiModalEmbeddingModel`) and simulating vector retrieval to power context-aware Generative AI applications.

---

## Applied Generative AI Solutions
*Focus: Visual Reasoning, Structured Data Extraction, and Process Automation.*

### 5. Retail Recommendation Engine
* **File:** `02_retail_recommendation_engine.py`
* **Objective:** Automating visual inventory analysis for personalized customer recommendations.
* **Tech Stack:** Gemini Pro Vision + Structured JSON Output.
* **Outcome:** Converts an image of a room into a structured list of furniture recommendations based on design style analysis.

### 6. Multimodal Document Analysis (OCR++)
* **File:** `01_gemini_multimodal_core.py` & `flight_schedule_analysis
