

class DataGenerator:

    def __init__(self, cfg, feature_functions):

        self.cfg = cfg
        self.feature_functions = feature_functions

        self.generated_inputs = self.generate_inputs()
        self.training_data = self.get_data()


    """
        Returns a sequence of inputs (list of characters).
        It generates it from the Context-Free Grammar rules of a language
    """
    def generate_inputs(self):
        pass


    """
        Returns a matrix of labels
        Size of matrix is (features, length_of_generated_input)
    """
    def get_data(self):
        pass
