from APS_sensor.configuration.mongo_db_connection import MongoDBClient
from APS_sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from APS_sensor.pipeline.training_pipeline import TrainingPipeline
if __name__ == '__main__':
    train_pipeline= TrainingPipeline()
    train_pipeline = train_pipeline.run_pipeline()
    
