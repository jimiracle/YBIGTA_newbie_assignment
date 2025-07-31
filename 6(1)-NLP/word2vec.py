import torch
from torch import nn, Tensor, LongTensor
from torch.optim import Adam

from transformers import PreTrainedTokenizer

from typing import Literal


import time
from tqdm import tqdm



class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method
        

    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        pad_token_id = tokenizer.pad_token_id

        tokenized = [tokenizer.encode(sent, add_special_tokens=False) for sent in corpus]
        tokenized = [[tok for tok in sent if tok != pad_token_id] for sent in tokenized]

        print(f"Training start: method = {self.method}, epochs = {num_epochs}")
        for epoch in range(1, num_epochs + 1):
            start_time = time.time()
            print(f"\n[Epoch {epoch}/{num_epochs}]")

            if self.method == "cbow":
                loss = self._train_cbow(tokenized, criterion, optimizer)
            elif self.method == "skipgram":
                loss = self._train_skipgram(tokenized, criterion, optimizer)

            elapsed = time.time() - start_time
            print(f"  Loss: {loss:.4f} | Time: {elapsed:.2f}s | ETA: {(elapsed * (num_epochs - epoch)):.2f}s")


    def _train_cbow(self, tokenized, criterion, optimizer):
        self.train()
        window = self.window_size
        total_loss = 0
        count = 0

        for sent in tqdm(tokenized, desc="CBOW Training"):
            if len(sent) < 2 * window + 1:
                continue
            for idx in range(window, len(sent) - window):
                context = sent[idx - window:idx] + sent[idx + 1:idx + window + 1]
                target = sent[idx]
                context_tensor = torch.tensor(context, dtype=torch.long).to(self.embeddings.weight.device)
                target_tensor = torch.tensor([target], dtype=torch.long).to(self.embeddings.weight.device)

                context_emb = self.embeddings(context_tensor)
                context_emb = context_emb.mean(dim=0, keepdim=True)
                logits = self.weight(context_emb)
                loss = criterion(logits, target_tensor)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                count += 1

        return total_loss / count if count > 0 else 0

    def _train_skipgram(self, tokenized, criterion, optimizer):
        self.train()
        window = self.window_size
        total_loss = 0
        count = 0

        for sent in tqdm(tokenized, desc="Skip-Gram Training"):
            if len(sent) < 2 * window + 1:
                continue
            for idx in range(window, len(sent) - window):
                target = sent[idx]
                context = sent[idx - window:idx] + sent[idx + 1:idx + window + 1]
                target_tensor = torch.tensor([target], dtype=torch.long).to(self.embeddings.weight.device)

                for ctx in context:
                    ctx_tensor = torch.tensor([ctx], dtype=torch.long).to(self.embeddings.weight.device)
                    target_emb = self.embeddings(target_tensor)
                    logits = self.weight(target_emb)
                    loss = criterion(logits, ctx_tensor)

                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                    total_loss += loss.item()
                    count += 1

        return total_loss / count if count > 0 else 0