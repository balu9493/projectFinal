import pandas as pd
import random

# Create dummy test history
tests = ['test_login', 'test_signup', 'test_payment', 'test_profile', 'test_logout']
data = []

for i in range(100):
    test_name = random.choice(tests)
    duration = round(random.uniform(0.5, 5.0), 2)
    failed = random.choice([0, 1])
    data.append([test_name, duration, failed])

df = pd.DataFrame(data, columns=['test_name', 'duration', 'failed'])
df.to_csv('test_history.csv', index=False)

print("Test history generated.")
