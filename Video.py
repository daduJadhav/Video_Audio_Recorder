import cv2

class Video():
    def __init__(self):
        self.cap = cv2.VideoCapture(0) # this 0 is for th in-build camera, and VideoCapture id to take picture
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', fourcc, 20.00, (640 ,480)) # hear 20.00 is fps and (640,480 ) is for 480 px

    def record(self):
        # Defining the codec and create Video- Writer objective

        while True:
            sucess, frame = self.cap.read()

            self.out.write(frame)

            cv2.imshow('Origional Windows',frame) # hear Origional Windows is for just the first name and frame is the frame is to show

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    
        
















