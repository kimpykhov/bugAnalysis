# Predicting Bug Resolution Time

This project explores whether historical bug metadata can be used to estimate how long a bug will take to be resolved.

Using structured attributes such as priority, severity, component, and assignee, the goal is to build a baseline ML model that predicts bug resolution time (or classifies bugs by expected resolution speed) and to analyze the limits of such predictions in a noisy, real-world setting.

- Model estimates expected resolution time based on historical patterns and does not provide exact predictions.
- The model does not account for changes in priority, scope, or assignee after bug creation.
- External dependencies (team load, releases, organizational factors) are not represented in the data.
- Predictions are valid only within the distribution of historical data and may degrade for unseen components or workflows.

## All dataset in the project is synthetic.