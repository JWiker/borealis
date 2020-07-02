*****************
Config Parameters
*****************
+-----------------------------------------+-------------------------+--------------------------------------+
|Config field                             | Example entry           | Description                          |
+=========================================+=========================+======================================+
| site_id                                 | sas                     | 3-letter standard ID of the radar    |
+-----------------------------------------+-------------------------+--------------------------------------+
| gps_octoclock_addr                      | addr=192.168.10.131     | IP address of the GPS Octoclock      |
+-----------------------------------------+-------------------------+--------------------------------------+
| devices                                 | recv_frame_size=4000,   | UHD USRP device arguments.           |
|                                         | addr0=192.168.10.100,   |                                      |
|                                         | addr1=192.168.10.101,   |                                      |
|                                         | addr2=192.168.10.102,   |                                      |
|                                         | addr3=192.168.10.103,   |                                      |
|                                         | addr4=192.168.10.104,   |                                      |
|                                         | addr5=192.168.10.105,   |                                      |
|                                         | addr6=192.168.10.106,   |                                      |
|                                         | addr7=192.168.10.107,   |                                      |
|                                         | addr8=192.168.10.108,   |                                      |
|                                         | addr9=192.168.10.109,   |                                      |
|                                         | addr10=192.168.10.110,  |                                      |
|                                         | addr11=192.168.10.111,  |                                      |
|                                         | addr12=192.168.10.112,  |                                      |
|                                         | addr13=192.168.10.113,  |                                      |
|                                         | addr14=192.168.10.114,  |                                      |
|                                         | addr15=192.168.10.115   |                                      |
+-----------------------------------------+-------------------------+--------------------------------------+
| main_antenna_count                      | 16                      | Number of main array antennas (TX/RX)|
+-----------------------------------------+-------------------------+--------------------------------------+
| interferometer_antenna_count            | 4                       | Number of interferometer antennas    |
+-----------------------------------------+-------------------------+--------------------------------------+
| main_antenna_usrp_rx_channels           | 0,2,4,6,8,10,12,14,16,  | UHD channel designation for RX main  |
|                                         | 18,20,22,24,26,28,30    | antennas                             |
+-----------------------------------------+-------------------------+--------------------------------------+
| interferometer_antenna_usrp_rx_channels | 1,3,5,7                 | UHD channel designation for RX intf  |
|                                         |                         | antennas.                            |
+-----------------------------------------+-------------------------+--------------------------------------+
| main_antenna_usrp_tx_channels           | 0,1,2,3,4,5,6,7,8,9,    | UHD channel designation for TX main  |
|                                         | 10,11,12,13,14,15       | antennas.                            |
+-----------------------------------------+-------------------------+--------------------------------------+
| main_antenna_spacing                    | 15.24                   | Distance between antennas (m).       |
+-----------------------------------------+-------------------------+--------------------------------------+
| interferometer_antenna_spacing          | 15.24                   | Distance between antennas (m).       |
+-----------------------------------------+-------------------------+--------------------------------------+
| min_freq                                | 8.00E+06                | Minimum frequency we can run (Hz).   |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_freq                                | 20.00E+06               | Maximum frequency we can run (Hz).   |
+-----------------------------------------+-------------------------+--------------------------------------+
| minimum_pulse_length                    | 100                     | Minimum pulse length (us) dependent  |
|                                         |                         | upon AGC feedback sample and hold.   |
+-----------------------------------------+-------------------------+--------------------------------------+
| minimum_mpinc_length                    | 1                       | Minimum length of multi-pulse        |
|                                         |                         | increment (us).                      |
+-----------------------------------------+-------------------------+--------------------------------------+
| minimum_pulse_separation                | 125                     | The minimum separation (us) before   |
|                                         |                         | experiment treats it as a single     |
|                                         |                         | pulse (transmitting zeroes and not   |
|                                         |                         | receiving between the pulses. 125 us |
|                                         |                         | is approx two TX/RX times.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| tx_subdev                               | A:A                     | UHD daughterboard string which       |
|                                         |                         | defines how to configure ports. Refer|
|                                         |                         | to UHD subdev docs.                  |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_tx_sample_rate                      | 5.00E+06                | Maximum wideband TX rate each device |
|                                         |                         | can run in the system.               |
+-----------------------------------------+-------------------------+--------------------------------------+
| main_rx_subdev                          | A:A A:B                 | UHD daughterboard string which       |
|                                         |                         | defines how to configure ports. Refer|
|                                         |                         | to UHD subdev docs.                  |
+-----------------------------------------+-------------------------+--------------------------------------+
| interferometer_rx_subdev                | A:A A:B                 | UHD daughterboard string which       |
|                                         |                         | defines how to configure ports. Refer|
|                                         |                         | to UHD subdev docs.                  |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_rx_sample_rate                      | 5.00E+06                | Maximum wideband RX rate each        |
|                                         |                         | device can run in the system.        |
+-----------------------------------------+-------------------------+--------------------------------------+
| pps                                     | external                | The PPS source for the system        |
|                                         |                         | (internal, external, none).          |
+-----------------------------------------+-------------------------+--------------------------------------+
| ref                                     | external                | The 10 MHz reference source          |
|                                         |                         | (internal, external).                |
+-----------------------------------------+-------------------------+--------------------------------------+
| overthewire                             | sc16                    | Data type for samples the USRP       |
|                                         |                         | operates with. Refer to UHD docs for |
|                                         |                         | data types.                          |
+-----------------------------------------+-------------------------+--------------------------------------+
| cpu                                     | fc32                    | Data type of samples that UHD uses   |
|                                         |                         | on host CPU. Refer to UHD docs for   |
|                                         |                         | data types.                          |
+-----------------------------------------+-------------------------+--------------------------------------+
| gpio_bank                               | RXA                     | The daughterboard pin bank to use for|
|                                         |                         | TR and I/O signals.                  |
+-----------------------------------------+-------------------------+--------------------------------------+
| atr_rx                                  | 0x0006                  | The pin mask for the RX only mode.   |
+-----------------------------------------+-------------------------+--------------------------------------+
| atr_tx                                  | 0x0018                  | The pin mask for the TX only mode.   |
+-----------------------------------------+-------------------------+--------------------------------------+
| atr_xx                                  | 0x0060                  | The pin mask for the full duplex     |
|                                         |                         | mode (TR).                           |
+-----------------------------------------+-------------------------+--------------------------------------+
| atr_0x                                  | 0x0180                  | The pin mask for the idle mode.      |
+-----------------------------------------+-------------------------+--------------------------------------+
| tst_md                                  | 0x0600                  | The pin mask for test mode.          |
+-----------------------------------------+-------------------------+--------------------------------------+
| lo_pwr                                  | 0x1800                  | The pin mask for the low power signal|
+-----------------------------------------+-------------------------+--------------------------------------+
| agc_st                                  | 0x6000                  | The pin mask for the AGC signal.     |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_usrp_dac_amplitude                  | 0.99                    | The amplitude of highest allowed USRP|
|                                         |                         | TX sample (V).                       |
+-----------------------------------------+-------------------------+--------------------------------------+
| pulse_ramp_time                         | 1.00E-05                | The linear ramp time for the         |
|                                         |                         | pulse (s)                            |
+-----------------------------------------+-------------------------+--------------------------------------+
| tr_window_time                          | 6.00E-05                | How much windowing on either side of |
|                                         |                         | pulse is needed for TR signal (s).   |
+-----------------------------------------+-------------------------+--------------------------------------+
| agc_signal_read_delay                   | 0                       | Hardware dependent delay time for    |
|                                         |                         | reading of AGC and low power signals |
+-----------------------------------------+-------------------------+--------------------------------------+
| usrp_master_clock_rate                  | 1.00E+08                | Clock rate of the USRP master        |
|                                         |                         | clock (Sps).                         |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_output_sample_rate                  | 1.00E+05                | Maximum rate allowed after           |
|                                         |                         | downsampling (Sps)                   |
+-----------------------------------------+-------------------------+--------------------------------------+
| max_number_of_filter_taps_per_stage     | 2048                    | The maximum total number of filter   |
|                                         |                         | taps for all frequencies combined.   |
|                                         |                         | This is a GPU limitation.            |
+-----------------------------------------+-------------------------+--------------------------------------+
| router_address                          | tcp://127.0.0.1:6969    | The protocol/IP/port used for the ZMQ|
|                                         |                         | router in Brian.                     |
+-----------------------------------------+-------------------------+--------------------------------------+
| radctrl_to_exphan_identity              | RADCTRL_EXPHAN_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| radctrl_to_dsp_identity                 | RADCTRL_DSP_IDEN        | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| radctrl_to_driver_identity              | RADCTRL_DRIVER_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| radctrl_to_brian_identity               | RADCTRL_BRIAN_IDEN      | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| radctrl_to_dw_identity                  | RADCTRL_DW_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| driver_to_radctrl_identity              | DRIVER_RADCTRL_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| driver_to_dsp_identity                  | DRIVER_DSP_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| driver_to_brian_identity                | DRIVER_BRIAN_IDEN       | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| exphan_to_radctrl_identity              | EXPHAN_RADCTRL_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| exphan_to_dsp_identity                  | EXPHAN_DSP_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dsp_to_radctrl_identity                 | DSP_RADCTRL_IDEN        | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dsp_to_driver_identity                  | DSP_DRIVER_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dsp_to_exphan_identity                  | DSP_EXPHAN_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dsp_to_dw_identity                      | DSP_DW_IDEN             | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dspbegin_to_brian_identity              | DSPBEGIN_BRIAN_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dspend_to_brian_identity                | DSPEND_BRIAN_IDEN       | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dw_to_dsp_identity                      | DW_DSP_IDEN             | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| dw_to_radctrl_identity                  | DW_RADCTRL_IDEN         | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| brian_to_radctrl_identity               | BRIAN_RADCTRL_IDEN      | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| brian_to_driver_identity                | BRIAN_DRIVER_IDEN       | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| brian_to_dspbegin_identity              | BRIAN_DSPBEGIN_IDEN     | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| brian_to_dspend_identity                | BRIAN_DSPEND_IDEN       | ZMQ named socket identity.           |
+-----------------------------------------+-------------------------+--------------------------------------+
| ringbuffer_name                         | data_ringbuffer         | Shared memory name for ringbuffer.   |
+-----------------------------------------+-------------------------+--------------------------------------+
| ringbuffer_size_bytes                   | 200.00E+06              | Size in bytes to allocate for each   |
|                                         |                         | ringbuffer.                          |
+-----------------------------------------+-------------------------+--------------------------------------+
| data_directory                          | /data/borealis_data     | Location of output data files.       |
+-----------------------------------------+-------------------------+--------------------------------------+