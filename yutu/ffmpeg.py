import os,sys,time,os.path
from pytube import YouTube, Stream, helpers
from pytube.cli import (
    _ffmpeg_downloader as downloaders,
    _unique_name as fileUnique,
    _download as clidownload
    )
from warna import prRed, prGreen
import subprocess
from helpers import s
class RewriteFunction(object):
    """
    Fungsi ini untuk menulis ulang fungsi-fungsi yang telah disediakan
    """
    def Downloaderffmpeg(
        self, audio_stream: Stream, video_stream: Stream, target: str 
    )-> str:
        video_unique_name = fileUnique(
            helpers.safe_filename(video_stream.title),
            video_stream.subtype,
            "video",
            target=target,
        )

        audio_unique_name = fileUnique(
            helpers.safe_filename(video_stream.title),
            audio_stream.subtype,
            "audio",
            target=target,
        )

        clidownload(stream=video_stream, target=target, filename=video_unique_name)
        clidownload(stream=audio_stream, target=target, filename=audio_unique_name)

        video_path = os.path.join(
            target, f"{video_unique_name}.{video_stream.subtype}"
        )
        audio_path = os.path.join(
            target, f"{audio_unique_name}.{audio_stream.subtype}"
        )
        final_path = os.path.join(
            # target, f"{helpers.safe_filename(video_stream.title)}.{video_stream.subtype}"
            target, f"{helpers.safe_filename(video_stream.title)}.mp4"
        )

        try:
            subprocess.run(  
                [
                    "ffmpeg",
                    "-i",
                    video_path,
                    "-i",
                    audio_path,
                    "-codec",
                    "copy",
                    final_path,
                    "-loglevel",
                    "quiet"
                ]
            )
        except:
            print("Ada kesalahan saat menggabungkan video")
            sleep(0.5)
            print("Tapi tenang, file video dan audio masih ada")            
        finally:
            print(s("%s" % prGreen("Success")))
            print(s("File disimpan di %s" % prGreen(final_path)))

            os.unlink(video_path)
            os.unlink(audio_path)
            return final_path

        return None

    def DownloadMP3(self, audio_stream: Stream, target: str):
        """ Untuk download mp3 """
        audio_unique_name = fileUnique(
            helpers.safe_filename(audio_stream.title),
            audio_stream.subtype,
            "audio",
            target=target,
        )
        clidownload(stream=audio_stream, target=target, filename=audio_unique_name)
        
        audio_path = os.path.join(
            target, f"{audio_unique_name}.{audio_stream.subtype}"
        )
        
        final_path = os.path.join(
            target, f"{helpers.safe_filename(audio_stream.title)}.mp3"
        )

        try:
            subprocess.run(  
                [
                    "ffmpeg",
                    "-i",
                    audio_path,
                    "-b:a",
                    "192K",
                    "-vn",
                    final_path,
                    "-loglevel",
                    "quiet"
                ]
            )
        except:
            print("Ada kesalahan saat menggabungkan video")
            sleep(0.5)
            print("Tapi tenang, file udio masih ada")            
        finally:
            print("File berhasil di didownload")
            print("File disimpan di \n",final_path)

            os.unlink(audio_path)
            return final_path

        return None
