# Label tool for VLI implemented by PyQt5

1. 从youtube下载视频:  
    [download website](https://en.savefrom.net/)   
    在Label文件夹下，手动创建data/videos文件夹或者执行下面命令 
    ```
    mkdir -p data/videos
    ```
    例如下载https://www.youtube.com/watch?v=Hrj60-7EQnY ,**取url的v=后面字段，文件名保存为Hrj60-7EQnY.mp4**,保存到data/videos目录下  



2. 标注  
    手动创建文件夹data/jsons或者执行下面命令
    ```
    mkdir -p data/jsons
    ```
    启动标注程序:
    ```
    python demo.py
    ```
    选取data/videos目录下视频开始标注，标注结果会保存到data/jsons  
    **!!! 只有在视频pause状态下点击record按钮才会记录当前时间点**


3. 视频切割  
    多进程切割视频(需要系统安装ffmepg命令):
    ```
    python cut_video.py
    ```
    切割结果会保存到dataset/videos和dataset/jsons目录下

