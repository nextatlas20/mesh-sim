# Manifest-driven rebuilds

Every MeshSim run writes a `manifest.json` next to its output directory. The manifest
records the input CAD hash, the solver version, the decimation budget and the ordering
seed. `meshsimbuild --from-manifest manifest.json` replays the run byte-for-byte on the
same solver version and fails loudly on any mismatch.

Manifests are append-only: a rebuilt run gets a new manifest that references its parent.
