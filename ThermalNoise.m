clc;
clear;
close all;

% Parameters
n_samples = 10000;
B = 100;
R = 100;
T = 300;
k = 1.38e-23;

Fs = 1000;  % sampling frequency > 2B

time = (0:n_samples-1) / Fs;

%Generate thermal noise
Vrms = sqrt(4 * k * T * R * B);
thermal_noise = Vrms * randn(1, n_samples);

% Time Domain Plot
figure;
plot(time, thermal_noise);
xlabel('Time (s)');
ylabel('Thermal Noise Amplitude (V)');
title('Generated Thermal Noise');
grid on;

%PSD Analysis
[psd, freq] = pwelch(thermal_noise, [], [], [], Fs);

figure;
plot(freq, 10*log10(psd));
xlabel('Frequency (Hz)');
ylabel('PSD (dBV^2/Hz)');
title('Power Spectral Density of Thermal Noise');
grid on;

% Display theoretical values
disp(['Theoretical RMS Voltage = ', num2str(Vrms), ' V']);
disp(['Theoretical PSD = ', num2str(4*k*T*R), ' V^2/Hz']);
