
from sklearn.tree import DecisionTreeClassifier

X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[3, 3]])

print("Predicted Class:", prediction[0])
