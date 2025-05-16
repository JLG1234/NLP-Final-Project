import subprocess

# Set your experiment configs here for reproducibility.
EXPERIMENTS = [
    # (name, iters, batch_size, learning_rate, seed)
    ("run1_default200", 200, 4, "1e-5", 42),
    ("run2_default150", 150, 4, "1e-5", 42),
    ("run3_default250", 250, 4, "1e-5", 42),
    ("run4_default500", 500, 4, "1e-5", 42),
    ("run5_bs8_lr2e-5", 250, 8, "2e-5", 42),
    ("run6_bs16_lr2e-5", 250, 16, "2e-5", 42),
    ("run7_bs16_lr2e-5_500", 500, 16, "2e-5", 42),
]

MODEL_PATH = "./models/Ministral-3b-instruct"
DATA_PATH = "./data"
ADAPTER_PATH = "./adapters"

def run_experiment(name, iters, batch_size, lr, seed):
    print(f"\n==== Starting {name} ====")
    cmd = [
        "mlx_lm.lora",
        "--model", MODEL_PATH,
        "--data", DATA_PATH,
        "--adapter-path", ADAPTER_PATH,
        "--iters", str(iters),
        "--num-layers", "-1",
        "--batch-size", str(batch_size),
        "--learning-rate", str(lr),
        "--seed", str(seed),
        "--train"
    ]
    log_path = f"trainlog_{name}.txt"
    with open(log_path, "w") as logfile:
        result = subprocess.run(cmd, stdout=logfile, stderr=subprocess.STDOUT)
    print(f"Training for {name} complete. Log saved to {log_path}")

def evaluate_experiment(name):
    print(f"\n==== Evaluating {name} ====")
    eval_cmd = ["python3", "evaluate.py"]
    log_path = f"eval_{name}.txt"
    with open(log_path, "w") as logfile:
        subprocess.run(eval_cmd, stdout=logfile, stderr=subprocess.STDOUT)
    print(f"Evaluation for {name} complete. Log saved to {log_path}")

if __name__ == "__main__":
    # To reproduce all runs, simply uncomment the loop below.
    # for exp in EXPERIMENTS:
    #     name, iters, batch_size, lr, seed = exp
    #     run_experiment(name, iters, batch_size, lr, seed)
    #     evaluate_experiment(name)

    # To run just the best configuration, uncomment below:
    run_experiment("best_run_bs16_lr2e-5_500", 500, 16, "2e-5", 42)
    evaluate_experiment("best_run_bs16_lr2e-5_500")
