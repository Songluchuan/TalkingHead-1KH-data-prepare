import os 
import pickle
import glob 
from tqdm import trange

# root_dir = '/home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_512_vid'
# train_videos = {os.path.basename(video).split('#')[0] for video in os.listdir(os.path.join(root_dir, 'train'))}
# train_videos = list(train_videos)

ori_list = '/home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_256/train_file_list.pickle'
tmp_file = open(ori_list,'rb')
train_files_list = pickle.load(tmp_file)
ids = list(train_files_list.keys())#[:20]

# import pdb; pdb.set_trace()
# ids = ids[:20]
dirt = {}

for i in trange(len(ids)):
    names = train_files_list[ids[i]]
    print(i, '/', len(ids))

    tmp = []
    for j in range(len(names)):
        # print(j, '/', len(names))

        ff = names[j].replace('cropped_clips_256', 'cropped_clips_512_vid').replace('.jpg', '.mp4')
        if os.path.isdir(ff):
            if len(os.listdir(ff)) > 5:
                tmp.append(ff)
        else:
            continue

    dirt[ids[i]] = tmp
    


list_file = open('/home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_512_vid/train_file_list.pickle','wb')
pickle.dump(dirt,list_file)
list_file.close()

