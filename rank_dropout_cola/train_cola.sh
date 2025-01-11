#!/bin/bash
# export WANDB_RUN_ID="l25vss04"
# export WANDB_RESUME=true
export PYTHONPATH=$(pwd) # should be LoRa-XS folder
python task1/rank_dropout_cola/run_glue.py --target_task cola --wandb_diasabled False