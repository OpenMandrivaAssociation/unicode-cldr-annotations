Name:		unicode-cldr-annotations
Version:	33.0.0_1
Release:	2
Summary:	Annotation files from the Unicode Common Locale Data Repository
Group:		System/Libraries
URL:		http://cldr.unicode.org/
License:	Unicode License (BSD-like)
Source0:	https://github.com/fujiwarat/cldr-emoji-annotation/archive/%{version}.tar.gz
Source10:       http://www.unicode.org/Public/emoji/11.0/emoji-data.txt
Source11:       http://www.unicode.org/Public/emoji/11.0/emoji-sequences.txt
Source12:       http://www.unicode.org/Public/emoji/11.0/emoji-test.txt
Source13:       http://www.unicode.org/Public/emoji/11.0/emoji-variation-sequences.txt
Source14:       http://www.unicode.org/Public/emoji/11.0/emoji-zwj-sequences.txt
Source20:	https://www.unicode.org/Public/UNIDATA/UCD.zip
BuildArch:	noarch
BuildRequires:	unzip

%description
Annotation files from the Unicode Common Locale Data Repository

%prep
%autosetup -n cldr-emoji-annotation-%{version}
./autogen.sh
%configure

%build
%make

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/unicode/emoji
install -m644 %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{buildroot}%{_datadir}/unicode/emoji/
mkdir -p %{buildroot}%{_datadir}/unicode/ucd
cd %{buildroot}%{_datadir}/unicode/ucd
unzip %{S:20}

%files
%{_datadir}/unicode/emoji
%{_datadir}/unicode/cldr/common/annotations
%{_datadir}/unicode/cldr/common/annotationsDerived
%{_datadir}/unicode/ucd
%{_datadir}/pkgconfig/cldr-emoji-annotation.pc
