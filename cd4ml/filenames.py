"""
Keep all filename/path logic here rather than polluting code with hardcoded paths
"""
import os
from cd4ml.utils import ensure_dir_exists

data_dir_default = 'data'
data_dir = os.getenv('CD4ML_DATA_DIR', data_dir_default)

ensure_dir_exists(data_dir)
ensure_dir_exists("%s/results" % data_dir)
ensure_dir_exists("%s/splitter" % data_dir)

file_names = {
    'metrics': '%s/results/metrics.json' % data_dir,
    'train': '%s/splitter/train.csv' % data_dir,
    'validation': '%s/splitter/validation.csv' % data_dir
}

