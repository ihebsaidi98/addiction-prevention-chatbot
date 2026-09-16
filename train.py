import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.nn.modules import module
from torch.utils.data import Dataset, DataLoader

from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
# nboucliw jomal l patterns ly fl intents lkol
for intent in intents['intents']:
    tag = intent['tag']
    # n7oto kol tag fil list tags
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize kol jomla
        w = tokenize(pattern)
        # n7oto l kelmet fil list all words
        all_words.extend(w)
        # n7oto kol word wl tag mte3ha fil list xy
        xy.append((w, tag))

# na7iw l ponctuation w ne5dho l base mt3 kol kelma ba3d manrj3oha miniscule
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# na7iw l kelmat l m3awda w nadhmhom selon l alphabet
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

# training data
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # X: bag of words lkol jomla fil patterns
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: n3ty label lkol tag bsh njm n3ytlo byh
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train


    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)


criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
    
        outputs = model(words)
       
        loss = criterion(outputs, labels)
        
       
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')