# Script generated with Bloom
pkgdesc="ROS - This stack provides utilities commonly needed for a variety of computer vision tasks."
url='http://wiki.ros.org/cob_perception_common'

pkgname='ros-kinetic-cob-perception-common'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-3d-mapping-msgs'
'ros-kinetic-cob-cam3d-throttle'
'ros-kinetic-cob-image-flip'
'ros-kinetic-cob-object-detection-msgs'
'ros-kinetic-cob-object-detection-visualizer'
'ros-kinetic-cob-perception-msgs'
'ros-kinetic-cob-vision-utils'
)

conflicts=()
replaces=()

_dir=cob_perception_common
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_perception_common $srcdir/cob_perception_common
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

