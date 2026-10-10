from pathlib import Path
import hashlib
import json
import math
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    'all-of-food': 'All-of-Food.zip',
    'all-of-food-vanilla': 'All-of-Food-Vanilla.zip',
    'ldiediet-original': 'LDieDiet-Original.zip',
}
IDENTIFIER = re.compile(r'^[a-z0-9_.-]+:[a-z0-9_./-]+$')

def validate(pack):
    metadata = json.loads((pack / 'pack.mcmeta').read_text(encoding='utf8'))
    assert metadata['pack']['pack_format'] == 15, pack
    assert 'MIT License' in (pack / 'LICENSE').read_text(encoding='utf8')
    for path in pack.rglob('*.json'):
        json.loads(path.read_text(encoding='utf8'), parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    groups = [json.loads(path.read_text(encoding='utf8')) for path in (pack / 'data/ldiediet/food_groups').glob('*.json')]
    for group in groups:
        assert isinstance(group['threshold'], int) and group['threshold'] > 0, group['name']
        assert group['flag'] in ['-c', '-o'], group['name']
        assert all(IDENTIFIER.fullmatch(item.lstrip('#')) for item in group['items']), group['name']
    if pack.name != 'ldiediet-original':
        members = {item for group in groups for item in group['items']}
        profiles = list((pack / 'data').glob('*/food_profiles/**/*.json'))
        coverage = json.loads((pack / 'coverage.json').read_text(encoding='utf8'))
        assert len(profiles) == coverage['foods_and_drinks']
        assert not coverage['unassigned']
        assert len(groups) == coverage['groups']
        for path in profiles:
            relative = path.relative_to(pack / 'data').parts
            item = relative[0] + ':' + '/'.join(relative[2:]).removesuffix('.json')
            assert item in members, 'Unassigned food: ' + item
            profile = json.loads(path.read_text(encoding='utf8'))
            assert math.isfinite(profile['cci']) and 1 <= profile['cci'] <= 4, item
            weights = profile['nutrients']
            assert all(math.isfinite(value) and value >= 0 for value in weights.values()), item
            assert not weights or abs(sum(weights.values()) - 1) < .00001, item
        for group in groups:
            namespace, path = group['advancement'].split(':')
            assert (pack / f'data/{namespace}/advancements/{path}.json').is_file(), group['name']
        for path in (pack / 'data/ldiediet/nutrition_scales').glob('*.json'):
            scale = json.loads(path.read_text(encoding='utf8'))
            assert scale['max_value'] == 100
            assert scale['thresholds'][0]['min'] == 80 and scale['thresholds'][0]['max'] == 100
            assert scale['thresholds'][0]['max_inclusive'] is False
            assert scale['thresholds'][1]['min'] == scale['thresholds'][1]['max'] == 100
    return {'groups': len(groups), 'files': len(list(pack.rglob('*.json')))}

def main():
    destination = ROOT / 'dist'
    destination.mkdir(exist_ok=True)
    result = {}
    hashes = {}
    for name, archive_name in PACKS.items():
        pack = ROOT / 'packs' / name
        result[name] = validate(pack)
        archive = destination / archive_name
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
            for path in sorted(pack.rglob('*')):
                if not path.is_file():
                    continue
                info = zipfile.ZipInfo(path.relative_to(pack).as_posix(), date_time=(2026, 10, 10, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                output.writestr(info, path.read_bytes())
        hashes[archive_name] = hashlib.sha256(archive.read_bytes()).hexdigest()
    (destination / 'SHA256.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf8')
    (destination / 'validation.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf8')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
