# BLE Networks Analysis with BLE Scanner

## 📷 Scanning Results

<img src="https://github.com/user-attachments/assets/29a64134-d5a7-492a-8edb-ce5446f1d2c3" width="300"/>

<img src="https://github.com/user-attachments/assets/d914082d-d473-4ad0-8c9a-8b4aee03bdd4" width="300"/>

## 1. Relationship Between RSSI and Estimated Distance

### Observation

There is a clear inverse relationship between RSSI and estimated distance:

- **Higher RSSI (e.g., -72 dBm)** → Short distance (~1.26 m)  
- **Lower RSSI (e.g., -95 dBm)** → Long distance (~17.78 m)

This confirms the theoretical **log-distance path loss model**.

However, the relationship is not perfectly linear:

- -81 dBm → 3.55 m  
- -82 dBm → 3.98 m  
- -83 dBm → 4.47 m  

A difference of only 1 dBm results in noticeable variation in estimated distance due to the logarithmic nature of signal attenuation.


## 2. Number and Types of BLE Devices

### Device Types Observed

- Multiple Apple devices (anonymous advertising, no device name)
- One device labeled **"Fridge"** (likely IoT appliance)
- One Windows-based device
- Several unidentified non-connectable advertisers

### Observations

- Most devices show **"N/A"** as name (privacy protection).
- Many devices are marked **Non-Connectable**, meaning:
  - They only broadcast advertising packets.
  - They do not allow direct connections.

This suggests that most detected devices are:

- Smartphones  
- Wearables  
- IoT devices  
- Background BLE advertisers  

## 3. Patterns and Inconsistencies

### 3.1 RSSI Fluctuation

Devices around -82 dBm show slightly different estimated distances (3.98 m vs 4.47 m).

Possible reasons:

- Multipath propagation  
- Human movement  
- Antenna orientation  
- WiFi interference (2.4 GHz band overlap)  

### 3.2 Advertising Interval Differences

Observed advertising intervals:

- 58 ms  
- 73 ms  
- 435 ms  
- 2501 ms  
- 3945 ms  

**Interpretation:**

- Short interval (e.g., 58 ms) → frequent advertising → higher energy consumption  
- Long interval (e.g., 3945 ms) → power-saving mode (likely battery-powered IoT device)

This reflects different design priorities:

- Smartphones → moderate advertising interval  
- IoT sensors → long interval for battery efficiency  

## 4. Environmental Impact Factors

### 4.1 Transmission Power

Devices may use different transmission power (TxPower) levels.

Two devices at similar distances may show different RSSI values due to:

- Hardware design differences  
- Manufacturer configuration  
- Power-saving modes  


### 4.2 Physical Obstructions

Indoor environments typically contain:

- Walls  
- Furniture  
- Metal structures  
- Human bodies  

Human bodies can attenuate BLE signals by approximately 3–10 dB, which explains sudden RSSI drops.


### 4.3 Environmental Noise and Interference

BLE operates in the **2.4 GHz ISM band**, which is also used by:

- WiFi  
- Microwave ovens  
- Other Bluetooth devices  

Interference can cause:

- RSSI fluctuations  
- Packet loss  
- Temporary signal degradation  


## 5. Security and Privacy Considerations

### 5.1 Everyday Use of BLE

BLE is widely used in:

- Wearables (smartwatches, fitness trackers)  
- Smart home devices (e.g., smart fridge, sensors)  
- Beacons (retail tracking systems)  
- Asset tracking tags  
- Smartphones (background advertising)  

### 5.2 Device Tracking Risk

Even when device names are hidden, tracking may still be possible through:

- Public MAC addresses  
- Persistent identifiers  
- Advertising behavior patterns  

This enables potential long-term monitoring of device presence.


### 5.3 Identifier Exposure

If a device uses a static public MAC address, attackers can:

- Identify the manufacturer via OUI lookup  
- Track user movement across locations  

Although modern devices often use randomized MAC addresses, privacy risks still exist.


### 5.4 Writeable Generic Attribute Profile (GATT)

![GATT Example 1](https://github.com/user-attachments/assets/b8970fef-9db8-4a04-9fa7-516a75cd0004)  
![GATT Example 2](https://github.com/user-attachments/assets/4c6747d7-4c19-4339-a715-3c60f509ccc3)

An example device (Tapo Smart IoT plug) exposed a vendor-specific GATT characteristic (UUID: 0x8883) with write permissions.

This represents a potential attack surface, particularly if authentication and authorization mechanisms are insufficient.

Writeable characteristics may allow:

- Unauthorized configuration changes  
- Command injection  
- Device misuse  


## 6. Overall Conclusion

The experimental results confirm that:

1. RSSI decreases as distance increases, following a logarithmic relationship.  
2. Indoor environments introduce signal fluctuations due to:
   - Obstructions  
   - Reflection  
   - Interference  
3. Advertising intervals vary significantly across device types.  
4. BLE technology presents privacy and security risks due to passive detectability and identifier exposure.

RSSI-based distance estimation is suitable for proximity detection but not for precise localization.
