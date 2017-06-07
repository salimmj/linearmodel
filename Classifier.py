from sklearn.model_selection import cross_val_score
import numpy as np

"""
    Classifier Class
    Trains a linear model for each feature on the provided trained model

    PS: This class will later be renamed to LinearModel and will support both
        regression models and linear classifiers for both continuous and binary
        features

        "feature1", fea

        features.feature1(w_i)
"""

class Classifier:

    """
        Classifier constructor
        @param model - Model to train on
        @param feature_list - List of features to train on
    """
    def __init__(self, model, feature_list, n_cells):

        self.model = model
        self.feature_list = feature_list
        self.n_cells = n_cells

        # list of cells. each cell is a list of features. each feature is a linear classifier
        self.trained_classifiers = [[LinearClassifier(model.get_cell(cell), impulse_feature) for impulse_feature in self.feature_list] for
                                    cell in range(n_cells)]

        self.scores = np.array([ [ feature.score for feature in cell_clf ] for cell_clf in self.trained_classifiers ])



class LinearClassifier:

    """
        LinearClassifier constructor
        @param model - Model to train on
        @param impulse_feature - Impulse feature to train on
    """
    def __init__(self, model, impulse_feature):

        self.model = model
        self.impulse_feature = impulse_feature

        self.score = self.get_score()

    def get_score(self):


        scores = cross_val_score


        pass
