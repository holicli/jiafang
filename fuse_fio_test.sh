#!/bin/bash

TIME=`date +%Y%m%d_%H%M%S`

  for bs in 32736 16 4 
#for rw in randwrite randread
do  
  ts=1
#  for bs in 2016 16 4 
for rw in write read randread
  do
      sync
      echo 3 > /proc/sys/vm/drop_caches
      #CMDLINE="./fio/fio -ioengine=psync -direct=0 -rw=${rw} -bs=${bs}k -size=${ts}G -directory=/home/ -numjobs=1 -name=testfile-${bs}-${TIME}"
      CMDLINE="./fio/fio -ioengine=psync -direct=1 -rw=${rw} -bs=${bs}k -size=${ts}G -directory=/home/holicli/ssd -numjobs=1 -name=mytest-${bs}-${TIME}"
      echo "${CMDLINE}"
#      echo "${CMDLINE}" >> ./log/fio-${TIME}.log
      eval "${CMDLINE}" 
  done
done
