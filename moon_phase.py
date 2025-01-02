from datetime import datetime, timedelta
import math


class MoonPhaseCalculator:
    """Calculate moon phases for any given date"""

    def __init__(self):
        # Known new moon date as reference point
        self.new_moon_ref = datetime(2000, 1, 6, 18, 14)
        self.lunar_cycle = 29.53058867  # Days in lunar month

    def calculate_phase(self, date):
        """Calculate moon phase for given date"""
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")

        # Calculate days since reference new moon
        days_since = (date - self.new_moon_ref).total_seconds() / 86400

        # Calculate lunar age (days into lunar cycle)
        lunar_age = days_since % self.lunar_cycle

        # Calculate phase percentage (0 to 100)
        phase_percent = (lunar_age / self.lunar_cycle) * 100

        # Determine moon phase
        if lunar_age < 1.84566:
            phase_name = "New Moon"
            symbol = "🌑"
        elif lunar_age < 5.53699:
            phase_name = "Waxing Crescent"
            symbol = "🌒"
        elif lunar_age < 9.22831:
            phase_name = "First Quarter"
            symbol = "🌓"
        elif lunar_age < 12.91963:
            phase_name = "Waxing Gibbous"
            symbol = "🌔"
        elif lunar_age < 16.61096:
            phase_name = "Full Moon"
            symbol = "🌕"
        elif lunar_age < 20.30228:
            phase_name = "Waning Gibbous"
            symbol = "🌖"
        elif lunar_age < 23.99361:
            phase_name = "Last Quarter"
            symbol = "🌗"
        elif lunar_age < 27.68493:
            phase_name = "Waning Crescent"
            symbol = "🌘"
        else:
            phase_name = "New Moon"
            symbol = "🌑"

        illumination = self.calculate_illumination(lunar_age)

        return {
            "date": date.strftime("%Y-%m-%d"),
            "phase_name": phase_name,
            "symbol": symbol,
            "lunar_age": round(lunar_age, 2),
            "phase_percent": round(phase_percent, 2),
            "illumination": round(illumination, 2)
        }

    def calculate_illumination(self, lunar_age):
        """Calculate visible illumination percentage"""
        # Convert lunar age to angle
        angle = (lunar_age / self.lunar_cycle) * 2 * math.pi
        # Calculate illumination using cosine function
        return 50 * (1 - math.cos(angle))

    def get_next_phase(self, date, target_phase):
        """Find the next occurrence of a specific moon phase"""
        current_date = datetime.strptime(date, "%Y-%m-%d")
        max_days_to_check = 30  # Maximum days to look ahead

        for i in range(max_days_to_check):
            check_date = current_date + timedelta(days=i)
            phase_info = self.calculate_phase(check_date)
            if phase_info["phase_name"] == target_phase:
                return phase_info

        return None


# Example usage
if __name__ == "__main__":
    calculator = MoonPhaseCalculator()

    # Get current moon phase
    today = datetime.now()
    current_phase = calculator.calculate_phase(today)

    print(f"Moon Phase Calculator Results for {current_phase['date']}")
    print(f"Phase: {current_phase['symbol']} {current_phase['phase_name']}")
    print(f"Lunar Age: {current_phase['lunar_age']} days")
    print(f"Phase Percentage: {current_phase['phase_percent']}%")
    print(f"Illumination: {current_phase['illumination']}%")

    # Find next full moon
    next_full = calculator.get_next_phase(today.strftime("%Y-%m-%d"), "Full Moon")
    if next_full:
        print(f"\nNext Full Moon: {next_full['date']}")