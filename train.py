import subprocess

# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "200",
#     "--num-layers", "-1",
#     "--train"
# ])

# Evaluation results:
"""venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py
Loading pretrained model
Loading datasets
Testing
Test loss 1.993, Test ppl 7.334.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % 

"""

# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "150",
#     "--num-layers", "-1",
#     "--train"
# ])

"""venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py 
Loading pretrained model
Loading datasets
Testing
Test loss 2.051, Test ppl 7.774.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % """

# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "250",
#     "--num-layers", "-1",
#     "--train"
# ])
"""
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py
Loading pretrained model
Loading datasets
Testing
Test loss 1.968, Test ppl 7.155.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % """


# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "500",
#     "--num-layers", "-1",
#     "--train"
# ])

"""venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py
Loading pretrained model
Loading datasets
Testing
Test loss 1.899, Test ppl 6.681.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % 
"""

# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "250",
#     "--num-layers", "-1",
#     "--batch-size", "8",
#     "--learning-rate", "2e-5",
#     "--seed", "42",
#     "--train"
# ])

"""
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 train.py
Loading pretrained model
Loading datasets
Training
Trainable parameters: 0.045% (1.491M/3315.716M)
Starting training..., iters: 250
Iter 1: Val loss 5.852, Val took 3.707s
Iter 10: Train loss 4.441, Learning Rate 2.000e-05, It/sec 3.158, Tokens/sec 599.660, Trained Tokens 1899, Peak mem 8.219 GB
Iter 20: Train loss 2.873, Learning Rate 2.000e-05, It/sec 3.412, Tokens/sec 652.410, Trained Tokens 3811, Peak mem 8.219 GB
Iter 30: Train loss 2.468, Learning Rate 2.000e-05, It/sec 3.676, Tokens/sec 697.742, Trained Tokens 5709, Peak mem 8.219 GB
Iter 40: Train loss 2.259, Learning Rate 2.000e-05, It/sec 3.415, Tokens/sec 646.063, Trained Tokens 7601, Peak mem 8.219 GB
Iter 50: Train loss 2.028, Learning Rate 2.000e-05, It/sec 3.179, Tokens/sec 597.882, Trained Tokens 9482, Peak mem 8.219 GB
Iter 60: Train loss 2.093, Learning Rate 2.000e-05, It/sec 2.799, Tokens/sec 534.066, Trained Tokens 11390, Peak mem 8.219 GB
Iter 70: Train loss 2.111, Learning Rate 2.000e-05, It/sec 3.176, Tokens/sec 614.509, Trained Tokens 13325, Peak mem 8.219 GB
Iter 80: Train loss 2.083, Learning Rate 2.000e-05, It/sec 3.176, Tokens/sec 616.689, Trained Tokens 15267, Peak mem 8.219 GB
Iter 90: Train loss 2.057, Learning Rate 2.000e-05, It/sec 3.173, Tokens/sec 610.207, Trained Tokens 17190, Peak mem 8.219 GB
Iter 100: Train loss 2.004, Learning Rate 2.000e-05, It/sec 2.970, Tokens/sec 567.859, Trained Tokens 19102, Peak mem 8.219 GB
Iter 100: Saved adapter weights to adapters/adapters.safetensors and adapters/0000100_adapters.safetensors.
Iter 110: Train loss 2.028, Learning Rate 2.000e-05, It/sec 2.974, Tokens/sec 576.694, Trained Tokens 21041, Peak mem 8.225 GB
Iter 120: Train loss 1.926, Learning Rate 2.000e-05, It/sec 2.971, Tokens/sec 560.084, Trained Tokens 22926, Peak mem 8.225 GB
Iter 130: Train loss 1.909, Learning Rate 2.000e-05, It/sec 3.401, Tokens/sec 644.540, Trained Tokens 24821, Peak mem 8.225 GB
Iter 140: Train loss 1.949, Learning Rate 2.000e-05, It/sec 3.165, Tokens/sec 603.515, Trained Tokens 26728, Peak mem 8.225 GB
Iter 150: Train loss 1.989, Learning Rate 2.000e-05, It/sec 2.781, Tokens/sec 536.158, Trained Tokens 28656, Peak mem 8.225 GB
Iter 160: Train loss 1.978, Learning Rate 2.000e-05, It/sec 3.155, Tokens/sec 603.914, Trained Tokens 30570, Peak mem 8.225 GB
Iter 170: Train loss 1.801, Learning Rate 2.000e-05, It/sec 3.392, Tokens/sec 647.844, Trained Tokens 32480, Peak mem 8.225 GB
Iter 180: Train loss 1.918, Learning Rate 2.000e-05, It/sec 3.391, Tokens/sec 636.579, Trained Tokens 34357, Peak mem 8.225 GB
Iter 190: Train loss 1.748, Learning Rate 2.000e-05, It/sec 3.162, Tokens/sec 590.652, Trained Tokens 36225, Peak mem 8.225 GB
Iter 200: Val loss 1.899, Val took 3.842s
Iter 200: Train loss 1.866, Learning Rate 2.000e-05, It/sec 3.162, Tokens/sec 598.913, Trained Tokens 38119, Peak mem 8.225 GB
Iter 200: Saved adapter weights to adapters/adapters.safetensors and adapters/0000200_adapters.safetensors.
Iter 210: Train loss 1.805, Learning Rate 2.000e-05, It/sec 3.168, Tokens/sec 598.438, Trained Tokens 40008, Peak mem 8.225 GB
Iter 220: Train loss 1.904, Learning Rate 2.000e-05, It/sec 3.399, Tokens/sec 640.335, Trained Tokens 41892, Peak mem 8.225 GB
Iter 230: Train loss 1.853, Learning Rate 2.000e-05, It/sec 3.171, Tokens/sec 589.491, Trained Tokens 43751, Peak mem 8.225 GB
Iter 240: Train loss 1.756, Learning Rate 2.000e-05, It/sec 3.400, Tokens/sec 641.661, Trained Tokens 45638, Peak mem 8.225 GB
Iter 250: Val loss 1.825, Val took 3.794s
Iter 250: Train loss 1.862, Learning Rate 2.000e-05, It/sec 2.970, Tokens/sec 574.090, Trained Tokens 47571, Peak mem 8.225 GB
Saved final weights to adapters/adapters.safetensors.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py
Loading pretrained model
Loading datasets
Testing
Test loss 1.871, Test ppl 6.496.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % """

# subprocess.run([
#     "mlx_lm.lora",
#     "--model", "./models/Ministral-3b-instruct",
#     "--data", "./data",
#     "--adapter-path", "./adapters",
#     "--iters", "250",
#     "--num-layers", "-1",
#     "--batch-size", "16",
#     "--learning-rate", "2e-5",
#     "--seed", "42",
#     "--train"
# ])

"""
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 train.py   
Loading pretrained model
Loading datasets
Training
Trainable parameters: 0.045% (1.491M/3315.716M)
Starting training..., iters: 250
Iter 1: Val loss 5.873, Val took 7.288s
Iter 10: Train loss 4.391, Learning Rate 2.000e-05, It/sec 1.608, Tokens/sec 600.182, Trained Tokens 3733, Peak mem 9.565 GB
Iter 20: Train loss 2.647, Learning Rate 2.000e-05, It/sec 1.505, Tokens/sec 569.892, Trained Tokens 7519, Peak mem 9.565 GB
Iter 30: Train loss 2.416, Learning Rate 2.000e-05, It/sec 1.250, Tokens/sec 474.417, Trained Tokens 11314, Peak mem 9.565 GB
Iter 40: Train loss 2.265, Learning Rate 2.000e-05, It/sec 1.470, Tokens/sec 558.890, Trained Tokens 15116, Peak mem 9.565 GB
Iter 50: Train loss 2.114, Learning Rate 2.000e-05, It/sec 1.446, Tokens/sec 549.061, Trained Tokens 18913, Peak mem 9.565 GB
Iter 60: Train loss 2.063, Learning Rate 2.000e-05, It/sec 1.445, Tokens/sec 551.957, Trained Tokens 22733, Peak mem 9.565 GB
Iter 70: Train loss 2.071, Learning Rate 2.000e-05, It/sec 1.361, Tokens/sec 541.475, Trained Tokens 26712, Peak mem 9.565 GB
Iter 80: Train loss 2.020, Learning Rate 2.000e-05, It/sec 1.825, Tokens/sec 692.583, Trained Tokens 30507, Peak mem 9.565 GB
Iter 90: Train loss 2.064, Learning Rate 2.000e-05, It/sec 1.466, Tokens/sec 556.104, Trained Tokens 34300, Peak mem 9.565 GB
Iter 100: Train loss 1.932, Learning Rate 2.000e-05, It/sec 1.473, Tokens/sec 556.182, Trained Tokens 38076, Peak mem 9.565 GB
Iter 100: Saved adapter weights to adapters/adapters.safetensors and adapters/0000100_adapters.safetensors.
Iter 110: Train loss 1.908, Learning Rate 2.000e-05, It/sec 1.583, Tokens/sec 603.225, Trained Tokens 41886, Peak mem 9.571 GB
Iter 120: Train loss 1.933, Learning Rate 2.000e-05, It/sec 1.385, Tokens/sec 527.089, Trained Tokens 45693, Peak mem 9.571 GB
Iter 130: Train loss 1.871, Learning Rate 2.000e-05, It/sec 1.581, Tokens/sec 602.023, Trained Tokens 49502, Peak mem 9.571 GB
Iter 140: Train loss 1.902, Learning Rate 2.000e-05, It/sec 1.477, Tokens/sec 568.657, Trained Tokens 53352, Peak mem 9.571 GB
Iter 150: Train loss 1.897, Learning Rate 2.000e-05, It/sec 1.377, Tokens/sec 518.357, Trained Tokens 57116, Peak mem 9.571 GB
Iter 160: Train loss 1.915, Learning Rate 2.000e-05, It/sec 1.467, Tokens/sec 556.799, Trained Tokens 60912, Peak mem 9.571 GB
Iter 170: Train loss 1.919, Learning Rate 2.000e-05, It/sec 1.582, Tokens/sec 596.993, Trained Tokens 64685, Peak mem 9.571 GB
Iter 180: Train loss 1.929, Learning Rate 2.000e-05, It/sec 1.365, Tokens/sec 528.441, Trained Tokens 68555, Peak mem 9.571 GB
Iter 190: Train loss 1.809, Learning Rate 2.000e-05, It/sec 1.458, Tokens/sec 554.872, Trained Tokens 72361, Peak mem 9.571 GB
Iter 200: Val loss 1.864, Val took 8.531s
Iter 200: Train loss 1.844, Learning Rate 2.000e-05, It/sec 1.839, Tokens/sec 681.241, Trained Tokens 76065, Peak mem 9.571 GB
Iter 200: Saved adapter weights to adapters/adapters.safetensors and adapters/0000200_adapters.safetensors.
Iter 210: Train loss 1.946, Learning Rate 2.000e-05, It/sec 1.190, Tokens/sec 468.757, Trained Tokens 80005, Peak mem 9.571 GB
Iter 220: Train loss 1.805, Learning Rate 2.000e-05, It/sec 1.427, Tokens/sec 546.227, Trained Tokens 83834, Peak mem 9.571 GB
Iter 230: Train loss 1.825, Learning Rate 2.000e-05, It/sec 1.514, Tokens/sec 569.951, Trained Tokens 87599, Peak mem 9.571 GB
Iter 240: Train loss 1.819, Learning Rate 2.000e-05, It/sec 1.501, Tokens/sec 574.572, Trained Tokens 91428, Peak mem 9.571 GB
Iter 250: Val loss 1.852, Val took 8.982s
Iter 250: Train loss 1.777, Learning Rate 2.000e-05, It/sec 1.479, Tokens/sec 562.947, Trained Tokens 95235, Peak mem 9.571 GB
Saved final weights to adapters/adapters.safetensors.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py
Loading pretrained model
Loading datasets
Testing
Test loss 1.822, Test ppl 6.187."""

subprocess.run([
    "mlx_lm.lora",
    "--model", "./models/Ministral-3b-instruct",
    "--data", "./data",
    "--adapter-path", "./adapters",
    "--iters", "500",
    "--num-layers", "-1",
    "--batch-size", "16",
    "--learning-rate", "2e-5",
    "--seed", "42",
    "--train"
])

"""
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 train.py 
Loading pretrained model
Loading datasets
Training
Trainable parameters: 0.045% (1.491M/3315.716M)
Starting training..., iters: 500
Iter 1: Val loss 5.873, Val took 7.282s
Iter 10: Train loss 4.391, Learning Rate 2.000e-05, It/sec 1.609, Tokens/sec 600.696, Trained Tokens 3733, Peak mem 9.565 GB
Iter 20: Train loss 2.647, Learning Rate 2.000e-05, It/sec 1.505, Tokens/sec 569.938, Trained Tokens 7519, Peak mem 9.565 GB
Iter 30: Train loss 2.416, Learning Rate 2.000e-05, It/sec 1.253, Tokens/sec 475.383, Trained Tokens 11314, Peak mem 9.565 GB
Iter 40: Train loss 2.265, Learning Rate 2.000e-05, It/sec 1.504, Tokens/sec 571.961, Trained Tokens 15116, Peak mem 9.565 GB
Iter 50: Train loss 2.114, Learning Rate 2.000e-05, It/sec 1.493, Tokens/sec 566.716, Trained Tokens 18913, Peak mem 9.565 GB
Iter 60: Train loss 2.063, Learning Rate 2.000e-05, It/sec 1.470, Tokens/sec 561.424, Trained Tokens 22733, Peak mem 9.565 GB
Iter 70: Train loss 2.071, Learning Rate 2.000e-05, It/sec 1.375, Tokens/sec 546.946, Trained Tokens 26712, Peak mem 9.565 GB
Iter 80: Train loss 2.020, Learning Rate 2.000e-05, It/sec 1.864, Tokens/sec 707.553, Trained Tokens 30507, Peak mem 9.565 GB
Iter 90: Train loss 2.064, Learning Rate 2.000e-05, It/sec 1.496, Tokens/sec 567.415, Trained Tokens 34300, Peak mem 9.565 GB
Iter 100: Train loss 1.932, Learning Rate 2.000e-05, It/sec 1.499, Tokens/sec 565.919, Trained Tokens 38076, Peak mem 9.565 GB
Iter 100: Saved adapter weights to adapters/adapters.safetensors and adapters/0000100_adapters.safetensors.
Iter 110: Train loss 1.908, Learning Rate 2.000e-05, It/sec 1.609, Tokens/sec 613.203, Trained Tokens 41886, Peak mem 9.571 GB
Iter 120: Train loss 1.933, Learning Rate 2.000e-05, It/sec 1.410, Tokens/sec 536.717, Trained Tokens 45693, Peak mem 9.571 GB
Iter 130: Train loss 1.871, Learning Rate 2.000e-05, It/sec 1.612, Tokens/sec 614.083, Trained Tokens 49502, Peak mem 9.571 GB
Iter 140: Train loss 1.902, Learning Rate 2.000e-05, It/sec 1.504, Tokens/sec 579.050, Trained Tokens 53352, Peak mem 9.571 GB
Iter 150: Train loss 1.897, Learning Rate 2.000e-05, It/sec 1.410, Tokens/sec 530.613, Trained Tokens 57116, Peak mem 9.571 GB
Iter 160: Train loss 1.915, Learning Rate 2.000e-05, It/sec 1.504, Tokens/sec 570.982, Trained Tokens 60912, Peak mem 9.571 GB
Iter 170: Train loss 1.919, Learning Rate 2.000e-05, It/sec 1.613, Tokens/sec 608.711, Trained Tokens 64685, Peak mem 9.571 GB
Iter 180: Train loss 1.929, Learning Rate 2.000e-05, It/sec 1.410, Tokens/sec 545.665, Trained Tokens 68555, Peak mem 9.571 GB
Iter 190: Train loss 1.809, Learning Rate 2.000e-05, It/sec 1.504, Tokens/sec 572.467, Trained Tokens 72361, Peak mem 9.571 GB
Iter 200: Val loss 1.864, Val took 8.267s
Iter 200: Train loss 1.844, Learning Rate 2.000e-05, It/sec 1.882, Tokens/sec 697.026, Trained Tokens 76065, Peak mem 9.571 GB
Iter 200: Saved adapter weights to adapters/adapters.safetensors and adapters/0000200_adapters.safetensors.
Iter 210: Train loss 1.946, Learning Rate 2.000e-05, It/sec 1.241, Tokens/sec 489.142, Trained Tokens 80005, Peak mem 9.571 GB
Iter 220: Train loss 1.805, Learning Rate 2.000e-05, It/sec 1.492, Tokens/sec 571.458, Trained Tokens 83834, Peak mem 9.571 GB
Iter 230: Train loss 1.825, Learning Rate 2.000e-05, It/sec 1.599, Tokens/sec 601.913, Trained Tokens 87599, Peak mem 9.571 GB
Iter 240: Train loss 1.819, Learning Rate 2.000e-05, It/sec 1.599, Tokens/sec 612.420, Trained Tokens 91428, Peak mem 9.571 GB
Iter 250: Train loss 1.777, Learning Rate 2.000e-05, It/sec 1.590, Tokens/sec 605.319, Trained Tokens 95235, Peak mem 9.571 GB
Iter 260: Train loss 1.823, Learning Rate 2.000e-05, It/sec 1.306, Tokens/sec 503.449, Trained Tokens 99091, Peak mem 9.571 GB
Iter 270: Train loss 1.843, Learning Rate 2.000e-05, It/sec 1.383, Tokens/sec 539.829, Trained Tokens 102993, Peak mem 9.571 GB
Iter 280: Train loss 1.792, Learning Rate 2.000e-05, It/sec 1.479, Tokens/sec 563.192, Trained Tokens 106801, Peak mem 9.571 GB
Iter 290: Train loss 1.799, Learning Rate 2.000e-05, It/sec 1.377, Tokens/sec 532.135, Trained Tokens 110666, Peak mem 9.571 GB
Iter 300: Train loss 1.860, Learning Rate 2.000e-05, It/sec 1.475, Tokens/sec 572.197, Trained Tokens 114545, Peak mem 9.571 GB
Iter 300: Saved adapter weights to adapters/adapters.safetensors and adapters/0000300_adapters.safetensors.
Iter 310: Train loss 1.853, Learning Rate 2.000e-05, It/sec 1.468, Tokens/sec 563.753, Trained Tokens 118385, Peak mem 9.571 GB
Iter 320: Train loss 1.842, Learning Rate 2.000e-05, It/sec 1.364, Tokens/sec 522.318, Trained Tokens 122214, Peak mem 9.571 GB
Iter 330: Train loss 1.794, Learning Rate 2.000e-05, It/sec 1.554, Tokens/sec 581.293, Trained Tokens 125954, Peak mem 9.571 GB
Iter 340: Train loss 1.764, Learning Rate 2.000e-05, It/sec 1.341, Tokens/sec 512.748, Trained Tokens 129777, Peak mem 9.571 GB
Iter 350: Train loss 1.731, Learning Rate 2.000e-05, It/sec 1.330, Tokens/sec 504.775, Trained Tokens 133572, Peak mem 9.571 GB
Iter 360: Train loss 1.783, Learning Rate 2.000e-05, It/sec 1.166, Tokens/sec 447.886, Trained Tokens 137414, Peak mem 9.571 GB
Iter 370: Train loss 1.727, Learning Rate 2.000e-05, It/sec 1.219, Tokens/sec 475.031, Trained Tokens 141312, Peak mem 9.571 GB
Iter 380: Train loss 1.790, Learning Rate 2.000e-05, It/sec 1.478, Tokens/sec 562.491, Trained Tokens 145118, Peak mem 9.571 GB
Iter 390: Train loss 1.772, Learning Rate 2.000e-05, It/sec 1.579, Tokens/sec 609.237, Trained Tokens 148977, Peak mem 9.571 GB
Iter 400: Val loss 1.800, Val took 9.081s
Iter 400: Train loss 1.696, Learning Rate 2.000e-05, It/sec 1.456, Tokens/sec 547.009, Trained Tokens 152735, Peak mem 9.571 GB
Iter 400: Saved adapter weights to adapters/adapters.safetensors and adapters/0000400_adapters.safetensors.
Iter 410: Train loss 1.669, Learning Rate 2.000e-05, It/sec 1.313, Tokens/sec 494.987, Trained Tokens 156505, Peak mem 9.571 GB
Iter 420: Train loss 1.758, Learning Rate 2.000e-05, It/sec 1.393, Tokens/sec 531.258, Trained Tokens 160319, Peak mem 9.571 GB
Iter 430: Train loss 1.703, Learning Rate 2.000e-05, It/sec 1.292, Tokens/sec 485.580, Trained Tokens 164077, Peak mem 9.571 GB
Iter 440: Train loss 1.695, Learning Rate 2.000e-05, It/sec 1.275, Tokens/sec 491.307, Trained Tokens 167930, Peak mem 9.571 GB
Iter 450: Train loss 1.714, Learning Rate 2.000e-05, It/sec 1.488, Tokens/sec 570.311, Trained Tokens 171763, Peak mem 9.571 GB
Iter 460: Train loss 1.791, Learning Rate 2.000e-05, It/sec 1.178, Tokens/sec 461.952, Trained Tokens 175683, Peak mem 9.571 GB
Iter 470: Train loss 1.733, Learning Rate 2.000e-05, It/sec 1.460, Tokens/sec 550.541, Trained Tokens 179454, Peak mem 9.571 GB
Iter 480: Train loss 1.752, Learning Rate 2.000e-05, It/sec 1.169, Tokens/sec 445.171, Trained Tokens 183261, Peak mem 9.571 GB
Iter 490: Train loss 1.779, Learning Rate 2.000e-05, It/sec 1.177, Tokens/sec 463.988, Trained Tokens 187202, Peak mem 9.571 GB
Iter 500: Val loss 1.767, Val took 10.047s
Iter 500: Train loss 1.706, Learning Rate 2.000e-05, It/sec 1.250, Tokens/sec 482.423, Trained Tokens 191062, Peak mem 9.571 GB
Iter 500: Saved adapter weights to adapters/adapters.safetensors and adapters/0000500_adapters.safetensors.
Saved final weights to adapters/adapters.safetensors.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % python3 evaluate.py 
Loading pretrained model
Loading datasets
Testing
Test loss 1.750, Test ppl 5.752.
venvjoeyguedalia@Joeys-MacBook-Pro Final Project % """