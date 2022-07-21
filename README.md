# projection_embeddings

BERTのToken Embeddingsを可視化します。

## Setting

* 次のコマンドでパッケージインストールします。

```bash
pip3 install -r requirements.txt
```

## BERTからベクトルを保存

```bash
python3 main.py
```

## TensorBoardを起動

```bash
tensorboard --logdir runs/
```

* ブラウザから`localhost:6006`にアクセス。
* 上のプルダウンからPROJECTORを選択。