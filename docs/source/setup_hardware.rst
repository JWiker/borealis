========
Hardware
========

------------------------------
System Overview and Rack Setup
------------------------------

Below is a recommended configuration in comparison to a common SuperDARN system, Note that the N200s are in custom made shelves, but shelves can also be purchased from National Instruments:

.. figure:: img/USRP-rack-rev5.png
   :scale: 75 %
   :alt: Block diagram of RX DSP software
   :align: center

Here is an actual rack configuration as installed by SuperDARN Canada at the Saskatoon (SAS) SuperDARN site. Note that space has been allowed between the rackmount items to allow for cable routing. There is a lot of cabling involved at the front of the devices.

.. figure:: img/sas-borealis-rack1.jpg
   :scale: 25 %
   :alt: Rack photo
   :align: center

The items installed in the rack at the Saskatoon site are listed below in order from top to bottom in the rack:

- Netgear XS708E 10Gb switch
- USRP rackmount shelf (in-house design) with 4 x N200s
- Ettus Octoclock
- USRP rackmount shelf (in-house design) with 4 x N200s
- Netgear XS708E 10Gb switch
- Rackmount shelf with 4 x low-noise amplifiers for the interferometer array channels, and a terminal strip for power (supplied by 15V Acopian)
- Ettus Octoclock-G (with GPSDO)
- USRP rackmount shelf (in-house design) with 4 x N200s
- Ettus Octoclock
- USRP rackmount shelf (in-house design) with 4 x N200s
- Netgear XS708E 10Gb switch
- Synology Network Attached Storage device
- APC Smart UPS
- 15V Acopian power supply

(3 x APC PDUs (AP7900B) are mounted at the back of the rack)

The Borealis computer is not in a rackmount case, instead it is placed to the right of the rack. 

-----
USRPs
-----

This guide assumes set up of a brand new, unopened Ettus N200.

Initial Test of the Unit
------------------------

*Install Daughterboards*

#. Open the unit and install the LFTX and LFRX daughtercards using hardware provided. The main USRP PCB is clearly marked with where to connect TX and RX daughterboards, and there is only one way they can fit while still allowing all the screw holes to line-up. The RX daughterboard is located directly above the fan power connection at the back of the motherboard.
#. Connect the output of TXA using an SMA cable to the custom-added SMA connection point on the front of the USRP using one of the SMA Male to female bulkhead SMA cables. Connect the output of RXA to RF1 and RXB to RF2 on the front of the USRP using two more SMA Male to female bulkhead cables.
#. Verify that the jumper J510 on the N200 motherboard is jumping the two 0.1" header pins furthest from the board edge. The jumper is located behind the CLK_REF (REF IN) SMA connector on the front of the N200. This ensures that the reference clock input is coming from the front-panel SMA connector, and not the secondary SMA connector located on the motherboard labeled 'J507 CLK_REF 2'.

*Connect to the USRP*

#. USRPs have a default IP address of `192.168.10.2`. Assign a computer network interface an address that can communicate in this subnet. Connect the USRP to the computer's network interface either directly or through one of the switches from the system specifications. Connect the USRP power supply.
#. Verify the board powers on and is discoverable. The USRP should be discoverable by pinging 192.168.10.2. Ettus' USRP UHD library supplies a tool called `uhd_usrp_probe` which should also be able to detect the device. See software setup for notes on installing UHD. The USRP may require a firmware upgrade.
#. Connect an SMA T connection (F-M-F) to the TX output from the front of the N200, connect another SMA T (F-M-F) to the first T. Connect one end of the second SMA T to RX1, and the other end to RX2 with phase matched SMA M-M cables. Connect the free SMA output of the first SMA T to the scope. Connect the Octoclock PPS and 10MHz reference signals to the USRP. Make sure that the jumper on J510 is in the rightmost position connecting the front panel 10MHz as the system reference.

*Test the USRP*

#. Use the UHD utilities `rx_samples_to_file`, `tx_bursts` and `txrx_loopback_to_file` to verify the USRP works. Use the scope to see the transmit signal. The RX samples will be a binary file that can be quickly read in a plotted with Numpy/Matplotlib. While testing, watch the front panel LEDs to see that they work as expected.

*Disassembly for Enclosure Modifications*

#. If the USRP is working correctly, the inner motherboard, fan, daughtercards and RF cables can all be removed from the unit. Carefully peel the product sticker and store with the motherboard, this contains the MAC address, SN and PN of the unit. All removed components and the sticker can be stored in the anti-static bags that were supplied with the unit. The enclosure is ready for machining the additional holes. Ensure that you note which way the fan was installed for reinstallation later.

Custom Enclosure Modifications
------------------------------

*The custom machining involves the following machining steps*

#. Five extra SMA holes that are 'D' shaped to fit most standard SMA bulkhead connectors. Four of these holes are on the back of the N200, and one is on the front, in line with the two existing RF1 and RF2 SMA bulkhead holes.
#. A DSUB shaped hole for a DE9 connector at the rear of the unit for connection to existing SuperDARN transmitters.
#. Four holes for standard 5mm LED clips (6.35 +/-0.05mm diameter) with 9.5mm centers to appropriately space them.


Installing the Custom-Made TXIO Board
-------------------------------------

#. Once the enclosures are machined, the electronics and components can all be reinstalled. Place the product sticker back in place on the rear of the unit. There are slight indentations in the case to indicate where the product sticker goes. Connect RXA to port RF1, connect RXB to port RF2, and connect TXA to the additional front panel hole that was added.
#. Install the LEDs (TODO: Add description of how to install LED clip here) into their corresponding holes. The order of the LED install patterns from left to right are the TX only indicator (RED), the IDLE indicator (YELLOW), the RX only indicator (GREEN) and the TR indicator (BLUE). Optionally, add labels to the LEDs on the front panel.
#. Install the fan, making sure to re-install it the same way it was originally installed.

    .. image:: img/txio_fan_direction.jpg
       :height: 500px
       :width: 500px
       :alt: Arrows indicate fan rotation and air flow direction
       :align: center


*Pre-Assemble the TXIO board before installation into the N200*

#. Begin by connecting eight 0.1" female-female jumper cables to pins 1-4 and 6-9 of the D-sub connector. The other ends of these wires connects to header J2 on the TXIO board

	+--------+------+------+------+
	| Colour | Sig  | DSUB | J2   |
      	+========+======+======+======+
	| Brown  | AGC- | 1    | 7    |
	+--------+------+------+------+
	| Orange | TR-  | 2    | 8    |
	+--------+------+------+------+
	| Blue   | TM-  | 3    | 2    |
	+--------+------+------+------+
	| Grey   | LP-  | 4    | 1    |
	+--------+------+------+------+
	| [NC]   | [NC] | 5    | [NC] |
	+--------+------+------+------+
	| Red    | AGC+ | 6    | 9    |
	+--------+------+------+------+
	| Yellow | TR+  | 7    | 10   |
	+--------+------+------+------+
	| Green  | TM+  | 8    | 4    |
	+--------+------+------+------+
	| Purple | LP+  | 9    | 3    |
	+--------+------+------+------+

    .. image:: img/txio_dsub_fanpwr.jpg
       :scale: 80%
       :alt: TXIO dsub wire connections
       :align: center

    .. image:: img/txio_lfrx_signals.jpg
       :scale: 80%
       :alt: TXIO lrfx signal connections
       :align: center

#. Connect the four U.Fl to SMA female bulkhead cables to J4, J5, J6 and J7 of the TXIO board. Orientation of the cables doesn't matter, as they will fit in the N200 case if rotated properly.

    .. image:: img/txio_pcb_connections.jpg
       :scale: 80%
       :alt: TXIO PCB view
       :align: center

#. Connect 4 pairs of 0.1" female to female jumper wires to header J3 on the TXIO board. THe other ends will connect to the LEDs already installed in the N200 case. There is no need to connect anything to the 4 rightmost pins on J3, these are expansion headers and two are connected (label 'OUT') to the leftover open collector pins on the LED driver chip U5 (SN7406D), the other two (labels '_0' and '_1') are connected to the 5V rail via pullup resistors R5 and R6. **NOTE** If you use your own voltage supply with the open-collector outputs, be aware that the maximum voltage is 30V, and the maximum current sink is 40mA. See the SN7406D datasheet for more details.

        +--------------+-------------+----------------+
	| J3 Pin label | Wire Colour | LED Connection |
	+==============+=============+================+
	| TXo          | Brown       | RED-           |
	+--------------+-------------+----------------+
	| RED          | Red         | RED+           |
	+--------------+-------------+----------------+
	| IDLE         | Orange      | Yellow-        |
	+--------------+-------------+----------------+
	| YLW          | Yellow      | Yellow+        |
	+--------------+-------------+----------------+
	| RX           | Blue        | Green-         |
	+--------------+-------------+----------------+
	| GRN          | Green       | Green+         |
	+--------------+-------------+----------------+
	| TX           | Grey        | Blue-          |
	+--------------+-------------+----------------+
	| BLU          | Purple      | Blue+          |
	+--------------+-------------+----------------+

    **NOTE** '-' means cathode, '+' means anode

#. Connect 10 0.1" female to female jumper wires to J1, the other ends will connect to the LFRX daughterboard pin headers.

	+---------+-----------+-------------+-------------+-----------+
	| J1 Pin  | Pin label | Wire colour | LFRX header | LFRX Pin  |
	+=========+===========+=============+=============+===========+
	| 1       | OUT_0     | [NC]        | [NC]        | [NC]      |
	+---------+-----------+-------------+-------------+-----------+
	| 2       | OUT_1     | [NC]        | [NC]        | [NC]      |
	+---------+-----------+-------------+-------------+-----------+
	| 3       | GND       | Brown       | J16         | 'DGND'    |
	+---------+-----------+-------------+-------------+-----------+
	| 4       | +6V       | Red         | J16         | '6V'      |
	+---------+-----------+-------------+-------------+-----------+
	| 5       | RXo       | Orange      | J15         | io_rx[1]  |
	+---------+-----------+-------------+-------------+-----------+
	| 6       | Txo       | Yellow      | J15         | io_rx[3]  |
	+---------+-----------+-------------+-------------+-----------+
	| 7       | TR        | Green       | J15         | io_rx[5]  |
	+---------+-----------+-------------+-------------+-----------+
	| 8       | IDLE      | Blue        | J15         | io_rx[7]  |
	+---------+-----------+-------------+-------------+-----------+
	| 9       | LP        | Purple      | J15         | io_rx[9]  |
	+---------+-----------+-------------+-------------+-----------+
	| 10      | AGC       | Grey        | J15         | io_rx[11] |
	+---------+-----------+-------------+-------------+-----------+
	| 11      | TM        | White       | J15         | io_rx[13] |
	+---------+-----------+-------------+-------------+-----------+
	| 12      | GND       | Black       | J16         | 'DGND'    |
	+---------+-----------+-------------+-------------+-----------+


    .. image:: img/txio_lfrx_signals.jpg
       :scale: 80%
       :alt: TXIO LFRX signal connections
       :align: center

    .. image:: img/txio_lfrx_pwr.jpg
       :scale: 80%
       :alt: TXIO LRFX pwr connections
       :align: center

#. Install the TXIO board by screwing it into place on the USRP housing with the two provided holes. The TXIO board uses the same size and style of screw that the N200 motherboard and daughtercards do.

    - Install the DSUB connector with the provided standoff screws. **NOTE** some models of DSUB will have split lock washers, but we've found that the thickness of the N200 case is too thick to use them. The DSUB standoff screws are notoriously easy to snap as well, so be careful.
    - Install the 4x SMA female bulkhead cables at the back of the N200, when facing the rear of the N200 case the order from left to right is: J4, J5, J6, J7 (the same order as on the PCB, so no wires should cross each-other).
    - Finally, connect the LFRX jumper wires from J1 and LED wires from J3 to complete the installation.

    .. image:: img/txio_rear.jpg
       :scale: 80%
       :alt: TXIO rear view
       :align: center

#. Follow the testing procedure below to run a simple test of the TXIO outputs.

    **TXIO OUTPUT TESTS**

    - Connect a needle probe to channel one of your oscilloscope and set it to trigger on the rising edge of channel one.

    - Run test_txio_gpio.py located in borealis/testing/n200_gpio_test. Usage is as follows:

        `python3 test_txio_gpio.py <N200_ip_address>`

    - When prompted to enter the pins corresponding to the TXIO signals, press enter to accept the default pin settings. This will begin the tests. Pressing CTRL+C and entering "y" will tell the program to run the next test.

    - Insert the needle probe into the SMA output corresponding to RXO. The scope signal should be the inverse of the pattern flashed by the GREEN front LED. Then, proceed to the next test (CTRL+C, then enter "y").

    - Insert the needle probe into the SMA output corresponding to TXO. The scope signal should be the inverse of the pattern flashed by the RED and BLUE front LEDs. Then, proceed to the next test (CTRL+C, then enter "y").

    - Insert the needle probe into the SMA output corresponding to TR. The scope signal should be the inverse of the pattern flashed by the BLUE and GREEN front LEDs. Then, proceed to the next test (CTRL+C, then enter "y").

        - Insert the needle probe into the hole corresponding to pin 7 of the D-Sub connector (TR+). The scope signal should follow the pattern flashed by the BLUE and GREEN front LEDs.

        - Insert the needle probe into the hole corresponding to pin 2 of the D-Sub connector (TR-). The scope signal should be the inverse of the pattern flashed by the BLUE and GREEN front LEDs.

    - Insert the needle probe into SMA output corresponding to IDLE. The scope signal should be the inverse of the pattern flashed by the YELLOW front LED. Then, proceed to the next test (CTRL+C, then enter "y").

    - Insert the needle probe into the hole corresponding to pin 8 of the D-Sub. The scope signal should follow the sequence of numbers being printed to your terminal (high when the number is non-zero, low when the number is zero).

        - Insert the needle probe into the hole corresponding to pin 3 of the D-Sub. The scope signal should be the inverse of the sequence of numbers being printed to your terminal. Then, proceed to the next test (CTRL+C, then enter "y").

    - To properly perform the loopback tests of the differential signals, connect the D-Sub pins to each other in the following configuration:

        - Pin 6 to pin 7
        - Pin 1 to pin 2
        - Pin 8 to pin 9
        - Pin 3 to pin 4

    - Once connected ensure that during the TR, AGC loopback test, the hex digit is non zero when the terminal indicates the output pin is low, and vice versa. Then, proceed to the next test (CTRL+C, then enter "y").

    - Ensure that during the TM, LP loopback test, the hex digit is non zero when the terminal indicates the output pin is low, and vice versa. Press CTRL+C, then enter "y" to end the tests.

    - This concludes the tests! If any of these signal output tests failed, additional troubleshooting is needed. To check the entire logic path of each signal, follow the testing procedures found in the TXIO notes document.

#. Install enclosure cover lid back in place, ensuring that no wires are pinched.

Configuring the Unit for Borealis
---------------------------------

1. Use UHD utility usrp_burn_mb_eeprom to assign a unique IP address for the unit. Label the unit with the device IP address.
2. The device should be configured and ready for use.

--------
Pre-amps
--------

For easy debugging, pre-amps are recommended to be installed inside existing SuperDARN transmitters where possible for SuperDARN main array channels. SuperDARN transmitters typically have a 15V supply and the low-noise amplifiers selected for pre-amplification (Mini-Circuits ZFL-500LN) operate at 15V, with max 60mA draw. The cable from the LPTR (low power transmit/receive) switch to the bulkhead on the transmitter can be replaced with a couple of cables to and from a filter and pre-amp. 

Note that existing channel filters (typically custom 8-20MHz filters) should be placed ahead of the pre-amps in line to avoid amplifying noise. 

It is also recommended to install all channels the same for all main array channels to avoid varying electrical path lengths in the array which will affect beamformed data.

Interferometer channels will need to be routed to a separate plate and supplied with 15V by a separate supply capable of supplying the required amperage for a minimum of 4 pre-amps.

-----------------------
Computer and Networking
-----------------------

To be able to run Borealis at high data rates, a powerful CPU with many cores and a high number of PCI lanes is needed. The team recommends an Intel i9 10 core CPU or better. Likewise a good NVIDIA GPU is needed for fast data processing. The team recommends a GeForce 1080TI/2080 or better. Just make sure the drivers are up to date on Linux for the model. A 10Gb(or multiple 1Gb interfaces) or better network interface is also required.

Not all networking equipment works well together or with USRP equipment. Some prototyping with different models may be required.

Once these components are selected, the supporting components such as motherboard, cooling and hard drives can all be selected. Assemble the computer following the instructions that come with the motherboard.
