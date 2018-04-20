# Script generated with Bloom
pkgdesc="ROS - The cob_object_detection_visualizer package"


pkgname='ros-kinetic-cob-object-detection-visualizer'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'opencv'
'pcl'
'ros-kinetic-catkin'
'ros-kinetic-cob-object-detection-msgs'
'ros-kinetic-cv-bridge'
'ros-kinetic-eigen-conversions'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-visualization-msgs'
)

depends=('boost'
'opencv'
'pcl'
'ros-kinetic-cob-object-detection-msgs'
'ros-kinetic-cv-bridge'
'ros-kinetic-eigen-conversions'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=cob_object_detection_visualizer
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_object_detection_visualizer $srcdir/cob_object_detection_visualizer
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

