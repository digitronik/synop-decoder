from distutils.core import setup
import py2exe

#setup(windows=["Attendance.py"])  # without icon

setup(
    windows = [
        {
            "script": "SYNOP Decoder.py",
            "icon_resources":[(1, "figures/decoder-64x64.ico")]
        }
    ],
)