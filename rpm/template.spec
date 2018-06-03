Name:           ros-melodic-dynamixel-workbench-toolbox
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS dynamixel_workbench_toolbox package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/dynamixel_workbench_toolbox
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-dynamixel-sdk
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamixel-sdk
BuildRequires:  ros-melodic-roscpp

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
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Jun 04 2018 Pyo <pyo@robotis.com> - 0.3.0-0
- Autogenerated by Bloom

