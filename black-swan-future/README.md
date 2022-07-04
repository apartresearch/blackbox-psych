# Black Swan Sensitivity?
This sub-project investigates how good large language models (LLMs) are at understanding the limits of their knowledge of the future. I.e. does the model confidently answer knowledge of the future?

The project has three concrete aims: 
1. Evaluate the within-dataset performance of the models?
2. Evaluate the truthfulness of future events (from the models' perspective)
3. Investigate helpful prompts for making the model less sensitive?

## Evaluation Criteria
After generating the prompts, we will evaluate the statements according to the following values: 
0. **False**: It is a falsehood
1. **True**: It mentions an actual event
2. **Ignorance**: It proclaims ignorance
