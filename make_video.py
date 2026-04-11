import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def generate_video():
    # .jpg లేదా .png ఫైళ్లను వెతకడం
    images = [img for img in os.listdir() if img.endswith(('.jpg', '.png', '.jpeg'))]
    images.sort()

    if not images or not os.path.exists("audio.mp3"):
        print("Error: Files not found! Please check image and audio.mp3 names.")
        return

    audio = AudioFileClip("audio.mp3")
    duration_per_image = audio.duration / len(images)

    clips = [ImageClip(m).set_duration(duration_per_image) for m in images]
    final_video = concatenate_videoclips(clips, method="compose")
    final_video = final_video.set_audio(audio)
    
    final_video.write_videofile("vishwanetra_video.mp4", fps=24, codec="libx264")
    print("Success: Video Created!")

if __name__ == "__main__":
    generate_video()
