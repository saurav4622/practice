import tkinter as tk
from tkinter import messagebox
import cv2
import qrcode

class QRCodeScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")
        
        self.camera = cv2.VideoCapture(0)  # Initialize camera

        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        self.scan_button = tk.Button(root, text="Scan QR Code", command=self.scan_qr_code)
        self.scan_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.scan_qr_code()  # Start scanning immediately

    def scan_qr_code(self):
        ret, frame = self.camera.read()  # Read frame from camera

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color from BGR to RGB
            self.photo = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())  # Convert frame to PhotoImage
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            decoded_objects = cv2.QRCodeDetector().detectAndDecodeMulti(frame)
            for obj in decoded_objects[0]:
                self.show_qr_info(obj)

        self.root.after(10, self.scan_qr_code)  # Repeat scanning every 10 milliseconds

    def show_qr_info(self, qr_info):
        x, y, w, h = qr_info
        qr_data = qr_info[4]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, qr_data, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        messagebox.showinfo("QR Code Detected", qr_data)

    def close(self):
        self.camera.release()  # Release camera resource
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeScannerApp(root)
    root.mainloop()
