# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugins

# >> macros
# << macros

Summary:    Nemo QML plugins source package.
Version:    0.3.5
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugins
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugins.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtContacts)
BuildRequires:  pkgconfig(mlite)
BuildRequires:  pkgconfig(QtSparql)

%description
Do not install this, install the subpackaged plugins.

%package contacts
Summary:    QML contacts plugin
Group:      System/Libraries

%description contacts
A more performant (and less problematic) QtContacts QML binding

%package contacts-tests
Summary:    QML contacts plugin tests
Group:      System/Libraries

%description contacts-tests
Tests for QML contacts plugin

%package messages
Summary:    Plugin providing public messages API
Group:      System/Libraries

%description messages
Plugin providing public API for interacting with messages applications

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%files contacts
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/contacts/libnemocontacts.so
%{_libdir}/qt4/imports/org/nemomobile/contacts/qmldir
# >> files contacts
# << files contacts

%files contacts-tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins/contacts/*
# >> files contacts-tests
# << files contacts-tests

%files messages
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/messages/libnemomessages.so
%{_libdir}/qt4/imports/org/nemomobile/messages/qmldir
# >> files messages
# << files messages
