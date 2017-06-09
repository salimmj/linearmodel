import cfg
import numpy as np

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

        input = cfg.CFG();

        input.add_prod_rule('S0', '0 S0 | ( S1 )')
        input.add_prod_rule('S1', '1 S1 | ( S2 )')
        input.add_prod_rule('S2', '2 S2 | ( S3 )')
        input.add_prod_rule('S3', '3 S3 | ( S4 )')
        input.add_prod_fule('S4', '4, S4 | 4')
    	
        for i in xrange(10):

            print input.gen_random_sentence('S0')

            return input.gen_random_sentence('S0')


    """
        Returns a matrix of labels
        Size of matrix is (features, length_of_generated_input)
    """
    def get_data(self):

        #NOT CORRECT - WILL FIX ASAP

    	 return np.matrix( [self.feature_functions(self.generated_inputs)], [len(self.generated_inputs)] )
