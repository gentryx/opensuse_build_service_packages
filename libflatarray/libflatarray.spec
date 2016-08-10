#
# spec file for package LibFlatArray
#


Name:		libflatarray
Version:	0.3.0
Release:	0.3.0
Summary:	An SoA array library for C++
Group:		Development/Libraries/C++
License:	Boost
URL:		http://libgeodecomp.org/libflatarray.html
Source0:	%{name}_%{version}.tar.gz
BuildRequires:  cmake gcc gcc-c++ wget
Autoreqprov:    on

%description
fixme

%package devel
Group:		Development/Libraries/C++
Summary: Development files for libflatarray
Requires: cmake

%description devel
fixme2

%prep
tar -xf ../SOURCES/libflatarray_0.3.0.tar.gz
mv libflatarray-0.3.0/* .
rm -rf libflatarray-0.3.0/

%build
cmake -DLIB_INSTALL_DIR=%_lib -DCMAKE_INSTALL_PREFIX=%buildroot/%_prefix .
make

%install
make install

%files devel
%_prefix/include/libflatarray
%_libdir/cmake
