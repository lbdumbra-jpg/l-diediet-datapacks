# All of Food Vanilla

A datapack for L’DieDiet 2.0.0, Minecraft 1.20.1 / Forge. **43 vanilla food/drink IDs, 11 groups, six nutrition scales, achievements, and saved CCI.**

Requires only L’DieDiet. Groups without vanilla food are omitted; unique-food quotas are reduced to available membership. Third-party rewards are replaced with vanilla effects and external-mod conditions are removed.

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

Validation may warn about the preserved `sea_world`/`milk_detox` dependencies. The groups have independent slots whose activation was checked separately. Such a warning does not mean the whole group is blocked.
