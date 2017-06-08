from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
import numpy as np

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
        @param model_data - Model to train on, it is a data cube of the form 2 x cells x features x time_steps
        @param feature_list - List of features to train on
    """
    def __init__(self, model_data, feature_list, n_cells):

        self.model_data = model_data
        self.feature_list = feature_list
        self.n_cells = n_cells

        # list of cells. each cell is a list of features. each feature is a linear classifier
        self.trained_classifiers = [[LinearClassifier(self.model_data[0][cell][i], self.model_data[1][cell][i], impulse_feature)
                                     for i, impulse_feature in enumerate(self.feature_list)] for cell in range(n_cells)]

        self.scores = np.array([ [ feature.score for feature in cell_clf ] for cell_clf in self.trained_classifiers ])



class LinearClassifier:

    """
        LinearClassifier constructor
        @param model - Model to train on
        @param impulse_feature - Impulse feature to train on
    """
    def __init__(self, cell_X, cell_y, impulse_feature):

        self.cell_X = cell_X # array of hidden states of the cell at each time step (so it's like a matrix if HS is a vector)
        self.cell_y = cell_y # array of labels ( what the feature outputs at each time step)
        self.impulse_feature = impulse_feature # we dont necessarily need the name of the feature it's just there

        self.score = self.get_score()

    def get_score(self):
        clf = make_pipeline(preprocessing.StandardScaler(), svm.LinearSVC())
        scores = cross_val_score(clf, self.cell_X, self.cell_y, cv=20)
        return scores.mean()
 