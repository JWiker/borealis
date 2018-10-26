#!/bin/bash

# PROJECT BOREALIS BOOTER
# 12-JUNE-2018
# Adam Lozinsky

# Title Header.
echo ""
echo "Project Borealis Booter"
echo "v2.3-Alpha Season 1 Episode 3"
echo "-----------------------------------------------------------------------------------"

# These are the commands to in each window.
if [ "$2" = "release" ]; then
    start_brian="python -O brian/brian.py; bash"
    start_exphan="sleep 0.001s; python experiment_handler/experiment_handler.py "$1" ; bash;"
    start_radctrl="sleep 0.001s; python -O radar_control/radar_control.py; bash;"
    start_datawrite="sleep 0.001s; python -O data_write/data_write.py --file-type=hdf5 --enable-pre-bf-iq --enable-bfiq; bash;"
    start_n200driver="sleep 0.001s; source mode "$2"; n200_driver > n200_output.txt; bash"
    start_dsp="sleep 0.001s; source mode "$2"; signal_processing; bash;"
    start_tids="sleep 0.001s; python -O usrp_drivers/n200/set_affinity.py; bash;"
else
    start_brian="python brian/brian.py; bash"
    start_exphan="sleep 0.001s; python experiment_handler/experiment_handler.py "$1" ; bash"
    start_radctrl="sleep 0.001s; python -O radar_control/radar_control.py; bash"
    start_datawrite="sleep 0.001s; python data_write/data_write.py; bash"
    start_n200driver="sleep 0.001s; source mode "$2" ; gdb -ex start n200_driver; bash"
    start_dsp="sleep 0.001s; source mode "$2"; /usr/local/cuda/bin/cuda-gdb -ex start signal_processing; bash"
    start_tids="sleep 0.001s; python usrp_drivers/n200/set_affinity.py; bash"
fi

# Modify screen rc file
sed -i.bak "s#START_BRIAN#$start_brian#; \
            s#START_EXPHAN#$start_exphan#; \
            s#START_RADCTRL#$start_radctrl#; \
            s#START_DATAWRITE#$start_datawrite#; \
            s#START_N200DRIVER#$start_n200driver#; \
            s#START_DSP#$START_DSP#; \
            s#START_TIDS#$start_tids#;" borealisscreenrc

# Launch a detached screen with editted layout.
screen -S borealis -c borealisscreenrc
# Return the original config file
mv borealisscreenrc.bak borealisscreenrc