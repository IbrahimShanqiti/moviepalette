
Allowed_Extensions = ['mp4']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Allowed_Extensions

  
def load_video(files): 
      
  if 'video' not in files:
      raise Exception('No video file found.')
  
  video = files['video']
  if video.filename == '':
      raise Exception('No video selected.')

  if not allowed_file(video.filename): 
      raise Exception('Invalid video file')
  
  return video