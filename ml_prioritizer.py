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

# Save result
prioritized_tests.to_csv('prioritized_tests.csv', index=False)
print("Prioritization complete.\n")
print(prioritized_tests.head())

# Save top 3 test names to a file
top_tests = prioritized_tests['test_name'].head(3)
top_tests.to_csv('top_tests.txt', index=False, header=False)

