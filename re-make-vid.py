import os 
import glob
from tqdm import trange


train_root = '/home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_256/test/'

files = glob.glob(train_root + '/*.jpg')

for i in trange(len(files)):
    base_name = os.path.basename(files[i])

    if '#' in base_name:
        # import pdb; pdb.set_trace()
        # new_base_name = base_name.replace('#', '_')
        # os.system('mv %s %s'%(files[i], train_root + new_base_name))
        continue
    else:
        # continue
        new_base_name = base_name.replace('_0', '#0')
        os.system('mv %s %s'%(files[i], train_root + new_base_name))
        # import pdb; pdb.set_trace()
        # /home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_512_vid/train/trGNjNAxMMA_0186_S1344_E1388_L247_T309_R583_B645.mp4
        # /home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_512_vid/train/trGNjNAxMMA#0186_S1344_E1388_L247_T309_R583_B645.mp4

