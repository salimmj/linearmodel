from sklearn.model_selection import cross_val_score

"""
    Classifier Class
    Trains a linear model for each feature on the provided trained model

    PS: This class will later be renamed to LinearModel and will support both
        regression models and linear classifiers for both continuous and binary
        features
"""

class Classifier:

    """
        Classifier constructor
        @param model - Model to train on
        @param feature_list - List of features to train on
    """
    def __init__(self, model, feature_list):

        self.model = model
        self.feature_list = feature_list

        self.trained_classifiers = [LinearClassifier(model, impulse_feature) for impulse_feature in self.feature_list]


class LinearClassifier:

    """
        LinearClassifier constructor
        @param model - Model to train on
        @param impulse_feature - Impulse feature to train on
    """
    def __init__(self, model, impulse_feature):

        self.model = model
        self.impulse_feature = impulse_feature

        self.trained_linear_classifier = self.train()

    def train(self):


        scores = cross_val_score(clf, iris.data, iris.target, cv=5)


        pass
