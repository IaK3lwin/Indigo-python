from pytube import YouTube


def mp3(url: str = 'none', path: str = 'none'):
    def on_process():
        print('in progress..')
        ...
    def on_complete():
        ...
    
    video = YouTube(url,
                    on_progress_callback=on_process,
                    on_complete_callback=on_complete).streams.filter(file_extension='mp3')
    
    print(video)
    def title():
       return video.title
    
    return {'title' : title()}

d = mp3('https://www.youtube.com/shorts/bOUZUfDjTh8', 'video')
