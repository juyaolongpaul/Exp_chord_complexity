import pyaudio
import threading
import Queue
import wave
import numpy as np
import time
import sys,os


class PlayerWorker(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.cmdQ = q
        self.p = pyaudio.PyAudio()
    def __del__(self):
        if "wf" in dir(self):
            self.wf.close()
        self.p.terminate()
    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        print ("normal callback, data's length =", len(data))
        return (data, pyaudio.paContinue)
    def playBufferCallback(self, in_data, frame_count, time_info, status):
        global index
        if index + frame_count * self.wf1.getsampwidth() >= len(self.data):
            i = index
            index = 0
            print ("callback end")
            return (self.data[i:-1], pyaudio.paAbort)
        else:
            data = self.data[index:index + frame_count * self.wf1.getsampwidth()]
            index += frame_count * self.wf1.getsampwidth()
            print ("callback continue: index = ", index)
            return (data, pyaudio.paContinue)

    def run(self):
        while(True):
            cmdString = self.cmdQ.get()
            command = eval(cmdString)
            if command[0] == "STOP":
                if "stream" in dir(self):
                    # self.stream.stop_stream()
                    self.stream.close()
                else:
                    pass

            elif command[0] == "PLAY":
                if "stream" in dir(self):
                    # self.stream.stop_stream()
                    self.stream.close()
                self.waveFileName = command[1]
                self.wf = wave.open(self.waveFileName, 'rb')
                self.stream = self.p.open(format = self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels = self.wf.getnchannels(),
                        rate = self.wf.getframerate(),
                        output = True,
                        stream_callback = self.callback)

            elif command[0] == "PLAY2":
                global index
                index = 0
                if "stream" in dir(self):
                    self.stream.close()
                self.wf1 = wave.open(command[1], 'rb')
                self.wf2 = wave.open(command[2], 'rb')
                params1 = self.wf1.getparams()
                params2 = self.wf2.getparams()
                fs = params1[2]
                nframes1 = params1[3]
                nframes2 = params2[3]
                data1 = self.wf1.readframes(nframes1)
                data2 = self.wf2.readframes(nframes2)
                wave_data1 = np.fromstring(data1, dtype=np.int16)
                zero_pad = np.zeros(0.5 * fs, dtype=np.int16)
                wave_data2 = np.fromstring(data2, dtype=np.int16)
                wave_data = np.concatenate((wave_data1, zero_pad, wave_data2))
                self.data = wave_data.tostring()
                self.stream = self.p.open(format = self.p.get_format_from_width(self.wf1.getsampwidth()),
                        channels = self.wf1.getnchannels(),
                        rate = self.wf1.getframerate(),
                        output = True,
                        stream_callback = self.playBufferCallback)


class Player:
    def __init__(self):
        global index
        index = 0
        self.cmdQ = Queue.Queue()        # Command queue
        self.worker = PlayerWorker(self.cmdQ) # Real player worker thread
        self.worker.start()

    def playFile(self, fileName):
        self.fileName = fileName
        self.cmdQ.put("%r" % ["PLAY", fileName])

    def playTwoFile(self, fileName1, fileName2):
        self.fileName1 = fileName1
        self.fileName2 = fileName2
        self.cmdQ.put("%r" % ["PLAY2", fileName1, fileName2])
        
    def stopPlay(self):
        self.cmdQ.put("%r" % ["STOP"])

