from Classifier import Classifier


"""
    Featured-Scored Model Class
    Abstraction of feature as a query on a model.
    Holds the model, the list of features (queries) and the output.
    The main task of this class is to return a score for each feature for each neuron.
    Other methods are helper methods.
"""
class FS_Model:

    """
        FS_Model constructor
        @param model - Model to query
        @param feature_list - List of features (queries)
    """
    def __init__(self, model, feature_list, n_cells):

        self.model = model
        self.feature_list = feature_list
        self.feature_len = len(feature_list)
        self.n_cells = n_cells

        # Creates Classifier instance which trains on model (for each feature separately)
        self.TrainedClassifier = Classifier(model, feature_list)

        self.cell_scores = self.get_scores()


    """
        Returns list of scores of each cell
    """
    def get_scores(self):
        scores = {} # list of scores, one for each udf

        # Making List of cell scores. Each cell score is a list of score for each feature
        for i in range(self.n_cells):
            scores[i] = []

        # Filling the scores for each cell
        for cell in range(self.n_cells):
            scores[cell] = self.get_cell_scores(cell)

        return scores


    """
        Returns feature scores of specified cell as a list
        @param cell - Cell to query by each feature
    """
    def get_cell_scores(self, cell):
        cell_scores = [0] * self.feature_len

        for feature in range(self.feature_len):
            cell_scores[feature] = self.calculate_score(cell, feature)


    """
        Returns score (type double) of prediction accuracy of the cell on the feature
        @param cell - Cell to query
        @param feature - Feature (query)
    """
    def calculate_score(self, cell, feature):
        return self.TrainedClassifier.get_cell_accuracy_wrt_feature(cell, feature)
