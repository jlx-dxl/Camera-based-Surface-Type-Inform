import os
import torch
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

class ImageDataset(Dataset):
    def __init__(self, dataset_type, base_path=".", txt_folder='Data/Dataset/', transform=None):
        assert dataset_type in ['train', 'val', 'test'], "dataset_type must be 'train', 'val' or 'test'"
        
        txt_file = os.path.join(txt_folder, f'{dataset_type}_paths.txt')
        
        with open(txt_file, 'r') as f:
            self.image_paths = f.readlines()
        
        self.base_path = base_path
        self.transform = transforms.Compose([
            transforms.Resize((640, 480)),
            transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = os.path.join(self.base_path, self.image_paths[idx].strip())
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image

if __name__ == '__main__':
    i = 1
    dataset = ImageDataset('train')
    dataloader = DataLoader(dataset, batch_size=20, shuffle=True, num_workers=12)
    for batch in tqdm(dataloader):
        tqdm.write(f'Batch {i}: {batch.size()}')
        i += 1