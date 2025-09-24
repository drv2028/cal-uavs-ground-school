import cv2

cap = cv2.VideoCapture("minecraft_stitch_test.mp4")

if (cap.isOpened() == False):
    print("Error")

frames = []
frame_count = 0
sample_rate = 10

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        if frame_count % sample_rate == 0:
            frames.append(frame)

    else:
        break

    frame_count += 1

cap.release()

stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)

status, stitched = stitcher.stitch(frames)

new_height, new_width = stitched.shape[:2]
result = cv2.resize(stitched, (int(0.3 * new_width), int(0.3 * new_height)))

cv2.imshow("Mosaic", result)
cv2.imwrite("stitched_result.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()