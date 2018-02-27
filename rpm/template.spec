Name:           ros-kinetic-dynamixel-workbench-toolbox
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS dynamixel_workbench_toolbox package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://wiki.ros.org/dynamixel_workbench
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamixel-sdk
Requires:       ros-kinetic-roscpp
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamixel-sdk
BuildRequires:  ros-kinetic-roscpp

%description
This package is composed of 'dynamixel_item', 'dynamixel_tool',
'dynamixel_driver' and 'dynamixel_workbench' class. The 'dynamixel_item' is
saved as control table item and information of Dynamixels. The 'dynamixel_tool'
class loads its by model number of Dynamixels. The 'dynamixel_driver' class
includes wraped function used in DYNAMIXEL SDK. The 'dynamixel_workbench' class
make simple to use Dynamixels

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
* Wed Feb 28 2018 Pyo <pyo@robotis.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Feb 21 2018 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

