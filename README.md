# This is a fork of [mgflast/easymode](https://github.com/mgflast/easymode)

## Reconstruction only

This fork adds a lightweight reconstruction entry point that uses locally loaded Warp and AreTomo3 modules.
Had issues to install easymode with loaded Warp and AreTomo3 modules due to conflicting cuda versions.

See [CLEANUP_GUIDE.md](CLEANUP_GUIDE.md) for instructions on removing unused code and creating a minimal footprint version.

Created with Claude.

To install:

```
conda create -n easymode_reconstruct_only python==3.10 mrcfile tifffile numpy scipy psutil lxml tqdm -y 
conda activate easymode_reconstruct_only
conda activate easymode_reconstruct_only
conda install pip
pip install git+https://github.com/mgflast/easymode.git
```

Example:

```bash
module load aretomo3
module load warp/
easymode_reconstruct_only --frames /path/to/frames --mdocs /path/to/mdocs
```
