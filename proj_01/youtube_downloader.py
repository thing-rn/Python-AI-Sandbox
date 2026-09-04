import os
import yt_dlp
def download_video(url, output_folder="../content", cookies_file=None):
    os.makedirs(output_folder, exist_ok=True)
    ydl_opts = {
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "no_warnings": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0"
        }
    }
    if cookies_file:
        ydl_opts["cookiefile"] = cookies_file
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
if __name__ == "__main__":
    link = input("Enter YouTube URL: ")
    cookie_path = input("Cookie file path (leave empty to skip): ").strip()
    cookies = cookie_path if cookie_path else None
    download_video(link, cookies_file=cookies)
    print("Download complete!")
