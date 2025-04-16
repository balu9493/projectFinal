# Continuous Improvement in DevOps: Implementing Machine Learning for Test Prioritization

This project demonstrates how to enhance a standard DevOps Continuous Integration (CI) pipeline by integrating **Machine Learning (ML)** for intelligent test case prioritization.

---

## 🚀 Project Overview

In large-scale software development, running the entire test suite after every code change can be time-consuming. This project applies an ML-based approach to predict the likelihood of failure for each test case based on historical test data — and **automatically prioritizes tests** so the most critical ones run first.

---

## 🔥 How the Jenkins Pipeline Works

The Jenkins pipeline follows this step-by-step flow:

1️⃣ **Clone Repository**  
   Pulls the latest code from GitHub.

2️⃣ **Install Dependencies**  
   Uses `pip` to install all Python packages from `requirements.txt`.

3️⃣ **Generate Test Data**  
   The script `generate_test_data.py` simulates test history by generating random test execution records (`test_history.csv`).

4️⃣ **Prioritize Tests (ML)**  
   The `ml_prioritizer.py` script:
   - Trains a `RandomForestClassifier` on historical test data.
   - Predicts failure probability for each test.
   - Generates a ranked list (`prioritized_tests.csv`).
   - Saves the top N tests to `top_tests.txt`.

5️⃣ **Run Prioritized Tests**  
   Jenkins reads `top_tests.txt` and executes only the selected test cases, reducing time while maintaining focus on the most failure-prone tests.

6️⃣ **Generate Report** *(optional)*  
   Displays the full prioritized test list after each build, providing visibility for developers and testers.

---

## 💡 Why Use Machine Learning for Test Prioritization?

- 🔍 **Smarter Testing:**  
   ML predicts which tests are likely to fail based on past patterns, letting you detect bugs faster.

- ⚡ **Faster Feedback:**  
   Reduces build times by focusing on the most important tests first, especially useful in large projects.

- 📈 **Adaptive Learning:**  
   The model retrains automatically on every pipeline run as the test history evolves, making your pipeline intelligent and self-improving.

---

## 📂 Outputs

- `test_history.csv` — Generated test history.
- `prioritized_tests.csv` — Sorted list of all tests with predicted failure probabilities.
- `top_tests.txt` — List of the top N tests to be executed.

---

✅ **Result:**  
This system creates an automated, intelligent testing flow that improves with every build — a perfect demonstration of Continuous Improvement in DevOps!

---

