1. Difference between time domain and frequency domain

Time domain describes how a signal varies over time.

The x-axis is time (seconds).

Amplitude, pulses, delays, rise/fall times, noise in time can be seen

Frequency domain describes how a signal’s energy is distributed across frequencies.

The x-axis is frequency (Hz).

Frequency domain is essential for bandwidth, filtering, interference, and modulation analysis.

2. Why does filtering help in RF receivers?

Filtering is critical in RF receivers because it:

Selects the desired signal

A band-pass filter allows only the wanted frequency band to pass.

Prevents nearby channels from interfering.

Reduces noise

Thermal noise is spread across frequency.

Filtering limits noise bandwidth, improving signal-to-noise ratio (SNR).

Prevents receiver overload

Strong out-of-band signals can saturate amplifiers or mixers.

Filters protect sensitive RF stages.

Improves demodulation accuracy

Removing unwanted frequency components leads to cleaner baseband signals.

3. What does modulation achieve in an RF system?

Modulation shifts a baseband (low-frequency) signal onto a high-frequency carrier.

This achieves several goals:

Enables wireless transmission

Antennas efficiently radiate high-frequency signals, not DC or audio-range signals.

Allows frequency multiplexing

Multiple users can transmit simultaneously at different carrier frequencies.

Improves propagation characteristics

Higher frequencies can be directed, reflected, or penetrate environments differently.

Separates signals in the spectrum

Prevents different transmitters from overlapping.

4. Typically, the low-pass filter is the easiest to design because:

It has only one cutoff frequency.

Component values are straightforward to calculate.

No need to control both upper and lower passband edges.

Stable and predictable behavior with minimal sensitivity to component tolerances.

In contrast:

Band-pass and band-stop filters require precise control of two cutoff frequencies.

High-pass filters are slightly more sensitive to component variations at low frequencies.

5. From A3: Where do the new frequency components appear after modulation?

After modulation (especially amplitude modulation):

New frequency components appear at:

𝑓𝑐±𝑓𝑚

These are called sidebands:

Upper Sideband (USB): 
𝑓𝑐+𝑓𝑚

Lower Sideband (LSB): 
𝑓𝑐−𝑓𝑚
