Name:           ros-hydro-cob-image-flip
Version:        0.5.10
Release:        0%{?dist}
Summary:        ROS cob_image_flip package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/cob_image_flip
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-cob-vision-utils
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-opencv2
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
BuildRequires:  boost-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cob-vision-utils
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-opencv2
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf

%description
Flips the image of Care-O-bots kinect in dependence of the viewving direction of
the cameras to receive an upright image all the time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Aug 29 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.10-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.4-2
- Autogenerated by Bloom

* Thu Aug 28 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.6-2
- Autogenerated by Bloom

* Thu Aug 28 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.6-1
- Autogenerated by Bloom

* Thu Aug 28 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.6-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.4-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.5.4-0
- Autogenerated by Bloom

