# Mantendo estados dentro da classe.

class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def filming(self):
        if self.recording:
            print(f'{self.name} is already recording.')
            return
        print(f'{self.name} is recording...')
        self.recording = True

    def stop_recording(self):
        if not self.recording:
            print(f'{self.name} Is not recording.')
            return
        print(f'{self.name} is stopping recording...')
        self.recording = False

    def photographer(self):
        if self.recording:
            print(f"{self.name} is not photographer while recording.")
            return
        print(f"{self.name} is photographing...")

canon = Camera('Canon')
sony = Camera('Sony')

canon.filming()
canon.stop_recording()
canon.photographer()

print()

sony.stop_recording()
sony.filming()
sony.photographer()
sony.filming()
sony.stop_recording()
sony.photographer()