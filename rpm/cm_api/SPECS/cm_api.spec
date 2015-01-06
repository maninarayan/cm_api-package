# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%define cm_api_name cm_api
%define lib_cm_api /usr/lib/%{cm_api_name}

# disable repacking jars
%define __os_install_post %{nil}

Name: cm_api
Version: %{cm_api_version}
Release: %{cm_api_release}
Summary: Lightning-Fast Cluster Computing
URL: http://cloudera.github.io/cm_api/
Group: Development/Libraries
BuildArch: noarch
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: ASL 2.0
Source0: %{cm_api_name}-%{cm_api_patched_version}.tar.gz
Source1: do-component-build 
Source2: install_%{cm_api_name}.sh

%description 
Cloudera Manager's REST API lets you work with existing tools and programmatically manage your Hadoop Cluster.

%prep
%setup -n %{cm_api_name}-%{cm_api_patched_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT

bash $RPM_SOURCE_DIR/install_cm_api.sh \
          --build-dir=`pwd`         \
          --prefix=$RPM_BUILD_ROOT


#######################
#### FILES SECTION ####
#######################
%files
%defattr(-,root,root,755)
%{lib_cm_api}

