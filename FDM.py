#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class FDM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "FDM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_sink_x_0_0_1_1_3 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_1_3.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_1_3_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_1_3.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_1_3.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_1_3_win)
        self.qtgui_sink_x_0_0_1_1_2 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_1_2.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_1_2_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_1_2.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_1_2.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_1_2_win)
        self.qtgui_sink_x_0_0_1_1_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_1_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_1_1_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_1_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_1_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_1_1_win)
        self.qtgui_sink_x_0_0_1_1_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_1_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_1_0_win)
        self.qtgui_sink_x_0_0_1_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_1_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_1_win)
        self.qtgui_sink_x_0_0_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m4", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m3", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m2", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m1", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.low_pass_filter_0_6 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                32000,
                1000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_5 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                32000,
                500,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_4 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                32000,
                1500,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_3 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                32000,
                2000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_2 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                1000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                2000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                1500,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                500,
                100,
                window.WIN_HAMMING,
                6.76))
        self.blocks_multiply_xx_1_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_1_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_1_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_1_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_2 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                4750,
                5250,
                50,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                4750,
                5250,
                50,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                4750,
                5250,
                50,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                4750,
                5250,
                50,
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_2_1_6 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 3000, 1, 1, 0)
        self.analog_sig_source_x_2_1_5 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2000, 1, 1, 0)
        self.analog_sig_source_x_2_1_4 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 4000, 1, 1, 0)
        self.analog_sig_source_x_2_1_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 5000, 1, 1, 0)
        self.analog_sig_source_x_2_1_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1500, 1, 1, 0)
        self.analog_sig_source_x_2_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2000, 1, 1, 0)
        self.analog_sig_source_x_2_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 1, 1, 0)
        self.analog_sig_source_x_2_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 500, 1, 1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_2_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_2_1_0, 0), (self.low_pass_filter_0_2, 0))
        self.connect((self.analog_sig_source_x_2_1_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.analog_sig_source_x_2_1_2, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_2_1_3, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_2_1_3, 0), (self.blocks_multiply_xx_1_1_0, 1))
        self.connect((self.analog_sig_source_x_2_1_4, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.analog_sig_source_x_2_1_4, 0), (self.blocks_multiply_xx_1_1_1, 1))
        self.connect((self.analog_sig_source_x_2_1_5, 0), (self.blocks_multiply_xx_1_1, 0))
        self.connect((self.analog_sig_source_x_2_1_5, 0), (self.blocks_multiply_xx_1_1_2, 1))
        self.connect((self.analog_sig_source_x_2_1_6, 0), (self.blocks_multiply_xx_1_1_3, 1))
        self.connect((self.analog_sig_source_x_2_1_6, 0), (self.blocks_multiply_xx_1_2, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1_1_2, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_1_1_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_multiply_xx_1_1_3, 0))
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_multiply_xx_1_1_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_sink_x_0_0_1_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_1_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_1_0, 0), (self.low_pass_filter_0_3, 0))
        self.connect((self.blocks_multiply_xx_1_1_1, 0), (self.low_pass_filter_0_4, 0))
        self.connect((self.blocks_multiply_xx_1_1_2, 0), (self.low_pass_filter_0_5, 0))
        self.connect((self.blocks_multiply_xx_1_1_3, 0), (self.low_pass_filter_0_6, 0))
        self.connect((self.blocks_multiply_xx_1_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_1_1, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0_1_1_2, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_sink_x_0_0_1_1_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_sink_x_0_0_1_1_0, 0))
        self.connect((self.low_pass_filter_0_2, 0), (self.blocks_multiply_xx_1_2, 1))
        self.connect((self.low_pass_filter_0_2, 0), (self.qtgui_sink_x_0_0_1_1_3, 0))
        self.connect((self.low_pass_filter_0_3, 0), (self.qtgui_sink_x_0_0_1, 0))
        self.connect((self.low_pass_filter_0_4, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.low_pass_filter_0_5, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_6, 0), (self.qtgui_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FDM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_2_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_5.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1_6.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 4750, 5250, 50, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 4750, 5250, 50, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, 4750, 5250, 50, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(1, self.samp_rate, 4750, 5250, 50, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 500, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 1500, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 2000, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(1, self.samp_rate, 1000, 100, window.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1_1_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1_1_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_1_1_3.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=FDM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
