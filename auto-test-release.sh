#!/bin/bash
metaname=("meta-cgl" "meta-cloud-services" "meta-freescale" "meta-gplv2" "meta-measured" "meta-oe-sumo" "meta-qt5" "meta-security" "meta-selinux" "meta-virtualization" "meta-xilinx" "meta-skeleton")
metadir=("git://git.yoctoproject.org/meta-cgl" "git://git.yoctoproject.org/meta-cloud-services"  "https://git.yoctoproject.org/git/meta-freescale" "git://git.yoctoproject.org/meta-gplv2" "https://github.com/flihp/meta-measured.git" "git://git.openembedded.org/meta-openembedded" "git://github.com/meta-qt5/meta-qt5.git" "git://git.yoctoproject.org/meta-security" "git://git.yoctoproject.org/meta-selinux" "git://git.yoctoproject.org/meta-virtualization" "git://git.yoctoproject.org/meta-xilinx" "git://git.yoctoproject.org/poky")

usage () {
	echo ""
        echo "auto-test-release is used to automatically test release"
        echo ""
        echo "auto-test-release can help you build a bitbake environment"
        echo ""
        echo "it can help you automatically update the software in the warehouse"
        echo ""
        echo "   \$ ./auto-test-release PARA1 PARA2 PARA3 "
        echo "   after this,you can read log in PARA3"
	echo ""
        echo ""
        echo "======== para ========"
        echo "  PARA1         where do you want to put the meta repository"
        echo "  PARA2         where do you want to bitbake ubinux"
        echo "  PARA3         where do you want to put the log"

    exit
}


workdir=`pwd`
logdir=$workdir"/log"
time=$(date "+%Y%m%d")

diraccess(){
	if [ ! -n "$2" ];then
		echo Please input $1, thankyou  >> $logdir/$time.log
		exit 1
	fi
	if [ ! -d "$1" ];then	
		echo lease check if $point exists  >> $logdir/$time.log
		exit 1
	fi
	echo $2 is ok >> $logdir/$time.log 
}

logdiraccess(){
	if [ ! -d "$1" ];then
		cd $workdir
                echo logdir does not exist, using the default dir  >> $logdir/$time.log
	else
		logdir=$1
        fi
}

autogitpull(){
                cd $1
                #git checkout master
                git pull >> $logdir/$time.log 2>&1
}

autobitbake(){
        cd $1
	echo `pwd`
	echo $2
        source setup_ubinux.sh armv7be $2
        #bitbake json >> $logdir$time.log 2>&1
	#bitbake ubinux-all  2>&1 | tee $logdir$time.log
}

autogitclone(){
	cd $1
	git clone $2  2>&1 | tee $logdir/$time.log
}

autogit(){
	metaloop=0
	while [ $metaloop -lt ${#metaname[@]} ]
	do
		if [ ! -d "$1/${metaname[$metaloop]}" ];then
			echo ${metaname[$metaloop]} >> $logdir/$time.log
			autogitclone $1  ${metadir[$metaloop]}
		else
			echo ${metaname[$metaloop]} >> $logdir/$time.log
			autogitpull $1/${metaname[$metaloop]}
		fi
		let metaloop++
	done
}

logdiraccess $3
echo "----check dir start----" >> $logdir/$time.log

#if args is none, show usage
if [ $# -eq 0 ]; then
    usage
fi

case "$1" in
        -h|--help)
		usage
		shift
                ;;
        *)
                diraccess $1 "rootdir"
                ;;
esac

diraccess $2 "bitbakedir"

echo "----check dir end----" >> $logdir/$time.log

echo "----auto git start----" >> $logdir/$time.log
autogit $1
echo "-----auto git end-----" >> $logdir/$time.log

echo "-----bitbake start----" >> $logdir/$time.log
autobitbake $1 $2
echo "-----bitbake end------" >> $logdir/$time.log

