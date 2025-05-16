import subprocess

subprocess.run([
    "mlx_lm.lora",
    "--model", "./models/Ministral-3b-instruct",
    "--data", "./data",
    "--adapter-path", "./adapters",
    "--iters", "200",
    "--num-layers", "-1",
    "--test"
])

