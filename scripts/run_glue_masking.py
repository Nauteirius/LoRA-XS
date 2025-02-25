import argparse
import os


def glue_main(args):
    epoch = 40
    task = args.target_task  # should be one of COLA, SST2 and QNLI tasks
    model_name = "roberta-large"
    seeds = [int(args.seed)] if args.seed else [42, 43, 44, 45, 46]
    wandb_disabled = args.wandb_disabled
    for rank in [25]:
        results_dir = f"rank_masking_results_{task}_{rank}"
        for lr in [2e-3]:
            for cls_lr in [1e-3]:
                for seed in seeds:
                    run_str = f"""
                       WANDB_DISABLED="{wandb_disabled}" \
                       python main_glue_rank_masking.py \
                         --model_name_or_path {model_name} \
                         --lora_rank {rank} \
                         --task_name {task} \
                         --do_train \
                         --do_eval \
                         --seed {seed}\
                         --max_seq_length 128 \
                         --per_device_train_batch_size 32 \
                         --learning_rate {lr} \
                         --cls_learning_rate {cls_lr} \
                         --num_train_epochs {epoch} \
                         --save_steps 13400 \
                         --evaluation_strategy epoch  \
                         --logging_steps 1 \
                         --overwrite_output_dir \
                         --output_dir {results_dir}"""
                    os.system(run_str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_task", required=False, default="cola")
    parser.add_argument("--seed", required=False, default=None)
    parser.add_argument("--wandb_disabled", required=False, default=True)

    args = parser.parse_args()

    glue_main(args)