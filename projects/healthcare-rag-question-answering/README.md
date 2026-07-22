# Healthcare RAG Question Answering

## Overview

GenAI and NLP project that builds a retrieval-augmented question answering workflow for healthcare-style questions. The notebook explores document loading, chunking, embeddings, retrieval, prompt design, and LLM response generation.

## Business Problem

Healthcare professionals often need fast access to reliable information across large bodies of medical text. A RAG workflow can retrieve relevant context and use an LLM to produce more grounded answers than prompting alone.

## Dataset

- Local dataset file: none included in the current project folder
- Main artifact: notebook-based RAG workflow
- Report: `reports/healthcare_rag_question_answering.pdf`

## Approach

- Set up text processing and retrieval dependencies
- Loaded and chunked source text
- Generated embeddings
- Built a retriever-backed response function
- Tested medical question-answering prompts
- Refined the prompt template for more grounded and clinically careful answers

## RAG Pipeline

- Document processing: text chunking
- Retrieval: vector similarity search
- Generation: LLM response using retrieved context
- Prompting: healthcare-focused answer guidelines
- Evaluation: qualitative comparison of responses to test questions

## Notes

This project should be reviewed as a GenAI workflow notebook. Before public deployment, add clear source-document attribution, safety disclaimers, and evaluation examples.

## Files

```text
healthcare-rag-question-answering/
  README.md
  notebooks/healthcare_rag_question_answering.ipynb
  reports/healthcare_rag_question_answering.pdf
  data/
  models/
  assets/screenshots/
```
