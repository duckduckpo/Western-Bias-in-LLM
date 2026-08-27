# LLM Cultural Bias Analyzer

This repository contains an NLP data pipeline built to analyze the cultural alignment of Large Language Models. By querying LLMs with global survey questions, this project measures whether models default to Western (individualist/secular) or Non-Western (collectivist/traditional) values. 

Designed as a 3rd-year B.Tech Computer Networks project, this research explores how centralized network infrastructure and globalized data scraping can homogenize AI behavior, standardizing localized cultures across the web regardless of the model's geographic origin.

## Key Findings
* **The 5x Ratio:** Both GPT-20B and Qwen chose Western-aligned responses roughly 4 to 5 times more often than Non-Western responses.
* **High Evasion Rates:** Over 50% of the time, both models defaulted to neutral or middle-ground answers to avoid taking a hard stance on cultural issues.
* **Geographic Independence:** Qwen (developed in a non-Western region) displayed a slightly higher Western bias than GPT-20B, indicating that global training data completely overrides regional origins.

## Repository Structure
* `data/`: Raw global opinion CSVs, filtered prompt text files, the independent scoring rubric, and JSON model outputs.
* `scripts/`: Python scripts for data extraction, API querying (Groq/OpenAI compatible), and automated grading.
* `visualizations/`: Generated Matplotlib pie charts comparing model alignments.

## Setup & Execution
1. Install dependencies: `pip install pandas openai matplotlib`
2. Run `scripts/data_formatter.py` to extract questions from the CSV.
3. Run `scripts/llm_query.py` to generate model responses via API.
4. Run `scripts/pie_chart_maker.py` to plot the bias distribution.
