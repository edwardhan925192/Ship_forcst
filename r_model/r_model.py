import pandas as pd

class R_model:
    def __init__(self,train,test args):
        self.model_name = args.model_name
        self.train = train
        self.test = test

        if args.model_name == 'autogluon':
          self.auto_time = args.auto_time

    def run_model(self):
        if self.model_name == 'autogluon':
          self.run_autogluon()

    def run_autogluon(self):
        from autogluon.tabular import TabularPredictor

        label = 'CI_HOUR'  # Modify if your target column has a different name

        # Assuming you've already split your data and loaded it into self.train and self.test
        train_data = self.train
        test_data = self.test

        predictor = TabularPredictor(label=label).fit(
            train_data=train_data,
            time_limit=3600 * self.auto_time,
            presets='best_quality',  # Can be a list or str of preset configurations. E.g., 'best_quality'
            #hyperparameters='auto',
            #num_stack_levels=1,
            #stack_ensemble_levels=0,
            #hyperparameter_tune=False,
        )
        
        test_predictions = predictor.predict(self.test)
        
        return test_predictions
