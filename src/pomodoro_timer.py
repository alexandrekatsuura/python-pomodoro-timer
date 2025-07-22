import time
import os
import simpleaudio as sa

class PomodoroTimer:
    """
    A Pomodoro Timer class to manage work and break sessions with sound notifications.
    """
    
    def __init__(self, work_minutes=25, short_break_minutes=5, long_break_minutes=15, cycles=4):
        """
        Initializes the PomodoroTimer with specified durations and cycles.

        Args:
            work_minutes (int): Duration of a work session in minutes.
            short_break_minutes (int): Duration of a short break in minutes.
            long_break_minutes (int): Duration of a long break in minutes.
            cycles (int): Number of work/short break cycles before a long break.
        """
        if not all(isinstance(arg, int) and arg > 0 for arg in [work_minutes, short_break_minutes, long_break_minutes, cycles]):
            raise ValueError("All durations and cycles must be positive integers.")

        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes
        self.cycles = cycles
        self.current_cycle = 0

    def _play_sound(self):
        """
        Plays a sound notification. This is a placeholder and needs platform-specific implementation.
        """
        print("\n--- Sound Notification! ---\n")
        wave_obj = sa.WaveObject.from_wave_file("notification.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def _countdown(self, minutes, session_type):
        """
        Counts down the specified minutes for a given session type.

        Args:
            minutes (int): The duration of the session in minutes.
            session_type (str): The type of session (e.g., 'Work', 'Short Break', 'Long Break').
        """
        seconds = minutes * 60
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(f'\r{session_type} Session: {timer}', end="")
            time.sleep(1)
            seconds -= 1
        self._play_sound()

    def start_timer(self):
        """
        Starts the Pomodoro timer, cycling through work and break sessions.
        """
        print("Pomodoro Timer Started!")
        while True:
            self.current_cycle += 1
            print(f"\n--- Cycle {self.current_cycle} of {self.cycles} ---")

            # Work Session
            self._countdown(self.work_minutes, "Work")
            print("Work session finished!")

            if self.current_cycle % self.cycles == 0:
                # Long Break
                print("\n--- Starting Long Break ---")
                self._countdown(self.long_break_minutes, "Long Break")
                print("Long break finished!")
                self.current_cycle = 0 # Reset cycles after a long break
            else:
                # Short Break
                print("\n--- Starting Short Break ---")
                self._countdown(self.short_break_minutes, "Short Break")
                print("Short break finished!")

            input("Press Enter to start the next session or Ctrl+C to quit.")