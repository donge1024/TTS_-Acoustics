import os


def mp4_to_wav(mp4_path, wav_path, sampling_rate):
    """
    mp4 转 wav
    :param mp4_path: .mp4文件路径
    :param wav_path: .wav文件路径
    :param sampling_rate: 采样率
    :return: .wav文件
    """
    # 如果存在wav_path文件，先删除。
    if os.path.exists(wav_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(wav_path)
        # 终端命令
    command = "ffmpeg -i {} -ac 1 -ar {} {} && y".format(mp4_path, sampling_rate, wav_path)
    print('命令是：',command)
    # 执行终端命令
    os.system(command)


if __name__ == '__main__':
    filePath = r'D:\FastSpeech2-master\obm\ed'
    mp4_file = os.listdir(filePath)
    for filename in range(len(mp4_file)):
        print('D:\FastSpeech2-master\obm\ed\%s'%filename)

        mp4_path = os.getcwd() + r'\%filename.mp4'
        wav_path = os.getcwd() + r'\%filename.wav'
        sampling_rate = 16000
        mp4_to_wav(mp4_path, wav_path, sampling_rate)
