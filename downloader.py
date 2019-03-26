def main():
  import time
  import pytube
  import tkinter
  import sys
  from tkinter.filedialog import askdirectory
  from tkinter import messagebox

  print("put the the link of the video you would like to download (enter link and press enter once and then wait)")
  link = input()

  print("|\n-------------------------------------------------------------------------------------------------------\nNOTE: sometimes the video may not be available or you might get a 404 or 403 error code, 99% of the time these errors are from youtube, so if you get a 404 error you should try downloading again and it should work\n-------------------------------------------------------------------------------------------------------\n|")
  youtube = pytube.YouTube(link)

  def show_progress_bar(stream, _chunk, _file_handle, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('|\n |{bar}| {percent}%\r'.format(bar=status, percent=percent)) #rm string
    sys.stdout.flush()

  youtube.register_on_progress_callback(show_progress_bar)

  result = 1

  #  select format

  ans = messagebox.askquestion("download audio or video?", "click yes if you want audio only, click no if you want video only")

  if ans == 'yes':
    videos = youtube.streams.filter(only_audio=True).all()
    for video in videos:
      print(str(result) + ", " + str(video))
      result += 1

  if ans == 'no':
    videos = youtube.streams.filter(only_video=True).all()
    for video in videos:
      print(str(result) + ", " + str(video))
      result += 1

  print("\nchoose a number according to the quality you want, choosing a vcodec of 'avc1' may result in an error\n")

  number = int(input())
  vid = videos[number - 1]

  messagebox.showinfo("save where?", "choose a directory to save to")
  mainDir = askdirectory()

  # download start

  start = time.time()

  vid.download(mainDir)

  elapsed_time = time.time() - start

  messagebox.showinfo("Done", "your video was downloaded successfully")

  print(youtube.title + " successfully donwloaded to " + mainDir) 
  print("time taken to download: (hh:mm:ss)",time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

  restart = messagebox.askquestion("Restart?", "you wanna download another video?")
  if restart == 'yes':
    main()

  if restart == 'no':
    exit()  

main()      