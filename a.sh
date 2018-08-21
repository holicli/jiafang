#!/bin/bash
sites=("meta-cgli git://git.yoctoproject.org/meta-cgl" \
	"meta-cloud-services git://git.yoctoproject.org/meta-cloud-services" \
	"meta-freescale https://git.yoctoproject.org/git/meta-freescale" \
	"meta-gplv2 git://git.yoctoproject.org/meta-gplv2" \
	"meta-measured https://github.com/flihp/meta-measured.git" \
	"meta-oe-sumo git://git.openembedded.org/meta-openembedded" \
	"meta-qt5 git://github.com/meta-qt5/meta-qt5.git" \
	"meta-security git://git.yoctoproject.org/meta-security" \
	"meta-selinux git://git.yoctoproject.org/meta-selinux" \
	"meta-virtualization git://git.yoctoproject.org/meta-virtualization" \
	"meta-xilinx git://git.yoctoproject.org/meta-xilinx" \
	"meta-skeleton git://git.yoctoproject.org/poky")

n_sites=${#sites[*]}
metaname=""
metadir=""
for ((i=0;i<$n_sites;i++));
do
  inner_sites=(${sites[$i]})
  n_inner_sites=${#inner_sites[*]}
  for ((j=0;j<$n_inner_sites;j++));
  do
  if [ "0" -eq "$j" ];then
	  metaname[i]=${inner_sites[$j]}
  else
	  metadir[i]=${inner_sites[$j]}
  fi
  done
done
echo "数组的元素为: ${metaname[*]}"
echo "数组的元素为: ${metadir[*]}"
