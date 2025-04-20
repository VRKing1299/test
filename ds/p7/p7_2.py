from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Build decision tree model
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Predict
y_pred_tree = tree_model.predict(X_test)

# Evaluate
print("Accuracy (Decision Tree):", accuracy_score(y_test, y_pred_tree))

# Visualize the tree
plt.figure(figsize=(10,6))
tree.plot_tree(tree_model, feature_names=['Marks', 'Attendance'], class_names=['Fail', 'Pass'], filled=True)
plt.title("Decision Tree")
plt.show()
