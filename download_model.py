# download_model.py
from huggingface_hub import snapshot_download

def download_ministral_model(model_id="ministral/Ministral-3b-instruct", local_dir="./models_/Ministral-3b-instruct"):
    print(f"Downloading {model_id} to {local_dir} ...")
    snapshot_download(repo_id=model_id, local_dir=local_dir, local_dir_use_symlinks=False)
    print(f"Model downloaded to {local_dir}")

if __name__ == "__main__":
    download_ministral_model()
