import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load historical test data
df = pd.read_csv('test_history.csv')

# Encode test names as integers
df['test_id'] = df['test_name'].astype('category').cat.codes

# Features and label
X = df[['test_id', 'duration']]
y = df['failed']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict probabilities of failure (simulate prioritization)
df['priority_score'] = model.predict_proba(X)[:, 1]

# Sort tests by priority
prioritized_tests = df[['test_name', 'priority_score']].drop_duplicates().sort_values(by='priority_score', ascending=False)

# Filter: keep only test files that actually exist
existing_tests = []
for test in prioritized_tests['test_name']:
    if os.path.exists(f'tests/{test}.py'):
        existing_tests.append(test)

# Save valid top 3 tests to a file
with open('top_tests.txt', 'w') as f:
    for test in existing_tests[:3]:
        f.write(f"{test}\n")

# Save full prioritized list (optional — for reference/debugging)
prioritized_tests.to_csv('prioritized_tests.csv', index=False)

print("Prioritization complete.\n")
print(pd.DataFrame({'test_name': existing_tests[:3]}))
