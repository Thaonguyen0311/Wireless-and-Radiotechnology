# Example Device: Nordic nRF52832
Datasheet: https://docs.nordicsemi.com/bundle/nRF52832_PS_v1.9/resource/nRF52832_PS_v1.9.pdf
<img width="199" height="253" alt="image" src="https://github.com/user-attachments/assets/4a716474-e718-4137-b657-f99a223837cc" />

## RF System Blocks Explanation
### 1. Information Source / MCU

The MCU generates digital data to be transmitted or processes received data.
It controls the RF transceiver and manages communication protocols such as Bluetooth Low Energy.

### 2. RF Transceiver (Tx/Rx)

The RF transceiver converts signals between baseband and RF frequencies.
It includes both transmitter and receiver paths, enabling wireless communication.

### 3. Modulation / Demodulation

Modulation converts digital data into RF signals (e.g., GFSK in BLE).
Demodulation extracts the original data from the received RF signal.

### 4. Power Amplifier (PA)

The PA increases the power of the transmitted RF signal.
This ensures the signal can travel longer distances through the antenna.

### 5. Low Noise Amplifier (LNA)

The LNA amplifies weak incoming RF signals with minimal added noise.
It improves receiver sensitivity and signal quality.

### 6. RF Filtering / Matching Network

This block filters unwanted frequencies and matches impedance between components.
It ensures maximum power transfer and reduces signal reflections.

### 7. Antenna Interface

The antenna interface connects the RF circuitry to the antenna.
It radiates transmitted signals and captures incoming RF signals.

### 8. Power Supply for RF Section

Provides stable voltage to RF components such as PA and LNA.
Clean power is critical to avoid noise affecting RF performance.
