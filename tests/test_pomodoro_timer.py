import pytest
from src.pomodoro_timer import PomodoroTimer

class TestPomodoroTimer:
    """
    Unit tests for the PomodoroTimer class.
    """

    def test_initialization_valid_parameters(self):
        """
        Tests that the PomodoroTimer initializes correctly with valid parameters.
        """
        timer = PomodoroTimer(work_minutes=25, short_break_minutes=5, long_break_minutes=15, cycles=4)
        assert timer.work_minutes == 25
        assert timer.short_break_minutes == 5
        assert timer.long_break_minutes == 15
        assert timer.cycles == 4
        assert timer.current_cycle == 0

    def test_initialization_default_parameters(self):
        """
        Tests that the PomodoroTimer initializes correctly with default parameters.
        """
        timer = PomodoroTimer()
        assert timer.work_minutes == 25
        assert timer.short_break_minutes == 5
        assert timer.long_break_minutes == 15
        assert timer.cycles == 4
        assert timer.current_cycle == 0

    def test_initialization_invalid_parameters(self):
        """
        Tests that the PomodoroTimer raises ValueError for invalid parameters.
        """
        with pytest.raises(ValueError, match="All durations and cycles must be positive integers."):
            PomodoroTimer(work_minutes=0)
        with pytest.raises(ValueError, match="All durations and cycles must be positive integers."):
            PomodoroTimer(short_break_minutes=-5)
        with pytest.raises(ValueError, match="All durations and cycles must be positive integers."):
            PomodoroTimer(cycles="abc")


