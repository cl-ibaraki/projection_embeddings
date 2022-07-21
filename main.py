import os
import torch
from transformers import BertModel, BertJapaneseTokenizer
from tensorboardX import SummaryWriter

if __name__ == '__main__':
    model = BertModel.from_pretrained('cl-tohoku/bert-large-japanese')
    tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-large-japanese')

    token_embeddings = model.get_input_embeddings().weight.clone()
    vocab = tokenizer.get_vocab()

    embeddings = []
    words = []

    start_id = 11138

    for word in vocab:
        if '##' not in word and start_id <= vocab[word] and vocab[word] <= start_id+10000:
            embeddings.append(token_embeddings[vocab[word]])
            words.append(word)

    embeddings = torch.stack(embeddings, dim=0)

    writer = SummaryWriter()
    writer.add_embedding(embeddings, metadata=words)

