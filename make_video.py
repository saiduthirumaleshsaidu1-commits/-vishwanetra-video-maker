import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def generate_video():
    # అన్ని .jpg ఫైళ్లను తీసుకోవడం
    images = sorted([img for img in os.listdir() if img.endswith(".jpg")])
    
    if not images or not os.path.exists("audio.mp3"):
        print("Error: ఫోటోలు (image.jpg) లేదా ఆడియో (audio.mp3) దొరకలేదు!")
        return

    audio = AudioFileClip("audio.mp3")
    duration_per_image = audio.duration / len(images)

    clips = [ImageClip(m).set_duration(duration_per_image) for m in images]
    final_video = concatenate_videoclips(clips, method="compose")
    final_video = final_video.set_audio(audio)
    
    final_video.write_videofile("vishwanetra_video.mp4", fps=24, codec="libx264")
    print("వీడియో సిద్ధమైంది!")

if __name__ == "__main__":
    generate_video()
