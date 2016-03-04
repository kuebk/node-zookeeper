#!/bin/bash

ROOT=`pwd`
BUILD=$ROOT/../build/zookeeper
SOURCE=$ROOT/../deps/zookeeper

cd $SOURCE

if [ -e "$BUILD/lib/libzookeeper_st.la" ]; then
    echo "ZooKeeper has already been built"
    exit 0
fi

./configure \
--without-syncapi \
--enable-static \
--disable-shared \
--with-pic \
--libdir=$BUILD/lib \
--prefix=$BUILD && \
make -i && \
make -i install
if [ $? != 0 ] ; then
    echo "Unable to build zookeeper library"
    exit 1
fi
cd $ROOT
