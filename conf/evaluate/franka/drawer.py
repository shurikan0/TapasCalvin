from conf._machine import data_naming_config
from conf.env.panda.handguide_banana import franka_env_config
from conf.kp_encode_trajectories.vit.franka import policy_config as vit_config
from conf.policy.models.tpgmm.auto_test import auto_tpgmm_config
from tapas_gmm.env.franka import IK_Solvers, IKConfig
from tapas_gmm.evaluate import Config, EvalConfig
from tapas_gmm.policy.gmm import GMMPolicyConfig
from tapas_gmm.utils.config import SET_PROGRAMMATICALLY
from tapas_gmm.utils.misc import DataNamingConfig
from tapas_gmm.utils.observation import ObservationConfig

franka_env_config.teleop = True
franka_env_config.neutral_joints = (
    -0.9463,
    0.4039,
    -0.6560,
    -1.2133,
    1.0276,
    0.8185,
    -1.3722,
)
franka_env_config.eval = True
# franka_env_config.scale_action = False
franka_env_config.action_is_absolute = True
franka_env_config.postprocess_actions = False

# vit_config.encoder_config.encoder.use_spatial_expectation = False

franka_env_config.ik = IKConfig(
    solver=IK_Solvers.GN,
    max_iterations=1000,
    max_searches=50,
    tolerance=1e-6,
)


eval = EvalConfig(
    n_episodes=200,
    horizon=2500,
    seed=1,
    obs_dropout=None,
    viz=False,
    kp_per_channel_viz=False,
    show_channels=None,
)

encoder_naming_config = DataNamingConfig(
    task=None,  # If None, values are taken from data_naming_config
    feedback_type="demos",
    data_root=None,
)

policy_config = GMMPolicyConfig(
    suffix=None,
    model=auto_tpgmm_config,
    dbg_prediction=True,
    binary_gripper_action=True,
    batch_predict_in_t_models=False,
    return_full_batch=True,
    topp_in_t_models=True,
    topp_supersampling=0.1,  # 0.005,
    predict_dx_in_xdx_models=False,
    time_based=True,
    time_scale=1.0,
    force_overwrite_checkpoint_config=True,
    pos_lag_thresh=None,
    quat_lag_thresh=None,  # 0.4,
    pos_change_thresh=None,
    quat_change_thresh=None,  # 0.04,
    binary_gripper_closed_threshold=-0.5,
    encoder=vit_config,
    encoder_path="data/Drawer/demos_vit_keypoints_encoder-exp.pt",
    postprocess_prediction=False,  # Predicts abs pose if False
    # topp_in_t_models=True,
    # batch_t_max=1.25,
    # pos_change_thresh=None,
    # quat_change_thresh=None,
    # pos_lag_thresh=None,
    # quat_lag_thresh=None,
)


config = Config(
    env_config=franka_env_config,
    eval=eval,
    policy=policy_config,
    data_naming=data_naming_config,
    policy_type="gmm",
)
