import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset as torchDataset
from transformers import BertModel, BertTokenizer
import numpy as np
import re
import nltk
from nltk.corpus import stopwords


models = {
    'buy/rent': {'filename': 'buy_rent_model', 'labels': ['buy', 'rent', 'irrelevant']},
    'time': {'filename': 'time_model', 'labels': ['less than 6 month', '6 month', 'one year', 'irrelevant']},
    'ready/off-plan': {'filename': 'ready_off_plan_model', 'labels': ['ready', 'off-plan', 'irrelevant']},
    'property_type': {'filename': 'apartment_villa_model', 'labels': ['apartment', 'villa', 'irrelevant']},
    'room': {'filename': 'room_model', 'labels': ['0', '1', '2', '3', '4', '5', 'irrelevant']}
}
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
max_len = 25
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


'''
    Import Dataset Class & Model Class
'''


class Dataset(torchDataset):
    def __init__(self, tokenizer, dialogue_texts, targets=None, labels=None, max_len=50):
        self.dialogue_texts = dialogue_texts
        self.targets = targets
        self.has_target = isinstance(targets, list) or isinstance(targets, np.ndarray)
        self.label_map = {label: i for i, label in enumerate(labels)} if isinstance(labels, list) else {}
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.dialogue_texts)

    def __getitem__(self, item):
        dialogue_texts = self.dialogue_texts[item]

        encoding = self.tokenizer.encode_plus(
            dialogue_texts,
            add_special_tokens=True,
            truncation=True,
            max_length=self.max_len,
            return_token_type_ids=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt'
            )

        inputs = {
            'dialoge_text': dialogue_texts,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'token_type_ids': encoding['token_type_ids'].flatten()
        }

        if self.has_target:
            target = self.label_map.get(self.targets[item], self.targets[item])
            inputs['targets'] = torch.tensor(target, dtype=torch.long)

        return inputs


class ClassifierModel(nn.Module):
    def __init__(self, config):
        super(ClassifierModel, self).__init__()

        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)

    def forward(self, input_ids, attention_mask, token_type_ids):
        _, pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            return_dict=False)
        return self.classifier(self.dropout(pooled_output))


'''
    Import Preprocessing functions
'''


def preprocess_text(text: str, remove_stopwords: bool):
    text = re.sub(r"http\S+", "", text)
    text = re.sub("[^A-Za-z]+", " ", text)
    if remove_stopwords:
        tokens = nltk.word_tokenize(text)
        tokens = [w for w in tokens if not w.lower() in stopwords.words("english")]
        text = " ".join(tokens)
    text = text.lower().strip()
    return text


def preprocess_documents(documents):
    texts = []
    for i in range(len(documents)):
        text = preprocess_text(documents[i], remove_stopwords=False)
        texts.append(text)
    return texts


'''
    Import Loadings & Predictions functions
'''


def predict(model, targets, tokenizer, max_len=max_len, batch_size=32):
    dataset_p = Dataset(tokenizer, targets, None, None, max_len)
    data_loader = torch.utils.data.DataLoader(dataset_p, batch_size=batch_size)

    predictions = []
    prediction_probabilities = []

    model.eval()
    with torch.no_grad():
        for dl in data_loader:
            input_ids = dl['input_ids']
            attention_mask = dl['attention_mask']
            token_type_ids = dl['token_type_ids']

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            token_type_ids = token_type_ids.to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
                            token_type_ids=token_type_ids)

            _, preds = torch.max(outputs, dim=1)

            predictions.extend(preds)
            prediction_probabilities.extend(F.softmax(outputs, dim=1))

    predictions = torch.stack(predictions).cpu().detach().numpy()
    prediction_probabilities = torch.stack(prediction_probabilities).cpu().detach().numpy()

    return predictions, prediction_probabilities


def get_model_response(prompt, model_name, thresh=0.5, root_dir='model/'):
    assert models.keys().__contains__(model_name)
    model_info = models[model_name]
    model_filename = model_info['filename']
    labels = model_info['labels']
    model = torch.load(root_dir + model_filename, map_location=torch.device(device))
    preprocessed_text = preprocess_documents([prompt])
    y_pred, probs = predict(model, preprocessed_text, bert_tokenizer, max_len=max_len)
    if probs[0][y_pred[0]] < thresh:
        return None, None
    return y_pred[0], labels[y_pred[0]]
