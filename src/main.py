from pomodoro_timer import PomodoroTimer

class Main:
    def __init__(self):
        self._pomodoro_timer = PomodoroTimer()
        
    def run(self):
        """Main function to run the Pomodoro Timer."""
        try:
            self._pomodoro_timer.start_timer()
        except KeyboardInterrupt:
            print("\nPomodoro Timer stopped.")


if __name__ == "__main__":
    main = Main()
    main.run()
