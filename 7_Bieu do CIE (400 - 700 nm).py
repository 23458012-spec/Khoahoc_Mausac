import colour
import numpy as np
import matplotlib.pyplot as plt

# CIE 1931 - Standard Observer 2°
cmfs = colour.MSDS_CMFS[
    "CIE 1931 2 Degree Standard Observer"
]

# Giới hạn bước sóng từ 400 đến 700 nm
cmfs_400_700 = cmfs.copy().align(
    colour.SpectralShape(400, 700, 1)
)

XYZ = cmfs_400_700.values
xy = XYZ[:, :2] / np.sum(XYZ, axis=1)[:, None]

# Vẽ đường biên phổ
plt.figure(figsize=(8, 7))
plt.plot(xy[:, 0], xy[:, 1], "k-", linewidth=1.5)
plt.plot(
    [xy[-1, 0], xy[0, 0]],
    [xy[-1, 1], xy[0, 1]],
    "k-"
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("CIE 1931 Chromaticity Diagram (400–700 nm)")
plt.xlim(0, 0.8)
plt.ylim(0, 0.9)
plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.show()