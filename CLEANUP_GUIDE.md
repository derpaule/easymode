# Minimal Reconstruction-Only Version

The `reconstruct-only` branch can be significantly reduced by removing code not needed for `easymode_reconstruct_only`.

## What's Required

**Keep:**
- `src/easymode/__init__.py`
- `src/easymode/core/__init__.py`
- `src/easymode/core/config.py`
- `src/easymode/core/warp_wrapper.py`
- `src/easymode/core/settings.txt`
- `src/easymode/easymode_reconstruct_only.py`
- `bin/easymode_reconstruct_only`
- `pyproject-reconstruct-only.toml` (or rename to `pyproject.toml`)
- `README.md`
- `LICENSE.txt`

## What Can Be Removed

**Directories to delete:**
```bash
rm -rf src/easymode/main.py      # Full CLI - not needed
rm -rf src/easymode/encoder/     # Encoding networks - not needed
rm -rf src/easymode/n2n/         # Denoising (noise2noise) - not needed
rm -rf src/easymode/segmentation/# Segmentation networks - not needed
rm -rf src/easymode/tiltfilter/  # Tilt filtering - not needed
rm -rf src/easymode/training/    # Training scripts - not needed
rm -rf docs/                      # Documentation - optional
rm -rf assets/                    # Assets - not needed
```

**Optional files to clean up:**
```bash
rm -f CITATION.cff               # Citation metadata - optional
rm -f mkdocs.yml                 # Doc site config - optional
```

## Minimal Config

Use `pyproject-reconstruct-only.toml` as `pyproject.toml` for a lean build:

```bash
# Rename for minimal config
mv pyproject-reconstruct-only.toml pyproject.toml
```

Or keep both and install with:
```bash
pip install -e . -c pyproject-reconstruct-only.toml
```

## Setup Steps

1. **Create conda env:**
```bash
conda create -n easymode_reconstruct_only python=3.10 -c conda-forge mrcfile tifffile numpy scipy psutil lxml tqdm -y
```

2. **Install package (optional):**
```bash
conda activate easymode_reconstruct_only
pip install -e .   # uses pyproject.toml
```

3. **Run:**
```bash
module load aretomo3
module load warp/
./bin/easymode_reconstruct_only --frames /path/frames --mdocs /path/mdocs
```

## Footprint Reduction

- **Current:** ~50+ files across segmentation, n2n, tiltfilter, training, encoder modules
- **Minimal:** ~12 files total (config + wrapper + entry point)
- **Size reduction:** ~80-90% code removal
