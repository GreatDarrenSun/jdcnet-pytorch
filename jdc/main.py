import json
from .train import JDCTrainer

# load configuration file
with open('config.json', 'r') as jsonf:
    config = json.load(jsonf)

# create trainer and start training
jdc_trainer = JDCTrainer(config)
jdc_trainer.fit()
