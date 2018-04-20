# Script generated with Bloom
pkgdesc="ROS - Flips the image of Care-O-bots kinect in dependence of the viewing direction of the cameras to receive an upright image all the time."
url='http://wiki.ros.org/cob_image_flip'

pkgname='ros-kinetic-cob-image-flip'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'opencv'
'ros-kinetic-catkin'
'ros-kinetic-cob-perception-msgs'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-ros'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf'
)

depends=('boost'
'opencv'
'ros-kinetic-cob-perception-msgs'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-ros'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=cob_image_flip
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_image_flip $srcdir/cob_image_flip
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

