import os

from absl import flags

import xain.config

from .dataset import load_splits

c = xain.config.load()

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "local_datasets_dir",
    c.get("Path", "local_datasets_dir"),
    "Local directory to store datasets in. Usually ~/.xain/datasets",
)
flags.DEFINE_string(
    "datasets_repository",
    "http://xain-datasets.s3-website.eu-central-1.amazonaws.com",
    "Remote datasets repository.",
)
flags.DEFINE_boolean(
    "fetch_datasets",
    True,
    "Indicates if remote datasets should be fetched if required.",
)
