## Overview

This repository houses a comprehensive approach to developing an AI assistant tailored for K12 STEM education, with a strong emphasis on culturally responsive teaching practices. Our project spans several interconnected components: the generation of a culturally responsive dataset, prompt engineering for an AI assistant, and the implementation of a Retrieval-Augmented Generation (RAG) model using PostgreSQL and pgvector.

### Repository Structure

1. **Dataset Preparation**
   - Focuses on generating a culturally responsive dataset for fine-tuning a Large Language Model (LLM).
   - Techniques: PDF text extraction, segmentation, and Q&A generation.
   - Tools: `UnstructuredPDFLoader`, `OllamaFunctions` LLM model.
   - Output: JSON file with Q&A pairs that reflect diverse voices and inclusive practices.

2. **Prompt Engineering**
   - Details the creation and refinement of prompts to develop an AI assistant that supports culturally relevant K12 STEM education.
   - Techniques: System prompt design, iterative feedback, and testing.
   - Tools: Llama 3.1 model on the Ollama platform.
   - Focus: Inclusivity, engagement, cultural relevance, and continuous improvement.

3. **RAG Implementation**
   - Implements a Retrieval-Augmented Generation (RAG) model that utilizes PostgreSQL and pgvector for vector embedding storage.
   - Techniques: Document chunking, vector embedding generation, cosine similarity retrieval.
   - Tools: PostgreSQL with pgvector, LLaMA-3 model.
   - Output: Contextually accurate and relevant responses to user queries based on retrieved text chunks.

---

## 1. Objective and Scope

**Objective**: To develop an AI assistant and tools that help educators create culturally relevant, engaging, and inclusive lesson plans for K12 STEM education.

**Scope**:
- Design and test initial prompts for culturally responsive AI.
- Generate a culturally responsive dataset for fine-tuning.
- Implement and refine a RAG model for efficient information retrieval and augmentation.

## 2. Detailed Components

### 2.1 Dataset Preparation
- **Objective**: Generate a dataset that reflects diverse voices and inclusive practices in STEM education.
- **Techniques**:
  - **Text Extraction**: Extract meaningful text segments from PDFs using `UnstructuredPDFLoader`.
  - **Text Segmentation**: Apply fixed-size and sliding window segmentation to maintain context and structure.
  - **Q&A Generation**: Use `OllamaFunctions` to create Q&A pairs focused on culturally responsive teaching.
  - **Data Cleaning and Export**: Structure the dataset into JSON, with options to convert to CSV for easier integration.

### 2.2 Prompt Engineering
- **Objective**: Design prompts that guide the AI assistant to generate culturally relevant lesson plans.
- **Approach**:
  - **System Prompt**: Emphasizes inclusivity, engagement, and cultural relevance.
  - **Testing and Feedback**: Continuous refinement based on feedback to improve cultural nuance handling and engagement.
- **Enhancements**:
  - Updated prompts for clarity and specificity.
  - Revised structures for broader cultural relevance.
  - Ongoing evaluation to identify and close gaps.

### 2.3 RAG Model Implementation
- **Objective**: Implement a RAG model using PostgreSQL and pgvector for efficient retrieval of contextually relevant information.
- **Techniques**:
  - **Vector Embedding Generation**: Extract and store embeddings in PostgreSQL with pgvector.
  - **Cosine Similarity Retrieval**: Retrieve the most relevant text chunks based on user queries.
  - **Augmentation**: Use retrieved chunks to provide contextually accurate responses with the LLaMA-3 model.

---

## 3. Future Plans

1. **Continuous Feedback Loop**: Engage with educators and experts for ongoing review and improvement.
2. **Fine-Tuning**: Create and refine a dataset for further fine-tuning based on identified gaps.
3. **Expanded Testing**: Continue testing and documenting results to close remaining gaps.
