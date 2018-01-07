Name:           ros-indigo-cob-3d-mapping-msgs
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS cob_3d_mapping_msgs package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/cob_3d_mapping_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-cob-object-detection-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-object-detection-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Message, service and action definitions for environment perception.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 07 2018 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.11-0
- Autogenerated by Bloom

* Thu Jul 20 2017 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

