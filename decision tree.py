from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

def train_decision_tree_and_visualize():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Create a DecisionTreeClassifier instance
    clf = DecisionTreeClassifier()

    # Fit the classifier on the data
    clf.fit(X, y)

    # Export the Decision Tree to a Graphviz file
    export_graphviz(clf, out_file='tree.dot', feature_names=iris.feature_names, class_names=iris.target_names, filled=True)

    # Convert the Graphviz file to a PNG image using Graphviz
    with open('tree.dot') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph).render('decision_tree', format='png', cleanup=True)

# Call the function to train the decision tree and visualize it
train_decision_tree_and_visualize()
