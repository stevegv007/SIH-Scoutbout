from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
import os


class WebappVideo:

    def __init__(self):

        # -------------------------------------------------
        # Find the video file
        # -------------------------------------------------

        # __file__ = location of this Python file
        # This makes sure Python looks in the same folder
        # as Webapp_Video.py.
        folder = os.path.dirname(os.path.abspath(__file__))

        # Name of our temporary simulation video
        video_file = os.path.join(folder, "simulation_feed.mp4")


        # -------------------------------------------------
        # Create the video player
        # -------------------------------------------------

        self.player = QMediaPlayer()

        # Handles the video's audio
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)


        # -------------------------------------------------
        # Create the video display
        # -------------------------------------------------

        # This is the actual widget that shows the video
        self.video_widget = QVideoWidget()

        # Tell the player to display the video here
        self.player.setVideoOutput(self.video_widget)


        # -------------------------------------------------
        # Load the video
        # -------------------------------------------------

        self.player.setSource(
            QUrl.fromLocalFile(video_file)
        )


        # -------------------------------------------------
        # Loop the video forever
        # -------------------------------------------------

        # When the video reaches the end,
        # start it again from the beginning.
        self.player.mediaStatusChanged.connect(
            self.video_finished
        )


        # Start playing immediately
        self.player.play()


    # -----------------------------------------------------
    # Restart the video when it finishes
    # -----------------------------------------------------

    def video_finished(self, status):

        if status == QMediaPlayer.MediaStatus.EndOfMedia:

            # Start the video again from the beginning
            self.player.setPosition(0)

            self.player.play()


    # -----------------------------------------------------
    # Pause the video
    # -----------------------------------------------------

    def pause(self):
        self.player.pause()


    # -----------------------------------------------------
    # Play / resume the video
    # -----------------------------------------------------

    def play(self):
        self.player.play()


    # -----------------------------------------------------
    # Stop the video
    # -----------------------------------------------------

    def stop(self):
        self.player.stop()
