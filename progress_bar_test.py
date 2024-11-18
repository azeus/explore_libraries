from progress.bar import Bar
from progress.bar import ChargingBar
from progress.spinner import Spinner
from progress.spinner import MoonSpinner

import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()

chrging = ChargingBar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    chrging.next()
chrging.finish()

spin = Spinner('Processing', max=20)
for i in range(20):
    time.sleep(1)
    spin.next()
spin.finish()


moonspin = MoonSpinner('Processing', max=20)
for i in range(20):
    time.sleep(1)
    moonspin.next()
moonspin.finish()