# Intelligent Candidate Discovery & Ranking Engine

## Overview

This project was developed for the India Runs – Data & AI Challenge.

The goal is to build an explainable candidate ranking engine that identifies the most suitable candidates for a given job description using career history, experience, technical skills, and recruiter interaction signals.

---

## Problem Statement

Traditional recruitment systems rely heavily on keyword matching, often missing highly relevant candidates.

Our solution ranks candidates using multiple dimensions:

* Career relevance
* Experience fit
* Skill assessment performance
* Recruiter interaction signals
* Explainable scoring

---

## Dataset

The dataset contains approximately 100,000 candidate profiles with:

* Career history
* Skills
* Education
* Certifications
* Languages
* Redrob behavioral signals

---

## Architecture

Job Description
→ Feature Extraction
→ Career Relevance Analysis
→ Experience Matching
→ Skill Assessment Evaluation
→ Redrob Signal Analysis
→ Weighted Ranking Engine
→ Top Candidate Ranking
→ Explainable Output

---

## Ranking Factors

| Factor           | Weight |
| ---------------- | ------ |
| Career Relevance | 55%    |
| Experience Fit   | 20%    |
| Redrob Signals   | 10%    |
| Skill Assessment | 5%     |
| Title Relevance  | 8%     |
| Certifications   | 2%     |

---

## Features

* Candidate ranking
* Explainable recommendations
* Experience matching
* Skill assessment integration
* Behavioral signal analysis
* CSV export

---

## Output

The system produces:

* Ranked candidate list
* Candidate scores
* Explainable reasoning
* Submission-ready CSV files

---

## Tech Stack

* Python
* Pandas
* JSONL Processing
* Feature Engineering
* Ranking Algorithms

---

## Future Improvements

* Semantic retrieval using embeddings
* Learning-to-rank models
* Transformer-based reranking
* Adaptive weighting strategies
