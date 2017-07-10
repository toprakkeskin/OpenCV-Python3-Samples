import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0. kamera | 0 yerine 'dosyaadi' da gelebilir.
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Codec belirle.
# Video yazici olustur.
out = cv2.VideoWriter('../data/output1.avi',fourcc,20.0,(640,480))

while True:
	ret, frame = cap.read() # frame al
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # griye cevir
	
	out.write(frame) # renkli olani dosyaya yaz.
	
	cv2.imshow('frame',frame) # renkli olani ekrana bas
	cv2.imshow('gray',gray)   # gri olani ekrana bas

	# cikis icin q tusunu bekle.
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Objeleri serbest birak
cap.release()
out.release()
cv2.destroyAllWindows() # tum pencereleri kapat.
