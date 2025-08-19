from TextSummarization.config.configuration import ConfigurationManager
from TextSummarization.components.data_validation import DataValidation   # ✅ Correct
from TextSummarization.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)   # ✅ Fixed here too
        data_validation.validate_all_files_exist()


"""
from TextSummarization.config.configuration import ConfigurationManager
from TextSummarization.components.data_validation import DataValiadtion
from TextSummarization.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
"""