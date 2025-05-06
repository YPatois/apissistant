#!/usr/bin/env python3

import os # Optional for faster downloading
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
#os.environ["HF_HOME"] = "some_path/.cache/huggingface"
token=os.environ["HF_TOKEN"]

from huggingface_hub import snapshot_download

while True:
  try:
    snapshot_download(
      repo_id = "unsloth/DeepSeek-R1-GGUF",
      local_dir = "DeepSeek-R1-GGUF",
      allow_patterns = ["*UD-IQ1_S*"], # Select quant type UD-IQ1_S for 1.58bit,
      token = token,
      max_workers = 4
    )
  except RuntimeError:
    print ("Failed... Retrying...")


