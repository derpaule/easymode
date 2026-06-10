# This is a fork of [mgflast/easymode](https://github.com/mgflast/easymode)

## Reconstruction only

This fork adds a lightweight reconstruction entry point that uses the locally loaded Warp and AreTomo3 modules.

Example:

```bash
module load aretomo3
module load warp/
easymode_reconstruct_only --frames /path/to/frames --mdocs /path/to/mdocs
```
