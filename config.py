from pathlib import Path

def get_config():
    return {
        "batch_size": 8, 
        'num_workers': 2,
        "num_epochs": 4,
        "lr": 10**-4,
        "seq_len": 350,
        "d_model": 512,
        "lang_src": "en",
        "lang_tgt": "vi",
        "data_path": "evb.jsonl",
        "use_custom_dataset": True,
        "model_folder": "weights",
        "model_filename": "transformer_en_vi_",
        "preload": None,
        "tokenizer_file": "tokenizer_{0}.json",
        "experiment_name": "runs/transformer_en_vi_"
    }

def get_weights_file_path(config, epoch: str):
    model_folder = config['model_folder']
    model_filename = f"{config['model_filename']}{epoch}.pt"
    return str(Path(model_folder) / model_filename)