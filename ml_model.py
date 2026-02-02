from sklearn.linear_model import LogisticRegression
import numpy as np

model = LogisticRegression()

X = np.array([
    [0.9, 5],
    [0.4, 1],
    [0.7, 3]
])
y = np.array([1, 0, 1])

model.fit(X, y)

def predict_acceptance(skill_match, experience):
    return model.predict_proba([[skill_match, experience]])[0][1]
