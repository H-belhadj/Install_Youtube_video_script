import pytube

print('Download Video From Web By Python')
url = input('Enter Video URL: ')
pytube.YouTube(url).streams.get_highest_resolution().download()
