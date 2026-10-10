# L’DieDiet Datapacks

Standalone food catalogs, groups, nutrition scales, rewards, and achievements for [L’DieDiet 2.0.0](https://github.com/lbdumbra-jpg/l-diediet), Minecraft Java 1.20.1 / Forge.

[Download datapacks](https://github.com/lbdumbra-jpg/l-diediet-datapacks/releases/tag/v2.0.0) · [Download the mod](https://github.com/lbdumbra-jpg/l-diediet/releases/tag/v2.0.0) · [Author Guide](https://github.com/lbdumbra-jpg/l-diediet/blob/main/README_MODPACK_AUTHORS.md) · [Developer API](https://github.com/lbdumbra-jpg/l-diediet/blob/main/docs/INTEGRATION_API.md)

## Choose a pack

| Pack | Food/drink IDs | Groups | Scales | Intended use |
|---|---:|---:|---:|---|
| [All of Food](packs/all-of-food/README.md) | 1091 | 17 | 6 | FreshCraft's exported modded food catalog. |
| [All of Food Vanilla](packs/all-of-food-vanilla/README.md) | 43 | 11 | 6 | Vanilla food with L’DieDiet; no other mods required. |
| [LDieDiet Original](packs/ldiediet-original/README.md) | No standalone complete catalog | 17 | 6 | Preserved original rules and external dependencies. |

Install **one variant per world**. The packs share group and scale IDs. Put the release ZIP in `<world>/datapacks`, leave it zipped, then run `/reload` and `/ldiediet validate`. The mod is needed on server and clients; the datapack belongs to the world.

## Source layout

- `packs/`: editable pack source. Food profiles use each item's namespace; groups/scales use `ldiediet`.
- `schemas/`: JSON schemas for editor validation.
- `examples/`: opt-in authoring and integration examples, not automatically installed content.
- `tools/build.py`: validates source and creates reproducible ZIPs plus SHA-256 hashes in `dist`.

Run `python tools/build.py` with Python 3.9 or later. No extra Python packages are needed. Schema validation in an editor complements in-game validation; only the running mod set can confirm registry availability and reward reachability.

All of Food includes food and drinks from 50 mods plus vanilla Minecraft. See [Supported Food Sources](docs/SUPPORTED_MODS.md) for counts and `food-assignments.csv` for exact item IDs. Adding new mods requires extending source data; this is not an automatic catalog updater.

For modifications, follow the [Author Guide](https://github.com/lbdumbra-jpg/l-diediet/blob/main/README_MODPACK_AUTHORS.md). For script/mod integrations, see the [API Reference](https://github.com/lbdumbra-jpg/l-diediet/blob/main/docs/INTEGRATION_API.md). Report pack-data issues in this repository and mod behavior issues in the mod repository.

## License

The prepared datapack data is [MIT licensed](LICENSE). The packs do not redistribute third-party mod code, models, or textures.
