from scipy import signal
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft,fftshift
import math
import random
import cmath

def plot_fft(samplesa, rate):
    fft_samps=fft(samplesa)
    T= 1.0 /float(rate)
    num_samps=len(samplesa)
    if num_samps%2==1:
        xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), num_samps)
    else:
        xf = np.arange(-1.0/(2.0*T),1.0/(2.0*T),1.0/(T*num_samps))
    fig, smpplt = plt.subplots(1,1)
    fft_to_plot=np.empty([num_samps],dtype=complex)
    fft_to_plot=fftshift(fft_samps)
    smpplt.plot(xf, 1.0/num_samps * np.abs(fft_to_plot))
#    plt.xlim([-2500000,-2000000])
    return fig

def get_samples(rate,wave_freq,numberofsamps):
    rate = float(rate)
    wave_freq = float(wave_freq)

    sampling_freq=2*math.pi*wave_freq/rate
    sampleslen=int(numberofsamps)
    samples=np.empty([sampleslen],dtype=complex)
    for i in range(0,sampleslen):
        amp=1
        rads=math.fmod(sampling_freq*i,2*math.pi)
        samples[i]=amp*math.cos(rads)+amp*math.sin(rads)*1j
    return samples

# Create a signal (pink noise)
# in frequency domain

def make_pulse_train(fs,wave_freq):
    pullen=300 # us
    mpinc=1500 # us
    pulse_train=[0]
    #freq=10200 # kHz
    wave_freq=wave_freq
    rate=fs #kHz
    sampleslen=int(mpinc*1e-6*(pulse_train[-1]+1)*rate*1000)
    print sampleslen
    samples=np.empty([sampleslen],dtype=complex)
    i=1
    for pulse_time in pulse_train:
        if pulse_train.index(pulse_time)!=0:    
            numzeros=(pulse_time-(pulse_train[pulse_train.index(pulse_time)-1]+1))*mpinc*1e-6*rate*1000
            for num in range(0,numzeros):
                samples[i]=0
                i=i+1
        pulse=get_samples(rate*1000,wave_freq*1000,pullen*1e-6*rate*1000)
        for samp in pulse:
            samples[i]=samp
            i=i+1
        for num in range(0,int((mpinc-pullen)*1e-6*rate*1000)):
            samples[i]=0
            i=i+1
    if i!=sampleslen-1:
        print("ERROR Sampleslen")    
        print(i,sampleslen)
    return sampleslen, samples


def get_noise(ncoeff, seq_length):
    seq_length = float(seq_length)
    phase=[random.uniform(0,2*math.pi) for n in range(-ncoeff,1)] #phase of negative spectrum, make symmetric for positive.
    for n in range(1,ncoeff+1):
        phase.append(-phase[-(2*n)])
    freq=[float(n)/(2*math.pi) for n in range(-ncoeff,ncoeff+1)]
    #print(type(math.exp(phase[1]*1j)))
    zip1=zip(freq[0:ncoeff],phase[0:ncoeff])
    zip2=zip(freq[ncoeff+1:],phase[ncoeff+1:])
    coeff=np.empty([len(freq)],dtype=complex)
    coeff=np.array([(1/fk)*cmath.exp(phi*1j) for fk,phi in zip1] + [0] + [(1/fk)*cmath.exp(phi*1j) for fk,phi in zip2], dtype=complex)
    print(len(freq))
    print(len(coeff))
    sequence=ifft(coeff)
    return sequence,np.abs(coeff),freq

# SET VALUES
# Low-pass filter design parameters
fs = 12e6           # Sample rate, Hz
cutoff = 100e3      # Desired cutoff frequency, Hz
trans_width = 50e3  # Width of transition from pass band to stop band, Hz
numtaps = 512       # Size of the FIR filter.
wave_freq = -1.8e6  # 1.8 MHz below centre freq (12.2 MHz if ctr = 14 MHz)
ctrfreq = 14000     # kHz

# GET SAMPLES AND decimate.
num_samples, pulse_samples=make_pulse_train(fs, wave_freq)
# Assume this is a received signal of ours.

# use the first filter to get down to approximately 250 kHz bandwidth.
# we are at baseband centered around 12 MHz (ctrfreq)
# shift filter the appropriate amount, 

lpass = signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs],
                    [1, 0], Hz=fs)

shift_wave = get_samples(fs,wave_freq,numtaps)
bpass = np.array([l*i for l,i in zip(lpass,shift_wave)])

output = signal.convolve(pulse_samples,bpass,mode='same') / sum(bpass)
response = plot_fft(output,fs)
#fig5 = plt.figure()
#plt.plot(response,

w,h = signal.freqz(bpass, whole=True)

#noise_seq,noise_fft,noise_freq=get_noise(20,100)
#fig5 = plt.figure()
#plt.plot(np.arange(len(noise_seq)),noise_seq)
#plt.plot(noise_freq,noise_fft)

fig4 = plt.figure()
plt.plot(np.arange(len(bpass)),bpass)
plt.plot(np.arange(len(lpass)),lpass)
fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')

fig2 = plot_fft(bpass,fs)
fig3 = plot_fft(lpass,fs)

plt.show()
