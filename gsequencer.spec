#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsequencer
Version  : 3.7.25
Release  : 13
URL      : https://download.savannah.nongnu.org/releases/gsequencer/3.7.x/gsequencer-3.7.25.tar.gz
Source0  : https://download.savannah.nongnu.org/releases/gsequencer/3.7.x/gsequencer-3.7.25.tar.gz
Summary  : Advanced Gtk+ Sequencer audio processing engine
Group    : Development/Tools
License  : AGPL-3.0 GFDL-1.3 GPL-3.0 MIT
Requires: gsequencer-bin = %{version}-%{release}
Requires: gsequencer-data = %{version}-%{release}
Requires: gsequencer-lib = %{version}-%{release}
Requires: gsequencer-license = %{version}-%{release}
Requires: gsequencer-locales = %{version}-%{release}
Requires: gsequencer-man = %{version}-%{release}
BuildRequires : CUnit-dev
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : dssi-dev
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : ladspa_sdk-dev
BuildRequires : libinstpatch-dev
BuildRequires : libxslt-bin
BuildRequires : lv2-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-app-1.0)
BuildRequires : pkgconfig(gstreamer-audio-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(webkit2gtk-4.0)

%description
Advanced Gtk+ Sequencer
====
The gsequencer binary provides you a user interface. It allows you to play, capture and create music. There is a piano roll,
automation and wave form editor. It has machines for playing drum samples, Soundfont2 sound containers and synthesizers. They
usually can be connected to a MIDI input source (instrument). All sources need to be connected to the sink provided by AgsPanel,
thus the properties dialog from machine's context menu is responsible. The engine is extensible by following plugin formats:
LADSPA, DSSI and LV2. It has support for various audio backends like ALSA, Pulseaudio, JACK, OSSv4 and CoreAudio.

%package bin
Summary: bin components for the gsequencer package.
Group: Binaries
Requires: gsequencer-data = %{version}-%{release}
Requires: gsequencer-license = %{version}-%{release}

%description bin
bin components for the gsequencer package.


%package data
Summary: data components for the gsequencer package.
Group: Data

%description data
data components for the gsequencer package.


%package dev
Summary: dev components for the gsequencer package.
Group: Development
Requires: gsequencer-lib = %{version}-%{release}
Requires: gsequencer-bin = %{version}-%{release}
Requires: gsequencer-data = %{version}-%{release}
Provides: gsequencer-devel = %{version}-%{release}
Requires: gsequencer = %{version}-%{release}

%description dev
dev components for the gsequencer package.


%package doc
Summary: doc components for the gsequencer package.
Group: Documentation
Requires: gsequencer-man = %{version}-%{release}

%description doc
doc components for the gsequencer package.


%package lib
Summary: lib components for the gsequencer package.
Group: Libraries
Requires: gsequencer-data = %{version}-%{release}
Requires: gsequencer-license = %{version}-%{release}

%description lib
lib components for the gsequencer package.


%package license
Summary: license components for the gsequencer package.
Group: Default

%description license
license components for the gsequencer package.


%package locales
Summary: locales components for the gsequencer package.
Group: Default

%description locales
locales components for the gsequencer package.


%package man
Summary: man components for the gsequencer package.
Group: Default

%description man
man components for the gsequencer package.


%prep
%setup -q -n gsequencer-3.7.25
cd %{_builddir}/gsequencer-3.7.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611103607
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --enable-pulse --disable-jack
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1611103607
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gsequencer
cp %{_builddir}/gsequencer-3.7.25/COPYING %{buildroot}/usr/share/package-licenses/gsequencer/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gsequencer-3.7.25/COPYING.docs %{buildroot}/usr/share/package-licenses/gsequencer/e1d31e42d2a477d6def889000aa8ffc251f2354c
cp %{_builddir}/gsequencer-3.7.25/COPYING.server %{buildroot}/usr/share/package-licenses/gsequencer/78e50e186b04c8fe1defaa098f1c192181b3d837
cp %{_builddir}/gsequencer-3.7.25/COPYING.stk-4.3 %{buildroot}/usr/share/package-licenses/gsequencer/4dd48cd5313054fa2d2b4d4aea8bd1084eee03cd
cp %{_builddir}/gsequencer-3.7.25/license-notice-gnu-agpl-3-0+-c.txt %{buildroot}/usr/share/package-licenses/gsequencer/f0577b80018542d52160156fa1ee8c69d47692c7
cp %{_builddir}/gsequencer-3.7.25/license-notice-gnu-agpl-3-0+-sym.txt %{buildroot}/usr/share/package-licenses/gsequencer/7ebc86f953750b510db38c5cd2a3bf4c814412a1
cp %{_builddir}/gsequencer-3.7.25/license-notice-gnu-gpl-3-0+-c.txt %{buildroot}/usr/share/package-licenses/gsequencer/19a9f9334535d8418421d7018a7ca0abe6d4c369
cp %{_builddir}/gsequencer-3.7.25/license-notice-gnu-gpl-3-0+-sym.txt %{buildroot}/usr/share/package-licenses/gsequencer/0064571b622bf5a778941c9610c02ad9a4e91d90
%make_install
%find_lang gsequencer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsequencer
/usr/bin/midi2xml

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Ags-3.0.typelib
/usr/lib64/girepository-1.0/AgsAudio-3.0.typelib
/usr/lib64/girepository-1.0/AgsGui-3.0.typelib
/usr/share/applications/gsequencer.desktop
/usr/share/gir-1.0/*.gir
/usr/share/gsequencer/icons/ags.png
/usr/share/gsequencer/icons/ags.xpm
/usr/share/gsequencer/icons/jumper.png
/usr/share/gsequencer/images/ags.png
/usr/share/gsequencer/images/gsequencer-800x450.png
/usr/share/gsequencer/styles/ags.css
/usr/share/icons/hicolor/128x128/apps/gsequencer.png
/usr/share/icons/hicolor/32x32/apps/gsequencer.png
/usr/share/icons/hicolor/48x48/apps/gsequencer.png
/usr/share/icons/hicolor/64x64/apps/gsequencer.png
/usr/share/metainfo/org.nongnu.gsequencer.gsequencer.appdata.xml
/usr/share/mime-packages/gsequencer.xml
/usr/share/xml/gsequencer/schema/dtd/3.7.25/ags_file.dtd
/usr/share/xml/gsequencer/schema/dtd/3.7.25/ags_midi_file.dtd
/usr/share/xml/gsequencer/schema/dtd/3.7.25/ags_osc_file.dtd
/usr/share/xml/gsequencer/schema/dtd/3.7.25/ags_simple_file.dtd
/usr/share/xml/gsequencer/stylesheet/ags-xsl/midi-xml/ags-simple.xsl
/usr/share/xml/gsequencer/stylesheet/ags-xsl/midi-xml/ags.xsl

%files dev
%defattr(-,root,root,-)
/usr/include/ags/ags_api_config.h
/usr/include/ags/audio/ags_acceleration.h
/usr/include/ags/audio/ags_audio.h
/usr/include/ags/audio/ags_audio_application_context.h
/usr/include/ags/audio/ags_audio_buffer_util.h
/usr/include/ags/audio/ags_audio_signal.h
/usr/include/ags/audio/ags_automation.h
/usr/include/ags/audio/ags_buffer.h
/usr/include/ags/audio/ags_channel.h
/usr/include/ags/audio/ags_char_buffer_util.h
/usr/include/ags/audio/ags_devin.h
/usr/include/ags/audio/ags_devout.h
/usr/include/ags/audio/ags_diatonic_scale.h
/usr/include/ags/audio/ags_fast_pitch_util.h
/usr/include/ags/audio/ags_fifoout.h
/usr/include/ags/audio/ags_filter_util.h
/usr/include/ags/audio/ags_fm_synth_util.h
/usr/include/ags/audio/ags_fourier_transform_util.h
/usr/include/ags/audio/ags_frequency_map.h
/usr/include/ags/audio/ags_frequency_map_manager.h
/usr/include/ags/audio/ags_fx_factory.h
/usr/include/ags/audio/ags_generic_recall_channel_run.h
/usr/include/ags/audio/ags_generic_recall_recycling.h
/usr/include/ags/audio/ags_input.h
/usr/include/ags/audio/ags_lfo_synth_util.h
/usr/include/ags/audio/ags_midi.h
/usr/include/ags/audio/ags_midiin.h
/usr/include/ags/audio/ags_notation.h
/usr/include/ags/audio/ags_note.h
/usr/include/ags/audio/ags_output.h
/usr/include/ags/audio/ags_pattern.h
/usr/include/ags/audio/ags_playback.h
/usr/include/ags/audio/ags_playback_domain.h
/usr/include/ags/audio/ags_port.h
/usr/include/ags/audio/ags_port_util.h
/usr/include/ags/audio/ags_preset.h
/usr/include/ags/audio/ags_recall.h
/usr/include/ags/audio/ags_recall_audio.h
/usr/include/ags/audio/ags_recall_audio_run.h
/usr/include/ags/audio/ags_recall_audio_signal.h
/usr/include/ags/audio/ags_recall_channel.h
/usr/include/ags/audio/ags_recall_channel_run.h
/usr/include/ags/audio/ags_recall_container.h
/usr/include/ags/audio/ags_recall_dependency.h
/usr/include/ags/audio/ags_recall_dssi.h
/usr/include/ags/audio/ags_recall_dssi_run.h
/usr/include/ags/audio/ags_recall_factory.h
/usr/include/ags/audio/ags_recall_id.h
/usr/include/ags/audio/ags_recall_ladspa.h
/usr/include/ags/audio/ags_recall_ladspa_run.h
/usr/include/ags/audio/ags_recall_lv2.h
/usr/include/ags/audio/ags_recall_lv2_run.h
/usr/include/ags/audio/ags_recall_recycling.h
/usr/include/ags/audio/ags_recycling.h
/usr/include/ags/audio/ags_recycling_context.h
/usr/include/ags/audio/ags_sequencer_util.h
/usr/include/ags/audio/ags_sf2_synth_generator.h
/usr/include/ags/audio/ags_sf2_synth_util.h
/usr/include/ags/audio/ags_sfz_synth_generator.h
/usr/include/ags/audio/ags_sfz_synth_util.h
/usr/include/ags/audio/ags_sound_enums.h
/usr/include/ags/audio/ags_sound_provider.h
/usr/include/ags/audio/ags_soundcard_util.h
/usr/include/ags/audio/ags_synth_enums.h
/usr/include/ags/audio/ags_synth_generator.h
/usr/include/ags/audio/ags_synth_util.h
/usr/include/ags/audio/ags_track.h
/usr/include/ags/audio/ags_wave.h
/usr/include/ags/audio/audio-unit/ags_audio_unit_client.h
/usr/include/ags/audio/audio-unit/ags_audio_unit_devin.h
/usr/include/ags/audio/audio-unit/ags_audio_unit_devout.h
/usr/include/ags/audio/audio-unit/ags_audio_unit_port.h
/usr/include/ags/audio/audio-unit/ags_audio_unit_server.h
/usr/include/ags/audio/core-audio/ags_core_audio_client.h
/usr/include/ags/audio/core-audio/ags_core_audio_devin.h
/usr/include/ags/audio/core-audio/ags_core_audio_devout.h
/usr/include/ags/audio/core-audio/ags_core_audio_midiin.h
/usr/include/ags/audio/core-audio/ags_core_audio_port.h
/usr/include/ags/audio/core-audio/ags_core_audio_server.h
/usr/include/ags/audio/file/ags_audio_container.h
/usr/include/ags/audio/file/ags_audio_container_manager.h
/usr/include/ags/audio/file/ags_audio_file.h
/usr/include/ags/audio/file/ags_audio_file_link.h
/usr/include/ags/audio/file/ags_audio_file_manager.h
/usr/include/ags/audio/file/ags_gstreamer_file.h
/usr/include/ags/audio/file/ags_ipatch.h
/usr/include/ags/audio/file/ags_ipatch_dls2_reader.h
/usr/include/ags/audio/file/ags_ipatch_gig_reader.h
/usr/include/ags/audio/file/ags_ipatch_sample.h
/usr/include/ags/audio/file/ags_ipatch_sf2_reader.h
/usr/include/ags/audio/file/ags_sfz_file.h
/usr/include/ags/audio/file/ags_sfz_group.h
/usr/include/ags/audio/file/ags_sfz_region.h
/usr/include/ags/audio/file/ags_sfz_sample.h
/usr/include/ags/audio/file/ags_sndfile.h
/usr/include/ags/audio/file/ags_sound_container.h
/usr/include/ags/audio/file/ags_sound_resource.h
/usr/include/ags/audio/fx/ags_fx_analyse_audio.h
/usr/include/ags/audio/fx/ags_fx_analyse_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_analyse_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_analyse_channel.h
/usr/include/ags/audio/fx/ags_fx_analyse_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_analyse_recycling.h
/usr/include/ags/audio/fx/ags_fx_buffer_audio.h
/usr/include/ags/audio/fx/ags_fx_buffer_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_buffer_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_buffer_channel.h
/usr/include/ags/audio/fx/ags_fx_buffer_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_buffer_recycling.h
/usr/include/ags/audio/fx/ags_fx_dssi_audio.h
/usr/include/ags/audio/fx/ags_fx_dssi_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_dssi_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_dssi_channel.h
/usr/include/ags/audio/fx/ags_fx_dssi_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_dssi_recycling.h
/usr/include/ags/audio/fx/ags_fx_envelope_audio.h
/usr/include/ags/audio/fx/ags_fx_envelope_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_envelope_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_envelope_channel.h
/usr/include/ags/audio/fx/ags_fx_envelope_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_envelope_recycling.h
/usr/include/ags/audio/fx/ags_fx_eq10_audio.h
/usr/include/ags/audio/fx/ags_fx_eq10_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_eq10_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_eq10_channel.h
/usr/include/ags/audio/fx/ags_fx_eq10_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_eq10_recycling.h
/usr/include/ags/audio/fx/ags_fx_ladspa_audio.h
/usr/include/ags/audio/fx/ags_fx_ladspa_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_ladspa_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_ladspa_channel.h
/usr/include/ags/audio/fx/ags_fx_ladspa_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_ladspa_recycling.h
/usr/include/ags/audio/fx/ags_fx_lv2_audio.h
/usr/include/ags/audio/fx/ags_fx_lv2_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_lv2_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_lv2_channel.h
/usr/include/ags/audio/fx/ags_fx_lv2_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_lv2_recycling.h
/usr/include/ags/audio/fx/ags_fx_notation_audio.h
/usr/include/ags/audio/fx/ags_fx_notation_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_notation_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_notation_channel.h
/usr/include/ags/audio/fx/ags_fx_notation_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_notation_recycling.h
/usr/include/ags/audio/fx/ags_fx_pattern_audio.h
/usr/include/ags/audio/fx/ags_fx_pattern_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_pattern_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_pattern_channel.h
/usr/include/ags/audio/fx/ags_fx_pattern_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_pattern_recycling.h
/usr/include/ags/audio/fx/ags_fx_peak_audio.h
/usr/include/ags/audio/fx/ags_fx_peak_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_peak_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_peak_channel.h
/usr/include/ags/audio/fx/ags_fx_peak_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_peak_recycling.h
/usr/include/ags/audio/fx/ags_fx_playback_audio.h
/usr/include/ags/audio/fx/ags_fx_playback_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_playback_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_playback_channel.h
/usr/include/ags/audio/fx/ags_fx_playback_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_playback_recycling.h
/usr/include/ags/audio/fx/ags_fx_volume_audio.h
/usr/include/ags/audio/fx/ags_fx_volume_audio_processor.h
/usr/include/ags/audio/fx/ags_fx_volume_audio_signal.h
/usr/include/ags/audio/fx/ags_fx_volume_channel.h
/usr/include/ags/audio/fx/ags_fx_volume_channel_processor.h
/usr/include/ags/audio/fx/ags_fx_volume_recycling.h
/usr/include/ags/audio/gstreamer/ags_gstreamer_client.h
/usr/include/ags/audio/gstreamer/ags_gstreamer_devin.h
/usr/include/ags/audio/gstreamer/ags_gstreamer_devout.h
/usr/include/ags/audio/gstreamer/ags_gstreamer_port.h
/usr/include/ags/audio/gstreamer/ags_gstreamer_server.h
/usr/include/ags/audio/jack/ags_jack_client.h
/usr/include/ags/audio/jack/ags_jack_devin.h
/usr/include/ags/audio/jack/ags_jack_devout.h
/usr/include/ags/audio/jack/ags_jack_midiin.h
/usr/include/ags/audio/jack/ags_jack_port.h
/usr/include/ags/audio/jack/ags_jack_server.h
/usr/include/ags/audio/midi/ags_midi_buffer_util.h
/usr/include/ags/audio/midi/ags_midi_builder.h
/usr/include/ags/audio/midi/ags_midi_file.h
/usr/include/ags/audio/midi/ags_midi_parser.h
/usr/include/ags/audio/midi/ags_midi_util.h
/usr/include/ags/audio/osc/ags_osc_buffer_util.h
/usr/include/ags/audio/osc/ags_osc_builder.h
/usr/include/ags/audio/osc/ags_osc_client.h
/usr/include/ags/audio/osc/ags_osc_connection.h
/usr/include/ags/audio/osc/ags_osc_message.h
/usr/include/ags/audio/osc/ags_osc_parser.h
/usr/include/ags/audio/osc/ags_osc_response.h
/usr/include/ags/audio/osc/ags_osc_server.h
/usr/include/ags/audio/osc/ags_osc_util.h
/usr/include/ags/audio/osc/ags_osc_websocket_connection.h
/usr/include/ags/audio/osc/ags_osc_xmlrpc_message.h
/usr/include/ags/audio/osc/ags_osc_xmlrpc_server.h
/usr/include/ags/audio/osc/controller/ags_osc_action_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_config_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_export_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_front_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_info_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_meter_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_node_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_plugin_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_renew_controller.h
/usr/include/ags/audio/osc/controller/ags_osc_status_controller.h
/usr/include/ags/audio/osc/xmlrpc/ags_osc_xmlrpc_controller.h
/usr/include/ags/audio/pulse/ags_pulse_client.h
/usr/include/ags/audio/pulse/ags_pulse_devin.h
/usr/include/ags/audio/pulse/ags_pulse_devout.h
/usr/include/ags/audio/pulse/ags_pulse_port.h
/usr/include/ags/audio/pulse/ags_pulse_server.h
/usr/include/ags/audio/recall/ags_analyse_audio_signal.h
/usr/include/ags/audio/recall/ags_analyse_channel.h
/usr/include/ags/audio/recall/ags_analyse_channel_run.h
/usr/include/ags/audio/recall/ags_analyse_recycling.h
/usr/include/ags/audio/recall/ags_buffer_audio_signal.h
/usr/include/ags/audio/recall/ags_buffer_channel.h
/usr/include/ags/audio/recall/ags_buffer_channel_run.h
/usr/include/ags/audio/recall/ags_buffer_recycling.h
/usr/include/ags/audio/recall/ags_capture_wave_audio.h
/usr/include/ags/audio/recall/ags_capture_wave_audio_run.h
/usr/include/ags/audio/recall/ags_capture_wave_channel.h
/usr/include/ags/audio/recall/ags_capture_wave_channel_run.h
/usr/include/ags/audio/recall/ags_copy_audio_signal.h
/usr/include/ags/audio/recall/ags_copy_channel.h
/usr/include/ags/audio/recall/ags_copy_channel_run.h
/usr/include/ags/audio/recall/ags_copy_pattern_audio.h
/usr/include/ags/audio/recall/ags_copy_pattern_audio_run.h
/usr/include/ags/audio/recall/ags_copy_pattern_channel.h
/usr/include/ags/audio/recall/ags_copy_pattern_channel_run.h
/usr/include/ags/audio/recall/ags_copy_recycling.h
/usr/include/ags/audio/recall/ags_count_beats_audio.h
/usr/include/ags/audio/recall/ags_count_beats_audio_run.h
/usr/include/ags/audio/recall/ags_delay_audio.h
/usr/include/ags/audio/recall/ags_delay_audio_run.h
/usr/include/ags/audio/recall/ags_envelope_audio_signal.h
/usr/include/ags/audio/recall/ags_envelope_channel.h
/usr/include/ags/audio/recall/ags_envelope_channel_run.h
/usr/include/ags/audio/recall/ags_envelope_recycling.h
/usr/include/ags/audio/recall/ags_eq10_audio_signal.h
/usr/include/ags/audio/recall/ags_eq10_channel.h
/usr/include/ags/audio/recall/ags_eq10_channel_run.h
/usr/include/ags/audio/recall/ags_eq10_recycling.h
/usr/include/ags/audio/recall/ags_feed_audio_signal.h
/usr/include/ags/audio/recall/ags_feed_channel.h
/usr/include/ags/audio/recall/ags_feed_channel_run.h
/usr/include/ags/audio/recall/ags_feed_recycling.h
/usr/include/ags/audio/recall/ags_lfo_audio_signal.h
/usr/include/ags/audio/recall/ags_lfo_channel.h
/usr/include/ags/audio/recall/ags_lfo_channel_run.h
/usr/include/ags/audio/recall/ags_lfo_recycling.h
/usr/include/ags/audio/recall/ags_loop_channel.h
/usr/include/ags/audio/recall/ags_loop_channel_run.h
/usr/include/ags/audio/recall/ags_mute_audio.h
/usr/include/ags/audio/recall/ags_mute_audio_run.h
/usr/include/ags/audio/recall/ags_mute_audio_signal.h
/usr/include/ags/audio/recall/ags_mute_channel.h
/usr/include/ags/audio/recall/ags_mute_channel_run.h
/usr/include/ags/audio/recall/ags_mute_recycling.h
/usr/include/ags/audio/recall/ags_peak_audio_signal.h
/usr/include/ags/audio/recall/ags_peak_channel.h
/usr/include/ags/audio/recall/ags_peak_channel_run.h
/usr/include/ags/audio/recall/ags_peak_recycling.h
/usr/include/ags/audio/recall/ags_play_audio.h
/usr/include/ags/audio/recall/ags_play_audio_signal.h
/usr/include/ags/audio/recall/ags_play_channel.h
/usr/include/ags/audio/recall/ags_play_channel_run.h
/usr/include/ags/audio/recall/ags_play_channel_run_master.h
/usr/include/ags/audio/recall/ags_play_dssi_audio.h
/usr/include/ags/audio/recall/ags_play_dssi_audio_run.h
/usr/include/ags/audio/recall/ags_play_lv2_audio.h
/usr/include/ags/audio/recall/ags_play_lv2_audio_run.h
/usr/include/ags/audio/recall/ags_play_notation_audio.h
/usr/include/ags/audio/recall/ags_play_notation_audio_run.h
/usr/include/ags/audio/recall/ags_play_recycling.h
/usr/include/ags/audio/recall/ags_play_wave_audio.h
/usr/include/ags/audio/recall/ags_play_wave_audio_run.h
/usr/include/ags/audio/recall/ags_play_wave_channel.h
/usr/include/ags/audio/recall/ags_play_wave_channel_run.h
/usr/include/ags/audio/recall/ags_prepare_audio_signal.h
/usr/include/ags/audio/recall/ags_prepare_channel.h
/usr/include/ags/audio/recall/ags_prepare_channel_run.h
/usr/include/ags/audio/recall/ags_prepare_recycling.h
/usr/include/ags/audio/recall/ags_record_midi_audio.h
/usr/include/ags/audio/recall/ags_record_midi_audio_run.h
/usr/include/ags/audio/recall/ags_route_dssi_audio.h
/usr/include/ags/audio/recall/ags_route_dssi_audio_run.h
/usr/include/ags/audio/recall/ags_route_lv2_audio.h
/usr/include/ags/audio/recall/ags_route_lv2_audio_run.h
/usr/include/ags/audio/recall/ags_rt_stream_audio_signal.h
/usr/include/ags/audio/recall/ags_rt_stream_channel.h
/usr/include/ags/audio/recall/ags_rt_stream_channel_run.h
/usr/include/ags/audio/recall/ags_rt_stream_recycling.h
/usr/include/ags/audio/recall/ags_stream_audio_signal.h
/usr/include/ags/audio/recall/ags_stream_channel.h
/usr/include/ags/audio/recall/ags_stream_channel_run.h
/usr/include/ags/audio/recall/ags_stream_recycling.h
/usr/include/ags/audio/recall/ags_volume_audio_signal.h
/usr/include/ags/audio/recall/ags_volume_channel.h
/usr/include/ags/audio/recall/ags_volume_channel_run.h
/usr/include/ags/audio/recall/ags_volume_recycling.h
/usr/include/ags/audio/task/ags_add_audio.h
/usr/include/ags/audio/task/ags_add_audio_signal.h
/usr/include/ags/audio/task/ags_add_effect.h
/usr/include/ags/audio/task/ags_add_note.h
/usr/include/ags/audio/task/ags_add_soundcard.h
/usr/include/ags/audio/task/ags_apply_bpm.h
/usr/include/ags/audio/task/ags_apply_presets.h
/usr/include/ags/audio/task/ags_apply_sequencer_length.h
/usr/include/ags/audio/task/ags_apply_sf2_synth.h
/usr/include/ags/audio/task/ags_apply_sfz_synth.h
/usr/include/ags/audio/task/ags_apply_sound_config.h
/usr/include/ags/audio/task/ags_apply_synth.h
/usr/include/ags/audio/task/ags_apply_tact.h
/usr/include/ags/audio/task/ags_cancel_audio.h
/usr/include/ags/audio/task/ags_cancel_channel.h
/usr/include/ags/audio/task/ags_clear_audio_signal.h
/usr/include/ags/audio/task/ags_clear_buffer.h
/usr/include/ags/audio/task/ags_crop_note.h
/usr/include/ags/audio/task/ags_export_output.h
/usr/include/ags/audio/task/ags_free_selection.h
/usr/include/ags/audio/task/ags_link_channel.h
/usr/include/ags/audio/task/ags_move_note.h
/usr/include/ags/audio/task/ags_open_file.h
/usr/include/ags/audio/task/ags_open_sf2_instrument.h
/usr/include/ags/audio/task/ags_open_sf2_sample.h
/usr/include/ags/audio/task/ags_open_sfz_file.h
/usr/include/ags/audio/task/ags_open_single_file.h
/usr/include/ags/audio/task/ags_open_wave.h
/usr/include/ags/audio/task/ags_remove_audio.h
/usr/include/ags/audio/task/ags_remove_audio_signal.h
/usr/include/ags/audio/task/ags_remove_note.h
/usr/include/ags/audio/task/ags_remove_soundcard.h
/usr/include/ags/audio/task/ags_reset_amplitude.h
/usr/include/ags/audio/task/ags_reset_fx_analyse.h
/usr/include/ags/audio/task/ags_reset_fx_peak.h
/usr/include/ags/audio/task/ags_reset_note.h
/usr/include/ags/audio/task/ags_reset_peak.h
/usr/include/ags/audio/task/ags_resize_audio.h
/usr/include/ags/audio/task/ags_seek_soundcard.h
/usr/include/ags/audio/task/ags_set_audio_channels.h
/usr/include/ags/audio/task/ags_set_buffer_size.h
/usr/include/ags/audio/task/ags_set_device.h
/usr/include/ags/audio/task/ags_set_format.h
/usr/include/ags/audio/task/ags_set_muted.h
/usr/include/ags/audio/task/ags_set_samplerate.h
/usr/include/ags/audio/task/ags_start_audio.h
/usr/include/ags/audio/task/ags_start_channel.h
/usr/include/ags/audio/task/ags_start_sequencer.h
/usr/include/ags/audio/task/ags_start_soundcard.h
/usr/include/ags/audio/task/ags_stop_sequencer.h
/usr/include/ags/audio/task/ags_stop_soundcard.h
/usr/include/ags/audio/task/ags_switch_buffer_flag.h
/usr/include/ags/audio/task/ags_tic_device.h
/usr/include/ags/audio/task/ags_toggle_pattern_bit.h
/usr/include/ags/audio/thread/ags_audio_loop.h
/usr/include/ags/audio/thread/ags_audio_thread.h
/usr/include/ags/audio/thread/ags_channel_thread.h
/usr/include/ags/audio/thread/ags_export_thread.h
/usr/include/ags/audio/thread/ags_sequencer_thread.h
/usr/include/ags/audio/thread/ags_sf2_loader.h
/usr/include/ags/audio/thread/ags_sfz_loader.h
/usr/include/ags/audio/thread/ags_soundcard_thread.h
/usr/include/ags/audio/thread/ags_wave_loader.h
/usr/include/ags/audio/wasapi/ags_wasapi_devin.h
/usr/include/ags/audio/wasapi/ags_wasapi_devout.h
/usr/include/ags/file/ags_file.h
/usr/include/ags/file/ags_file_id_ref.h
/usr/include/ags/file/ags_file_launch.h
/usr/include/ags/file/ags_file_link.h
/usr/include/ags/file/ags_file_lookup.h
/usr/include/ags/lib/ags_buffer_util.h
/usr/include/ags/lib/ags_complex.h
/usr/include/ags/lib/ags_conversion.h
/usr/include/ags/lib/ags_endian.h
/usr/include/ags/lib/ags_function.h
/usr/include/ags/lib/ags_log.h
/usr/include/ags/lib/ags_math_util.h
/usr/include/ags/lib/ags_regex.h
/usr/include/ags/lib/ags_solver_matrix.h
/usr/include/ags/lib/ags_solver_polynomial.h
/usr/include/ags/lib/ags_solver_vector.h
/usr/include/ags/lib/ags_string_util.h
/usr/include/ags/lib/ags_time.h
/usr/include/ags/lib/ags_turtle.h
/usr/include/ags/lib/ags_turtle_manager.h
/usr/include/ags/lib/ags_uuid.h
/usr/include/ags/libags-audio.h
/usr/include/ags/libags-gui.h
/usr/include/ags/libags.h
/usr/include/ags/object/ags_applicable.h
/usr/include/ags/object/ags_application_context.h
/usr/include/ags/object/ags_config.h
/usr/include/ags/object/ags_connectable.h
/usr/include/ags/object/ags_countable.h
/usr/include/ags/object/ags_cursor.h
/usr/include/ags/object/ags_globals.h
/usr/include/ags/object/ags_macros.h
/usr/include/ags/object/ags_main_loop.h
/usr/include/ags/object/ags_marshal.h
/usr/include/ags/object/ags_mutable.h
/usr/include/ags/object/ags_plugin.h
/usr/include/ags/object/ags_portlet.h
/usr/include/ags/object/ags_priority.h
/usr/include/ags/object/ags_seekable.h
/usr/include/ags/object/ags_sequencer.h
/usr/include/ags/object/ags_sound_server.h
/usr/include/ags/object/ags_soundcard.h
/usr/include/ags/object/ags_tactable.h
/usr/include/ags/plugin/ags_base_plugin.h
/usr/include/ags/plugin/ags_dssi_manager.h
/usr/include/ags/plugin/ags_dssi_plugin.h
/usr/include/ags/plugin/ags_ladspa_conversion.h
/usr/include/ags/plugin/ags_ladspa_manager.h
/usr/include/ags/plugin/ags_ladspa_plugin.h
/usr/include/ags/plugin/ags_lv2_conversion.h
/usr/include/ags/plugin/ags_lv2_event_manager.h
/usr/include/ags/plugin/ags_lv2_log_manager.h
/usr/include/ags/plugin/ags_lv2_manager.h
/usr/include/ags/plugin/ags_lv2_option_manager.h
/usr/include/ags/plugin/ags_lv2_plugin.h
/usr/include/ags/plugin/ags_lv2_preset.h
/usr/include/ags/plugin/ags_lv2_preset_manager.h
/usr/include/ags/plugin/ags_lv2_turtle_parser.h
/usr/include/ags/plugin/ags_lv2_turtle_scanner.h
/usr/include/ags/plugin/ags_lv2_uri_map_manager.h
/usr/include/ags/plugin/ags_lv2_urid_manager.h
/usr/include/ags/plugin/ags_lv2_worker.h
/usr/include/ags/plugin/ags_lv2_worker_manager.h
/usr/include/ags/plugin/ags_lv2ui_manager.h
/usr/include/ags/plugin/ags_lv2ui_plugin.h
/usr/include/ags/plugin/ags_plugin_port.h
/usr/include/ags/plugin/ags_plugin_stock.h
/usr/include/ags/server/ags_registry.h
/usr/include/ags/server/ags_server.h
/usr/include/ags/server/ags_server_application_context.h
/usr/include/ags/server/ags_server_status.h
/usr/include/ags/server/ags_service_provider.h
/usr/include/ags/server/controller/ags_controller.h
/usr/include/ags/server/controller/ags_front_controller.h
/usr/include/ags/server/controller/ags_plugin_controller.h
/usr/include/ags/server/security/ags_auth_security_context.h
/usr/include/ags/server/security/ags_authentication.h
/usr/include/ags/server/security/ags_authentication_manager.h
/usr/include/ags/server/security/ags_business_group.h
/usr/include/ags/server/security/ags_business_group_manager.h
/usr/include/ags/server/security/ags_certificate.h
/usr/include/ags/server/security/ags_certificate_manager.h
/usr/include/ags/server/security/ags_password_store.h
/usr/include/ags/server/security/ags_password_store_manager.h
/usr/include/ags/server/security/ags_security_context.h
/usr/include/ags/server/security/ags_xml_authentication.h
/usr/include/ags/server/security/ags_xml_business_group.h
/usr/include/ags/server/security/ags_xml_certificate.h
/usr/include/ags/server/security/ags_xml_password_store.h
/usr/include/ags/thread/ags_concurrency_provider.h
/usr/include/ags/thread/ags_destroy_worker.h
/usr/include/ags/thread/ags_generic_main_loop.h
/usr/include/ags/thread/ags_message_delivery.h
/usr/include/ags/thread/ags_message_envelope.h
/usr/include/ags/thread/ags_message_queue.h
/usr/include/ags/thread/ags_returnable_thread.h
/usr/include/ags/thread/ags_task.h
/usr/include/ags/thread/ags_task_completion.h
/usr/include/ags/thread/ags_task_launcher.h
/usr/include/ags/thread/ags_thread.h
/usr/include/ags/thread/ags_thread_application_context.h
/usr/include/ags/thread/ags_thread_pool.h
/usr/include/ags/thread/ags_timestamp.h
/usr/include/ags/thread/ags_worker_thread.h
/usr/include/ags/util/ags_destroy_util.h
/usr/include/ags/util/ags_id_generator.h
/usr/include/ags/util/ags_list_util.h
/usr/include/ags/util/ags_soundcard_helper.h
/usr/include/ags/widget/ags_cartesian.h
/usr/include/ags/widget/ags_container.h
/usr/include/ags/widget/ags_dial.h
/usr/include/ags/widget/ags_expander.h
/usr/include/ags/widget/ags_expander_set.h
/usr/include/ags/widget/ags_hindicator.h
/usr/include/ags/widget/ags_hled_array.h
/usr/include/ags/widget/ags_hlevel_box.h
/usr/include/ags/widget/ags_hscale_box.h
/usr/include/ags/widget/ags_indicator.h
/usr/include/ags/widget/ags_led.h
/usr/include/ags/widget/ags_led_array.h
/usr/include/ags/widget/ags_level.h
/usr/include/ags/widget/ags_level_box.h
/usr/include/ags/widget/ags_notebook.h
/usr/include/ags/widget/ags_piano.h
/usr/include/ags/widget/ags_piano_keys.h
/usr/include/ags/widget/ags_ruler.h
/usr/include/ags/widget/ags_scale.h
/usr/include/ags/widget/ags_scale_box.h
/usr/include/ags/widget/ags_scrolled_level_box.h
/usr/include/ags/widget/ags_scrolled_piano.h
/usr/include/ags/widget/ags_scrolled_scale_box.h
/usr/include/ags/widget/ags_vindicator.h
/usr/include/ags/widget/ags_vled_array.h
/usr/include/ags/widget/ags_vlevel_box.h
/usr/include/ags/widget/ags_vscale_box.h
/usr/include/ags/widget/ags_widget_marshal.h
/usr/lib64/libags.so
/usr/lib64/libags_audio.so
/usr/lib64/libags_gui.so
/usr/lib64/libags_server.so
/usr/lib64/libags_thread.so
/usr/lib64/libgsequencer.so
/usr/lib64/pkgconfig/libags.pc
/usr/lib64/pkgconfig/libags_audio.pc
/usr/lib64/pkgconfig/libags_gui.pc
/usr/lib64/pkgconfig/libgsequencer.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gsequencer/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libags.so.3
/usr/lib64/libags.so.3.0.0
/usr/lib64/libags_audio.so.3
/usr/lib64/libags_audio.so.3.0.0
/usr/lib64/libags_gui.so.3
/usr/lib64/libags_gui.so.3.0.0
/usr/lib64/libags_server.so.3
/usr/lib64/libags_server.so.3.0.0
/usr/lib64/libags_thread.so.3
/usr/lib64/libags_thread.so.3.0.0
/usr/lib64/libgsequencer.so.0
/usr/lib64/libgsequencer.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsequencer/0064571b622bf5a778941c9610c02ad9a4e91d90
/usr/share/package-licenses/gsequencer/19a9f9334535d8418421d7018a7ca0abe6d4c369
/usr/share/package-licenses/gsequencer/4dd48cd5313054fa2d2b4d4aea8bd1084eee03cd
/usr/share/package-licenses/gsequencer/78e50e186b04c8fe1defaa098f1c192181b3d837
/usr/share/package-licenses/gsequencer/7ebc86f953750b510db38c5cd2a3bf4c814412a1
/usr/share/package-licenses/gsequencer/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gsequencer/e1d31e42d2a477d6def889000aa8ffc251f2354c
/usr/share/package-licenses/gsequencer/f0577b80018542d52160156fa1ee8c69d47692c7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gsequencer.1
/usr/share/man/man1/midi2xml.1

%files locales -f gsequencer.lang
%defattr(-,root,root,-)

