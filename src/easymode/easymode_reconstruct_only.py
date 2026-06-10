import argparse


def main():
    parser = argparse.ArgumentParser(description="easymode reconstruction-only wrapper using WarpTools and AreTomo3.")
    parser.add_argument('--frames', type=str, required=True, help="Directory containing raw frames.")
    parser.add_argument('--mdocs', type=str, required=True, help="Directory containing mdocs.")
    parser.add_argument('--apix', type=float, required=False, default=None, help="Pixel size of the frames in Angstrom. Leave empty to infer from mdoc.")
    parser.add_argument('--dose', type=float, required=False, default=None, help="Dose per frame in e-/A^2. Leave empty to infer from mdoc.")
    parser.add_argument('--extension', type=str, default=None, help="File extension of the frames (default: auto).")
    parser.add_argument('--tomo_apix', type=float, default=10.0, help="Pixel size of the tomogram in Angstrom (default: 10.0).")
    parser.add_argument('--thickness', type=float, default=3000.0, help="Thickness of the tomogram in Angstrom (default: 3000).")
    parser.add_argument('--shape', type=str, default=None, help="Frame shape (e.g. 4096x4096). If not provided, the shape is inferred from the data.")
    parser.add_argument('--steps', type=str, default='11111111', help="8-character string indicating which processing steps to perform.")
    parser.add_argument('--no_halfmaps', dest='halfmaps', action='store_false', help="If set, do not generate half-maps during motion correction or tomogram reconstruction.")
    parser.add_argument('--force_align', action='store_true', help="If set, force AreTomo3 alignment of tilt series even if alignment files are already present.")

    args = parser.parse_args()

    # Import reconstruct here to avoid importing heavy image libraries when showing --help
    from easymode.core.warp_wrapper import reconstruct

    reconstruct(frames=args.frames,
                mdocs=args.mdocs,
                apix=args.apix,
                dose=args.dose,
                extension=args.extension,
                tomo_apix=args.tomo_apix,
                thickness=args.thickness,
                shape=args.shape,
                steps=args.steps,
                halfmaps=args.halfmaps,
                force_align=args.force_align,
                warp_tools_cmd='WarpTools',
                aretomo3_cmd='AreTomo3',
                aretomo3_env='')


if __name__ == "__main__":
    main()
