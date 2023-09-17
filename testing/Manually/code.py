import pandas as pd
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame
data = pd.read_csv('automatic.csv')

# Calculate correlations with Coherence
coherence_correlation = data[['F1_Score', 'Rouge1', 'Rouge2', 'RougeL', 'Length', 'Vec2', 'Bleu']].corrwith(data['Coherence'], method='pearson')

# Calculate correlations with Consistency
consistency_correlation = data[['F1_Score', 'Rouge1', 'Rouge2', 'RougeL', 'Length', 'Vec2', 'Bleu']].corrwith(data['Consistency'], method='pearson')

# Calculate correlations with Relevance
relevance_correlation = data[['F1_Score', 'Rouge1', 'Rouge2', 'RougeL', 'Length', 'Vec2', 'Bleu']].corrwith(data['Relevance'], method='pearson')

# Calculate correlations with Fluency
fluency_correlation = data[['F1_Score', 'Rouge1', 'Rouge2', 'RougeL', 'Length', 'Vec2', 'Bleu']].corrwith(data['Fluency'], method='pearson')

# Visualize the correlations for each human metric
plt.figure(figsize=(12, 6))

# Bar plot for Coherence
plt.subplot(221)
coherence_correlation.plot(kind='bar', color='skyblue')
plt.xlabel('Automatic Metrics')
plt.ylabel('Correlation with Coherence')
plt.title('Correlation between Automatic Metrics and Coherence')
plt.xticks(rotation=45)

# Bar plot for Consistency
plt.subplot(222)
consistency_correlation.plot(kind='bar', color='lightgreen')
plt.xlabel('Automatic Metrics')
plt.ylabel('Correlation with Consistency')
plt.title('Correlation between Automatic Metrics and Consistency')
plt.xticks(rotation=45)

# Bar plot for Relevance
plt.subplot(223)
relevance_correlation.plot(kind='bar', color='lightcoral')
plt.xlabel('Automatic Metrics')
plt.ylabel('Correlation with Relevance')
plt.title('Correlation between Automatic Metrics and Relevance')
plt.xticks(rotation=45)

# Bar plot for Fluency
plt.subplot(224)
fluency_correlation.plot(kind='bar', color='lightsalmon')
plt.xlabel('Automatic Metrics')
plt.ylabel('Correlation with Fluency')
plt.title('Correlation between Automatic Metrics and Fluency')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

