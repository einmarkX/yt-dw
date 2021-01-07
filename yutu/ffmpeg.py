import os,sys,time,os.path
from pytube import YouTube, Stream, helpers
from pytube.cli import (
    _ffmpeg_downloader as downloaders,
    _unique_name as fileUnique,
    # _download as clidownload
    )
from warna import prRed, prGreen
import subprocess
from helpers import s

import argparse
import datetime as dt
import gzip
import json
import logging
import os
import shutil
import subprocess  # nosec
import sys
from typing import List
from typing import Optional

from pytube import __version__
from pytube import CaptionQuery
from pytube import Playlist
from pytube import Stream
from pytube import YouTube
from pytube.exceptions import PytubeError
from pytube.helpers import safe_filename
from pytube.helpers import setup_logger


# def on_progress(
#         stream: Stream, chunk: bytes, bytes_remaining: int
#     ) -> None:  # pylint: disable=W0613
#         filesize = stream.filesize
#         bytes_received = filesize - bytes_remaining
#         print(f'Filesizenya {filesize}')
#         RewriteFunction.display_progress_bar(bytes_received, filesize)

class RewriteFunction(object):
    """
    Fungsi ini untuk menulis ulang fungsi-fungsi yang telah disediakan
    """


    """ Mulai dari sini """
    def on_progress(
        self, stream: Stream, chunk: bytes, bytes_remaining: int
    ) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        self.display_progress_bar(bytes_received, filesize)

    def display_progress_bar(
        self, bytes_received: int, filesize: int, ch: str = "█", scale: float = 0.55
    ) -> None:
        columns = shutil.get_terminal_size().columns
        max_width = int(columns * scale)

        filled = int(round(max_width * bytes_received / float(filesize)))
        remaining = max_width - filled
        progress_bar = ch * filled + " " * remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        text = f" ↳ |{progress_bar}| {percent}%\r"
        sys.stdout.write(text)
        sys.stdout.flush()

    def _download(
        self,
        stream: Stream,
        target: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> None:
        filesize_megabytes = stream.filesize // 1048576
        # print(f"{filename or stream.default_filename} | {filesize_megabytes} MB")
        file_path = stream.get_file_path(filename=filename, output_path=target)
        if stream.exists_at_path(file_path):
            print(f"Already downloaded at:\n{file_path}")
            return

        stream.download(output_path=target, filename=filename)
        sys.stdout.write("\n")
    """ Sampai sini """

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

        self._download(stream=video_stream, target=target, filename=video_unique_name)
        self._download(stream=audio_stream, target=target, filename=audio_unique_name)

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
            print(s("File disimpan di" ))
            print(s("%s" % prGreen(final_path)))

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
        self._download(stream=audio_stream, target=target, filename=audio_unique_name)
        
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
