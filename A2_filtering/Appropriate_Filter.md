Input Signal=A1⋅sin⁡(2π⋅100⋅t)+A2⋅sin⁡(2π⋅200⋅t)+A3⋅sin⁡(2π⋅300⋅t)+A4⋅sin⁡(2π⋅400⋅t)
| Frequency Component(s)         | Filter Type            | Cutoff Frequency / Frequencies                  |
| ------------------------------ | ---------------------- | ----------------------------------------------- |
| **100 Hz**                     | Low Pass Filter (LPF)  | f_c ~ 150Hz                                     |
| **400 Hz**                     | High Pass Filter (HPF) | f_c ~ 350Hz                                     |
| **100 Hz and 200 Hz**          | Low Pass Filter (LPF)  | f_c ~ 250Hz                                     |
| **200 Hz**                     | Band Pass Filter (BPF) | f_c  150Hz and 250Hz                            |
| **300 Hz**                     | Band Pass Filter (BPF) | f_c  250Hz and 350Hz             |
| **300 Hz and 400 Hz**          | High Pass Filter (HPF) | f_c ~ 250Hz                      |
| **200 Hz and 300 Hz**          | Band Pass Filter (BPF) | f_c  150Hz and 350Hz             |
| **200 Hz, 300 Hz, and 400 Hz** | High Pass Filter (HPF) |  f_c ~ 150Hz                     |
| **100 Hz and 400 Hz**          | Band Stop Filter (BSF) | Stopband: f_c  150Hz and 350Hz   |
