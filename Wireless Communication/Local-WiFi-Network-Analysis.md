

# Local Wi-Fi Network Analysis
## 1. Introduction
The objective of this assignment is to analyze the performance and configuration of a local wireless network using the Network Analyzer mobile application. The analysis focuses on key network parameters including signal strength, latency, IP configuration, operating channel, security type, and nearby network interference. Furthermore, potential performance issues are identified and practical recommendations for improvement are proposed.
## 2. Measurement Setup
Device: Android smartphone
Operating System: Android
Application Used: Network Analyzer
Location: Indoor residential environment
Frequency Band: 2.4 GHz
## 3. Network Configuration Details
### 3.1 Active Connection Information
•	SSID: 74DA38FAAB8F
•	BSSID: 74:da:38:fa:ab:8f
•	Vendor: Edimax Technology Co. Ltd.
•	IP Address: 192.168.2.101
•	Subnet Mask: 255.255.255.0
•	Default Gateway: 192.168.2.1
•	DNS Servers: 83.218.160.135, 172.30.3.254
•	DHCP Lease Time: 3650 days
•	Frequency Band: 2.4 GHz
•	Security Type: WPA2 (AES)
### 3.2 Network Topology Observation
The IP address range (192.168.2.0/24) indicates a private IPv4 local area network. The default gateway (192.168.2.1) corresponds to the wireless router. DHCP is enabled, automatically assigning IP addresses to connected devices.
## 4. Wireless Environment Analysis
<img width="922" height="2048" alt="image" src="https://github.com/user-attachments/assets/eb8b0306-9984-437e-a73d-152a53161162" />
<img width="922" height="2048" alt="image" src="https://github.com/user-attachments/assets/3a3e294e-f884-4a7f-9c4c-6a95d95ac51e" />
### 4.1 Signal Strength
Measured signal strength of the connected network:
•	−50 dBm
Signal strength classification:
Signal Level	Quality
-30 to -50 dBm	Excellent
-50 to -60 dBm	Very Good
-60 to -70 dBm	Acceptable
Below -75 dBm	Weak
The measured value of −50 dBm indicates excellent signal quality at the measurement location.
### 4.2 Nearby Wi-Fi Networks
Several nearby networks were detected on the 2.4 GHz band:
Channel	Signal Strength	Channel Width	Security
5	-50 dBm	20 MHz	WPA2
3	-50 dBm	20 MHz	WPA2
3	-53 dBm	40 MHz	WPA2/WPA
7	-60 dBm	40 MHz	WPA2
7	-65 dBm	40 MHz	WPA2/WPA
9	-65 dBm	40 MHz	WPA2/WPA
1	-65 dBm	20 MHz	Unknown

## 5. Channel and Interference Analysis
The network operates on the 2.4 GHz band, which has only three non-overlapping channels:
•	Channel 1
•	Channel 6
•	Channel 11
However, the detected neighboring networks are using channels 3, 5, 7, and 9, which significantly overlap with each other.
Identified Issues:
1.	Heavy channel overlap in the 2.4 GHz band.
2.	Multiple networks using 40 MHz channel width, increasing interference.
3.	High probability of congestion due to shared frequency space.
Channel overlap can lead to:
•	Increased latency
•	Reduced throughput
•	Packet retransmissions
•	Network instability during peak usage
## 6. Security Evaluation
The connected network uses WPA2 (AES) encryption.
Security assessment:
•	WPA2 (AES) → Secure and widely accepted standard.
•	WPA/WPA2 mixed mode → Less secure.
•	WPA3 → More secure (recommended if supported).
The current configuration provides adequate security; however, upgrading to WPA3 would enhance protection against modern attacks.
## 7. Potential Performance Issues
Based on the collected data, the following potential issues were identified:
1.	High channel congestion in the 2.4 GHz band.
2.	Overlapping channel usage by neighboring networks.
3.	Use of 40 MHz width in a crowded spectrum.
4.	Exclusive use of 2.4 GHz instead of 5 GHz band.
Although signal strength is excellent at the measurement point, interference may still reduce actual throughput and increase latency.
## 8. Improvement
1.	Switch to 5 GHz band (if supported by router and devices).
2.	Manually set channel to 1, 6, or 11 to avoid overlap.
3.	Reduce channel width to 20 MHz in congested environments.
4.	Enable automatic channel optimization in router settings.
5.	Upgrade security to WPA3 (if available).
6.	Position router centrally and away from walls or metal objects.
## 9. Conclusion
This analysis demonstrates that while the local Wi-Fi network provides strong signal strength and stable configuration, it operates in a highly congested 2.4 GHz environment. Channel overlap and neighboring interference may negatively affect overall network performance.
By adjusting channel selection, reducing bandwidth width, and potentially migrating to the 5 GHz band, network reliability and efficiency can be significantly improved.
The collected measurements and screenshots provide a comprehensive overview of the network’s current state and form the basis for practical optimization strategies.

