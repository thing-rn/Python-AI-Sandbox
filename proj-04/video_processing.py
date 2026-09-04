# video_processing.py
from moviepy import VideoFileClip

def process_video(path):
    clip = VideoFileClip(path)
    clip.audio.write_audiofile("audio_extracted.mp3")
    trimmed = clip.subclip(0, 10)
    trimmed.write_videofile("trimmed_video.mp4")

if __name__ == "__main__":
    video_path = input("Enter video file path: ")
    process_video(video_path)
    print("Processing complete!")