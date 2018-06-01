Name:           ros-kinetic-dynamixel-workbench
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS dynamixel_workbench package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/dynamixel_workbench
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-dynamixel-workbench-controllers
Requires:       ros-kinetic-dynamixel-workbench-operators
Requires:       ros-kinetic-dynamixel-workbench-single-manager
Requires:       ros-kinetic-dynamixel-workbench-single-manager-gui
Requires:       ros-kinetic-dynamixel-workbench-toolbox
BuildRequires:  ros-kinetic-catkin

%description
Dynamixel-Workbench is dynamixel solution for ROS. This metapackage allows you
to easily change the ID, baudrate and operating mode of the Dynamixel.
Furthermore, it supports various controllers based on operating mode and
Dynamixel SDK. These controllers are commanded by operators.

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
* Fri Jun 01 2018 Pyo <pyo@robotis.com> - 0.3.0-0
- Autogenerated by Bloom

* Tue Mar 20 2018 Pyo <pyo@robotis.com> - 0.2.4-0
- Autogenerated by Bloom

* Fri Mar 09 2018 Pyo <pyo@robotis.com> - 0.2.3-0
- Autogenerated by Bloom

* Wed Feb 28 2018 Pyo <pyo@robotis.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Feb 21 2018 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

