from typing import Optional

__all__ = ['__version__', 'debug', 'cuda', 'git_version', 'hip', 'xpu']
__version__ = '2.10.0a0+gite67e3d9'
debug = False
cuda: Optional[str] = '13.0'
git_version = 'e67e3d95f3ab863c8b44a6b16ce9f25d40b0d517'
hip: Optional[str] = None
xpu: Optional[str] = None
