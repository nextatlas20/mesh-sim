"""Entry point for MeshSim command-line use."""

from meshsim.pipeline import build_from_manifest, decimate, weld


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(prog="meshsimbuild")
    parser.add_argument("--from-manifest", required=True)
    parser.add_argument("--out", default="out")
    args = parser.parse_args(argv)

    result = build_from_manifest(args.from_manifest, out_dir=args.out)
    print(f"wrote {result.vertices} vertices to {result.out_dir}")
    return 0


__all__ = ["main", "build_from_manifest", "decimate", "weld"]
