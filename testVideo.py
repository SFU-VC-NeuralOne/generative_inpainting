import cv2

cap = cv2.VideoCapture('hall_objects_qcif.y4m')
frame_list = []

i = 0
# loop through all the frames and store them in a list
while (i < 330):
    # Capture frame-by-frame
    i += 1
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(i)
    frame_list.append(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(10)

print(frame_list[0].shape)



