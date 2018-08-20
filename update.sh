#!/bin/bash
rootdir="/yocto/work001/fnst/ubinux/poky/"
metadir=("meta-cgl" "meta-cloud-services" "meta-freescale" "meta-gplv2" "meta-measured" "meta-oe-sumo" "meta-qt5" "meta-security" "meta-selinux" "meta-virtualization" "meta-xilinx" "meta-skeleton")
logdir="/yocto/work001/fnst/ubinux/log/"
time=$(date "+%Y%m%d")

directory(){
	if [ ! -d "$1" ];then
		echo Please check if $2 exists
	else
		$2=$1
	fi
}

autogitpull(){
        for var in ${metadir[@]}; do
                cd $rootdir$var
                #git checkout master
                echo $var: >> $logdir$time.log
                git pull >> $logdir$time.log 2>&1
        done
}

autoBitbake(){
        cd $rootdir
        source setup_ubinux.sh armv7be ../build-armv7be
        #bitbake json >> $logdir$time.log 2>&1
        bitbake ubinux-all  2>&1 | tee $logdir$time.log
}

case "$1" in
        -h|--help)
                echo please input like ./update.sh metadir bitbakedir logdir
                ;;
        *)
                directory $1 "rootdir"
                ;;
esac

directory $2 "bitbakedir"

directory $3 "logdir"


echo "----git pull start----" >> $logdir$time.log
#autogitpull
echo "-----git pull end-----" >> $logdir$time.log

echo "-----bitbake start----" >> $logdir$time.log
#autoBitbake
echo "-----bitbake end------" >> $logdir$time.log

