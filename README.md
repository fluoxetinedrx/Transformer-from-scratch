# Transformer Machine Translation (English → Vietnamese)

A from-scratch implementation of the Transformer architecture based on the seminal paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762), built using PyTorch.  
This project focuses on translating from **English to Vietnamese** using a fully custom tokenizer and training pipeline.

---

## Features

- Custom WordLevel tokenizer (trained from data)
- Full Transformer model from scratch (no Hugging Face, no high-level wrappers)
- Positional encoding, multi-head self-attention, residual connections
- Proper masking (padding and causal masks)
- Label smoothing, checkpointing, TensorBoard logging
- Train-ready with `evb.jsonl` dataset (English-Vietnamese)
