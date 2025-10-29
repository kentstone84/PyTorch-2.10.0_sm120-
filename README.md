# PyTorch 2.10 for RTX 5080 - Windows 11

## Requirements
- Windows 11
- Python 3.10 or 3.11
- NVIDIA GeForce RTX 5080
- Latest NVIDIA drivers (560+)

## Installation

1. Create a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Run the installer:
```powershell
.\install.ps1
```

## Verify Installation
```powershell
python -c "import torch; print(torch.cuda.is_available())"
```

## Package Contents
- PyTorch 2.10.0a0 (custom build for SM 120 / Blackwell)
- CUDA 13.0 runtime libraries
- cuDNN support
- All required DLL dependencies

## Build Info
- Built with CUDA 13.0
- Compute capability: SM 120 (Blackwell)
- Build date: [ADD DATE]
- Source: PyTorch main branch

## Troubleshooting

If you get DLL errors:
1. Ensure you have the latest NVIDIA drivers
2. Check that Python 3.10 or 3.11 is being used
3. Make sure you're in a clean virtual environment

## License
PyTorch is BSD-licensed. See torch/LICENSE for details.


## Verification
SHA256: `6202cfa3f4dac89e87bd21b754b3778288849428576e1bfd1dc11de4cfee421d`  
Verified on: Windows 11 Pro 23H2  