#
# spec file for package rambox
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           wmail
Version:        1.3.8
Release:        0
Summary:        The missing desktop client for Gmail & Google Inbox
License:        MIT
Group:          Productivity/Networking/Mail
Url:            https://thomas101.github.io/wmail/
ExclusiveArch:  x86_64 %ix86
%ifarch x86_64
Source0:        https://github.com/Thomas101/wmail/releases/download/v%{version}/WMail_1_3_8_prerelease_linux_x64.tar.gz
Source9:        https://github.com/Thomas101/wmail/releases/download/v%{version}/WMail_1_3_8_prerelease_linux_x86.tar.gz
%endif
%ifarch %ix86
Source0:        https://github.com/Thomas101/wmail/releases/download/v%{version}/WMail_1_3_8_prerelease_linux_x86.tar.gz
Source9:        https://github.com/Thomas101/wmail/releases/download/v%{version}/WMail_1_3_8_prerelease_linux_x64.tar.gz
%endif
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh
Source4:        %{name}.1

BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
Bringing the Gmail & Google Inbox experience to your desktop in a neatly packaged app.

Wmail adds loads of features that mail on the web misses making your mail feel right at home on your computer. It's easy to use, fast and has all the features you're already enjoying on the web.

%prep
%ifarch x86_64
%setup -n WMail-linux-x64
%endif
%ifarch %ix86
%setup -n WMail-linux-ia32
%endif

%build

%install
install -d %{buildroot}/{opt/%{name},usr/{bin,share/{pixmaps,man/man1}}}
cp -R * %{buildroot}/opt/%{name}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE4} %{buildroot}%{_datadir}/man/man1
%suse_update_desktop_file -i %{name}
chmod +x %{buildroot}/opt/%{name}/WMail

# Let's use %%doc macro.
rm %{buildroot}/opt/%{name}/LICENSE*

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc LICENSE*
/opt/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*.?.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
