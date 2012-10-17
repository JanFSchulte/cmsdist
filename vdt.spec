### RPM cms vdt V0.2.1

Source: svn://svnweb.cern.ch/guest/%{n}/tags/%{realversion}?scheme=http&strategy=export&module=%{n}&output=/%{n}-%{realversion}.tar.gz

BuildRequires: cmake

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%define keep_archives true

%prep
%setup -q -n %{n}

%build
cmake . \
  -DCMAKE_CXX_COMPILER="%cms_cxx" \
  -DCMAKE_INSTALL_PREFIX=%i

make %makeprocesses VERBOSE=1

%install
make install
