# All of Food

A datapack for L’DieDiet 2.0.0, Minecraft 1.20.1 / Forge. **1091 registered food/drink IDs, 17 groups, six nutrition scales, achievements, and saved CCI.**

Matches the FreshCraft-Vanilla registry exported on October 10, 2026. Original categories/rewards are retained and membership is extended to the installed pack's full food catalog. Profiles for absent optional mod items are skipped.

## Installation

Put the ZIP in `<world>/datapacks`, then run `/reload` and `/ldiediet validate`. Do not unzip it. Install L’DieDiet on server and clients; the datapack belongs to the server world. Open the journal with N.

Install one variant: All of Food, All of Food Vanilla, or Original. They share `ldiediet` group/scale IDs and override one another. The generated packs' achievements use their own namespaces.

## Catalog and customization

`food-assignments.csv` lists every item, group, nutrition composition, CCI, and assignment reason. Categories may overlap. Classification is based on recipes, tags, and gameplay purpose, not a medical nutrition model. Edit individual entries in their JSON profiles/groups.

`coverage.json` summarizes item counts by group and fallback assignments. The catalog includes default-stack FoodProperties, EAT/DRINK items, and cake. Splash/lingering potions are excluded; individual NBT variants are not separate catalog IDs. Ordinary potions and non-nutritious special drinks are excluded from habituation.

`data/<item namespace>/food_profiles/*.json` defines composition and CCI. Explicit fields in `config/ldiediet/diet_config.json` win; old automatic cache values do not override explicit datapack CCI.

`data/ldiediet/food_groups/*.json` defines membership and rewards. Nutrition scales use non-overlapping tiers `[80,100)` and exactly 100, with the upper tier replacing the lower. `formulas.json` defines growth/recovery balance. Apply edits with `/reload`.

When your mod list changes, add new food profiles and group membership. These packs contain data, not third-party mod files or models. [Modpack Author Guide](https://github.com/lbdumbra-jpg/l-diediet/blob/main/README_MODPACK_AUTHORS.md). License: [MIT](LICENSE).

## Compatibility notes

The alpha LDelightfulCuisine writes its own profiles to the shared configuration at startup, including zero-nutrition settings for some drinks. These explicit entries override this datapack. Check them after startup if you need All of Food values. This project does not modify LDelightfulCuisine code or its original settings.

Validation may warn about original mutual reward dependencies: `sea_world`/`milk_detox` and `high_proof`/`fast_food`/`temple_body`. Those links are preserved. Independent slots can supply activation paths; a cycle warning does not mean the entire group is blocked.
