import os 
import cv2 

import pdb 
import tqdm
import glob
import argparse

from functools import partial
from time import time as timer
from multiprocessing import Pool

import numpy as np
import multiprocessing as mp

# python extract_frames.py --output_dir /home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips_512_vid/test --size 512 --num_workers 32

parser = argparse.ArgumentParser()
# parser.add_argument('--input_dir', type=str, required=True,
#                     help='Dir containing youtube clips.')
parser.add_argument('--output_dir', type=str, required=True,
                    help='Location to dump outputs.')
parser.add_argument('--size', type=int, default=512,
                    help='image size.')
parser.add_argument('--num_workers', type=int, default=8,
                    help='How many multiprocessing workers?')
args = parser.parse_args()

def extract_frames(save_path, img_size, video_path):
    video_capture = cv2.VideoCapture(video_path)
    index = 0

    base_video = os.path.basename(video_path)
    base_video = base_video.replace('_00', '#00')
    save_jpg = os.path.join(save_path, base_video)
    os.makedirs(save_jpg, exist_ok=True)
    
    while True:
        success, frame = video_capture.read()
        #####
        if not success:
            break
        #####
        # elif index > 90:
        #     break
        else:
            
            rsz_frame = cv2.resize(frame, (int(img_size), int(img_size)), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(save_jpg + '/%06d.jpg'%index, rsz_frame)

            # if frame_array is None:
            #     frame_array = rsz_frame
            # else:
            #     frame_array = np.concatenate((frame_array, rsz_frame), axis=1)
            index = index + 1
    print(save_jpg)
    if len(os.listdir(save_jpg)) < 5:
        os.system('rm -rf %s'%save_jpg)
        return 
    



if __name__ == '__main__':

    crop_lists = sorted(glob.glob('/home/cxu-serve/p61/lsong11/TalkingHead-1KH/train/cropped_clips/*.mp4'))[-500:]
    print('length: ', len(crop_lists))
    # Create output folder.
    os.makedirs(args.output_dir, exist_ok=True)
    # Download videos.
    # process_vid = partial(extract_frames, args.output_dir, args.size)
    # import pdb; pdb.set_trace()

    # extract_frames(args.output_dir, args.size, crop_lists[0])

    start = timer()
    pool_size = args.num_workers
    print('Using pool size of %d' % (pool_size))
    
    process_pool = mp.Pool(processes=pool_size)
    for uu in range(len(crop_lists)):
        process_pool.apply_async(extract_frames, args=(args.output_dir, args.size, crop_lists[uu]))
    process_pool.close()
    process_pool.join()
    #with Pool(pool_size) as p:
    #    p.map(process_vid, crop_lists)
    print('Elapsed time: %.2f' % (timer() - start))
    
    # with mp.Pool(processes=pool_size) as p:
    #     _ = list(tqdm(p.imap_unordered(process_vid, crop_lists), total=len(crop_lists)))
    # print('Elapsed time: %.2f' % (timer() - start))
