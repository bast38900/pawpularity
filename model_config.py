from pred_models.models import LinearRegressionModel, LogisticRegressionModel, NN_PawpularityModel, NN_HumanModel, AdaBoostModel, KMeansModel, StackedModel


class ModelConfig:
    # Maps model types to their corresponding class implementations
    model_factory = {
        'linear_regression': LinearRegressionModel,
        'logistic_regression': LogisticRegressionModel,
        'nn_pawpularity': NN_PawpularityModel,
        'nn_human': NN_HumanModel,
        'kmeans' : KMeansModel,
        'ada_boost': AdaBoostModel,
        'stacked_model': StackedModel
    }

    # Maps use cases to the models that can be used for them
    use_case_models = {
        'human_prediction': ['logistic_regression','nn_human', 'ada_boost', 'stacked_model'],
        'pawpularity_score': ['linear_regression', 'nn_pawpularity'],
        'occlusion_detection': ['logistic_regression'],
        'data_clustering': ['kmeans'],
    }

    # Specifies the default model for each use case
    default_models = {
        'human_prediction': 'logistic_regression',
        'pawpularity_score': 'linear_regression',
        'occlusion_detection': 'logistic_regression',
        'data_clustering': 'kmeans',
    }

    # Defines which use cases are allowed
    allowed_use_cases = {
        'human_prediction', 
        'pawpularity_score', 
        'occlusion_detection',
        'data_clustering',
    }