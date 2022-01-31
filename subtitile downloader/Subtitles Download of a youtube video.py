from youtube_transcript_api import YouTubeTranscriptApi

video_id=input("Enter Video Id: ")
try:
    transcript_list=YouTubeTranscriptApi.list_transcripts(video_id="vQQEaSnQ_bs")
    transcript=transcript_list.find_transcript(['en'])
    list=transcript.fetch()

# Save subtitles using file handling
    for Text in list:
        with open('corey_schafer_subtitles.txt','a+') as f:
            f.write(Text['text'])
            f.write(' ')
        
except Exception as e:
    print("Error:",e)
        

