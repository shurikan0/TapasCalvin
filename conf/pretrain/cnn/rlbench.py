from conf._machine import data_naming_config
from conf.encoder.cnn.default import cnn_config
from conf.pretrain.default import observation_config, training_config
from tapas_gmm.pretrain import Config
from tapas_gmm.utils.data_loading import DataLoaderConfig

dataloader_config = DataLoaderConfig(
    train_split=0.7,
    batch_size=16,
    eval_batchsize=160,
)

config = Config(
    encoder_name="cnn",
    encoder_config=cnn_config,
    encoder_suffix=None,
    training=training_config,
    observation=observation_config,
    data_naming=data_naming_config,
    dataloader=dataloader_config,
    dc_data=None,
)
