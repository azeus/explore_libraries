from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy import units as u
from astropy.coordinates import get_sun, get_moon
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class AstronomyTools:
    def __init__(self):
        # Default location (can be modified)
        self.location = EarthLocation(lat=40.7128 * u.deg, lon=-74.0060 * u.deg, height=0 * u.m)
        self.time = Time(datetime.utcnow())

    def set_location(self, latitude, longitude, height=0):
        """Set observation location."""
        self.location = EarthLocation(lat=latitude * u.deg,
                                      lon=longitude * u.deg,
                                      height=height * u.m)

    def get_celestial_positions(self):
        """Get current positions of the Sun and Moon."""
        frame = AltAz(obstime=self.time, location=self.location)

        # Get Sun position
        sun = get_sun(self.time)
        sun_altaz = sun.transform_to(frame)

        # Get Moon position
        moon = get_moon(self.time)
        moon_altaz = moon.transform_to(frame)

        return {
            'sun': {
                'altitude': sun_altaz.alt.deg,
                'azimuth': sun_altaz.az.deg
            },
            'moon': {
                'altitude': moon_altaz.alt.deg,
                'azimuth': moon_altaz.az.deg
            }
        }

    def plot_object_path(self, hours=24):
        """Plot the path of the Sun and Moon over specified hours."""
        times = [datetime.utcnow() + timedelta(hours=h) for h in range(hours)]
        times = Time(times)

        sun_alts = []
        moon_alts = []

        for t in times:
            frame = AltAz(obstime=t, location=self.location)
            sun_altaz = get_sun(t).transform_to(frame)
            moon_altaz = get_moon(t).transform_to(frame)

            sun_alts.append(sun_altaz.alt.deg)
            moon_alts.append(moon_altaz.alt.deg)

        plt.figure(figsize=(12, 6))
        plt.plot(range(hours), sun_alts, 'r-', label='Sun')
        plt.plot(range(hours), moon_alts, 'b-', label='Moon')
        plt.xlabel('Hours from now')
        plt.ylabel('Altitude (degrees)')
        plt.title('Sun and Moon Paths')
        plt.grid(True)
        plt.legend()
        plt.show()

    def calculate_night_duration(self):
        """Calculate duration of astronomical night (sun below -18 degrees)."""
        times = [datetime.utcnow() + timedelta(hours=h) for h in range(24)]
        times = Time(times)

        night_start = None
        night_end = None

        for i, t in enumerate(times):
            frame = AltAz(obstime=t, location=self.location)
            sun_altaz = get_sun(t).transform_to(frame)

            if sun_altaz.alt.deg < -18:
                if night_start is None:
                    night_start = i
            elif night_start is not None and night_end is None:
                night_end = i
                break

        if night_start is not None and night_end is not None:
            return night_end - night_start
        return 0


def main():
    # Example usage
    tools = AstronomyTools()

    # Set location (New York City)
    tools.set_location(40.7128, -74.0060)

    # Get current positions
    positions = tools.get_celestial_positions()
    print("\nCurrent celestial positions:")
    print(f"Sun - Altitude: {positions['sun']['altitude']:.2f}°, "
          f"Azimuth: {positions['sun']['azimuth']:.2f}°")
    print(f"Moon - Altitude: {positions['moon']['altitude']:.2f}°, "
          f"Azimuth: {positions['moon']['azimuth']:.2f}°")

    # Calculate night duration
    night_hours = tools.calculate_night_duration()
    print(f"\nDuration of astronomical night: {night_hours} hours")

    # Plot paths
    print("\nGenerating plot of Sun and Moon paths...")
    tools.plot_object_path()


if __name__ == "__main__":
    main()