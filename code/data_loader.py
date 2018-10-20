from torch.utils.data.dataset import Dataset
from torchvision import transforms
from skimage import io, transform
import os
import numpy as np
import re

class SourceSepTrain(Dataset):
    def __init__(self, path='../Processed/Mixtures'): 
    # assuming this to be the directory containing all the magnitude spectrum 
    #for all songs and all segments used in training
        self.path = path
        self.list = os.listdir(self.path)

    def __getitem__(self, index):
        mixture_path = '../Processed/Mixtures/'
        bass_path = '../Processed/Bass/'
        vocals_path = '../Processed/Vocals/'
        drums_path = '../Processed/Drums/'
        others_path = '../Processed/Others/'
        mixture = torch.load(mixture_path+self.list[index])
        #phase = torch.load(mixture_path+self.list[index]+'_p')
        bass = torch.load(bass_path+self.list[index])
        vocals = torch.load(vocals_path+self.list[index])
        drums = torch.load(drums_path+self.list[index])
        others = torch.load(others_path+self.list[index])

        return (mixture,bass, vocals, drums, others)

    def __len__(self):
        return len(self.list) # length of how much data you have


class SourceSepTest(Dataset):
    def __init__(self, path='../Val/Mixtures'):
        # assuming this to be the directory containing all the magnitude spectrum 
        #for all songs and all segments used in training
        self.path = path
        self.list = os.listdir(self.path)

    def __getitem__(self, index):
        # stuff
        mixture_path = '../Val/Mixtures/'
        bass_path = '../Val/Bass/'
        vocal_path = '../Val/Vocals/'
        drums_path = '../Val/Drums/'
        others_path = '../Val/Others/'

        mixture = torch.load(mixture_path+self.list[index])
        #phase = torch.load(mixture_path+self.list[index]+'_p')
        bass = torch.load(bass_path+self.list[index])
        vocals = torch.load(vocals_path+self.list[index])
        drums = torch.load(drums_path+self.list[index])
        others = torch.load(others_path+self.list[index])

        return (mixture, bass, vocals, drums, others)

    def __len__(self):
        return len(self.list)
