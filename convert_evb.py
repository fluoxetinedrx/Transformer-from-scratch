import os
import re
import json

def extract_pairs_from_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        content = f.read()

    spair_blocks = re.findall(r"<spair.*?>(.*?)</spair>", content, flags=re.DOTALL)
    pairs = []

    for block in spair_blocks:
        try:
            en = re.search(r"<s id='en\d+'>(.*?)</s>", block).group(1)
            vi = re.search(r"<s id='vn\d+'>(.*?)</s>", block).group(1)
            pairs.append({"translation": {"en": en.strip(), "vi": vi.strip()}})
        except:
            continue
    return pairs

def convert_all(input_folder, output_path="evb.jsonl"):
    all_pairs = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".sgml"):
            file_path = os.path.join(input_folder, filename)
            pairs = extract_pairs_from_file(file_path)
            all_pairs.extend(pairs)

    with open(output_path, "w", encoding="utf-8") as f:
        for pair in all_pairs:
            json.dump(pair, f, ensure_ascii=False)
            f.write("\n")

    print(f"saved {len(all_pairs)} sentence pairs to {output_path}")

if __name__ == "__main__":
    convert_all(r"F:\study\project\EVBCorpus\EVBCorpus_EVBNews_v1.0\EVBCorpus_v1\EVBNews")
