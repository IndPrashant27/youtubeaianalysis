from yt_dlp import YoutubeDL
import os
from pathlib import Path

def download_vtt(video_url: str) -> str:
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'writesubtitles': True,
        'skip_download': True,
        'subtitleslangs': ['en'],
        'outtmpl': f'{output_dir}/%(id)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        video_id = info.get("id")
        vtt_path = f"{output_dir}/{video_id}.en.vtt"
        return vtt_path if os.path.exists(vtt_path) else ""

def vtt_to_text(vtt_path: str) -> str:
    lines = Path(vtt_path).read_text(encoding='utf-8').splitlines()
    return " ".join([
        line.strip()
        for line in lines
        if line and not line.startswith(("WEBVTT", "NOTE", "STYLE")) and "-->" not in line and not line.strip().isdigit()
    ])

def get_transcript_from_url(video_url: str) -> str:
    vtt_file = download_vtt(video_url)
    if not vtt_file:
        raise Exception("VTT file could not be downloaded.")
    return vtt_to_text(vtt_file)
