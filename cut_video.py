import json
import multiprocessing
import os
import shutil
import time

from tools import Logger, ms_to_time

'''
读取json文件，切割视频，调用ffmpeg命令：
ffmpeg -ss 01:00:00 -i input_file.mp4 -vcodec copy -acodec copy -t 00:06:00 output_file.mp4
-ss:起始时间
-t:分割时长
'''


SOURCE_DIR_JSON="data/jsons"
SOURCE_DIR_VID="data/videos"
DEST_DIR_VID="dataset/videos"
DEST_DIR_JSON="dataset/jsons"



# TODO
def cut(json_file):
    time.sleep(1)
    with open(os.path.join(SOURCE_DIR_JSON,json_file),"r") as f:
        results=json.load(f)
    videoname=results['filename']
    start=float(results['content']['start'])#ms
    end=float(results['content']['end'])#ms
    mid=float(results['content']['mid'])#ms
    
    tstart = ms_to_time(start)
    dur_long = ms_to_time(end-start)
    dur_short = ms_to_time(mid-start)

    prefix=os.path.splitext(json_file)[0]
    cmd = "ffmpeg -ss %s -i %s -vcodec copy -acodec copy -t %s  %s"%(tstart,os.path.join(SOURCE_DIR_VID,videoname),dur_long,
            os.path.join(DEST_DIR_VID,prefix+"-long.mp4"))
    cmd2 = "ffmpeg -ss %s -i %s -vcodec copy -acodec copy -t %s  %s"%(tstart,os.path.join(SOURCE_DIR_VID,videoname),dur_short,
            os.path.join(DEST_DIR_VID,prefix+"-short.mp4"))
    os.system(cmd)
    os.system(cmd2)
    shutil.copyfile(os.path.join(SOURCE_DIR_JSON,json_file),os.path.join(DEST_DIR_JSON,json_file))
    


if __name__ == "__main__":
    logger = Logger()
    if not os.path.exists(DEST_DIR_JSON):
        logger.warning("mkdir DEST_DIR_JSON:%s"%DEST_DIR_JSON)
        os.makedirs(DEST_DIR_JSON)
    if not os.path.exists(DEST_DIR_VID):
        logger.warning("mkdir DEST_DIR_VID:%s"%DEST_DIR_VID)
        os.makedirs(DEST_DIR_VID)

    files = os.listdir(SOURCE_DIR_JSON)
    pool = multiprocessing.Pool(processes=8)
    for f in files:
        cut(f)
        # pool.apply_async(cut, (f,))
    pool.close()
    pool.join()
    print("End")
