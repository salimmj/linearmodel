from CFG import CFG
import numpy as np

class DataGenerator:

    def __init__(self, cfg, feature_functions):

        self.cfg = cfg
        self.feature_functions = feature_functions

        # self.generated_inputs = self.generate_inputs()
        # self.training_data = self.get_data()


    """
        Returns a sequence of inputs (list of characters).
        It generates it from the Context-Free Grammar rules of a language
    """
    def generate_inputs(self, n):

        input = CFG()

        input.add_prod_rule('S0', '0 S0 | ( S1 )')
        input.add_prod_rule('S1', '1 S1 | ( S2 )')
        input.add_prod_rule('S2', '2 S2 | ( S3 )')
        input.add_prod_rule('S3', '3 S3 | ( S4 )')
        input.add_prod_rule('S4', '4 S4 | 4')

        output = ''

        for i in xrange(n):
            output += input.gen_random_sentence('S0')

        return output


    """
        Returns a matrix of labels
        Size of matrix is (features, length_of_generated_input)
    """
    def get_data(self):

        #NOT CORRECT - WILL FIX ASAP

         return np.matrix( [self.feature_functions(self.generated_inputs)], [len(self.generated_inputs)] )
