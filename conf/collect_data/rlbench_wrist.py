from conf._machine import data_naming_config
from conf.dataset.scene.rlbench_wrist import scene_dataset_config
from conf.env.rlbench.default import rlbench_env_config
from tapas_gmm.collect_data import Config
from tapas_gmm.env import Environment
from tapas_gmm.policy import PolicyEnum

config = Config(
    n_episodes=2,
    sequence_len=None,
    data_naming=data_naming_config,
    dataset_config=scene_dataset_config,
    env=Environment.RLBENCH,
    env_config=rlbench_env_config,
    policy_type=PolicyEnum.MANUAL,
    policy=None,
)
