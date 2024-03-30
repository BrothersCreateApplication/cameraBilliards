from celery import shared_task
import cv2
import time
from .models import VideoSegment
from datetime import datetime, timedelta
from .models import VideoSegment

def consume_rtsp_stream(rtsp_url, output_file_prefix):
	cap = cv2.VideoCapture(rtsp_url)
	if not cap.isOpened():
		print(f'Failed to open RTSP stream: {rtsp_url}')
		return
    
	#total_duration = timedelta(minutes=60)
	interval_duration = timedelta(minutes=5)	
	start_time = datetime.now()
	end_time = start_time + timedelta(minutes=1)
 
 	# frame_width = int(cap.get(3))
	# frame_height = int(cap.get(4))
	frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	fps = cap.get(cv2.CAP_PROP_FPS)
	fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
 
	interval_start_time = start_time
	interval_end_time = interval_start_time + interval_duration
	interval_counter = 1
 
	outputStream = None
 
	while (datetime.now() < end_time):
		ret, frame = cap.read()
		if not ret:
			break
 
		if datetime.now() > interval_end_time:
			interval_counter += 1
			interval_start_time = interval_end_time
			interval_end_time = interval_start_time + interval_duration
            
			if outputStream:
				outputStream.release()
    
			filename = f'{output_file_prefix}_{interval_counter}.avi'
			outputStream = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))
   
			segment = VideoSegment.objects.create(
				description=f'Segment {interval_counter}',
          start_time=interval_start_time,
          end_time=interval_end_time,
          video_file=f'videos/{filename}'
        )
			segment.save()
		
		if outputStream:
			outputStream.write(frame)
  
	cap.release()
	if outputStream:
		outputStream.release()
	cv2.destroyAllWindows()
 
	return
# if not out.isOpened():
# 	return JsonResponse({'error': 'Failed to open VideoWriter!'}, status=500)