Name:           ros-kinetic-cob-cam3d-throttle
Version:        0.6.9
Release:        0%{?dist}
Summary:        ROS cob_cam3d_throttle package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_cam3d_throttle
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
cob_cam3d_throttle: only for Trottel

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jul 18 2017 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

