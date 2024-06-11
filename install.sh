#!/bin/bash
# ---------------------
# created by @norcholly
# This .sh file is for installing the Python libraries required for expl0r4bimus.py to run on your machine. 
# Once you've run it once and completed the installations without errors, you can delete this .sh file.
# https://alirfandogan.com/
# github.com/norcholly
# ---------------------

current_time=$(date | awk '{print $4}')
function install() {

    echo -e "\033[91m"
    requests_exists=$(pip3 show requests | grep -o "Name: requests")
    if [ -z "$requests_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'Requests' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q requests
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'Requests' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'Requests' library is already in computer!\033[91m"

    fi

    sleep 1

    echo -e "\033[91m"
    ping3_exists=$(pip3 show ping3 | grep -o "Name: ping3")
    if [ -z "$ping3_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'Ping3' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q ping3
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'Ping3' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'Ping3' library is already in computer!\033[91m"

    fi

    sleep 1

    echo -e "\033[91m"
    nmap_exists=$(pip3 show python-nmap | grep -o "Name: python-nmap")
    if [ -z "$nmap_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'Python-Nmap' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q python-nmap
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'Python-Nmap' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'Python-Nmap' library is already in computer!\033[91m"

    fi

    sleep 1

    echo -e "\033[91m"
    colorama_exists=$(pip3 show colorama | grep -o "Name: colorama")
    if [ -z "$colorama_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'Colorama' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q colorama
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'Colorama' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'Colorama' library is already in computer!\033[91m"

    fi

    sleep 1

    echo -e "\033[91m"
    pyfiglet_exists=$(pip3 show pyfiglet | grep -o "Name: pyfiglet")
    if [ -z "$pyfiglet_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'Pyfiglet' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q pyfiglet
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'Pyfiglet' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'Pyfiglet' library is already in computer!\033[91m"

    fi

    sleep 1

    echo -e "\033[91m"
    readline_exists=$(pip3 show readline | grep -o "Name: readline")
    if [ -z "$readline_exists" ]; then
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95mIt seems that the 'readline' library is not installed on your machine. The library is being downloaded...\033[91m"
        sudo pip3 install -q readline
        echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92m'readline' library successfully installed!\033[91m"
    else
        echo -e "\033[1m\033[92m[\033[95m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[95mexpl0r4bimus\033[1m\033[92m] \033[95m'readline' library is already in computer!\033[91m"

    fi

    sleep 1

}

echo -e "\033[1m\033[92m[\033[93m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[93mexpl0r4bimus\033[1m\033[92m] \033[93mThe necessary libraries for expl0r4bimus to function without errors are being downloaded... This process only needs to be done once!\033[0m"
sleep 1
install
echo -e ""
echo -e "\033[1m\033[92m[\033[92m$current_time\033[1m\033[92m] \033[1m\033[92m[\033[92mexpl0r4bimus\033[1m\033[92m] \033[92mOperation completed! The tool is now ready to run smoothly. \033[3m\033[5m@norcholly\033[0m"
sleep 5
clear