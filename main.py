from pathlib import Path

from omegaconf import DictConfig, OmegaConf

from src.pairs import get_pairs, run_labelme, merge_pair

# @hydra.main(version_base=None, config_path="configs", config_name="main.yaml")
def main(cfg: DictConfig):
    scene_path = Path(cfg.scene_path).resolve()
    output_path = Path(cfg.output_path).resolve()
    pair_file = Path(cfg.pair_path).resolve() / f'pairs-query-{cfg.retrieval_conf}{cfg.pair_num}.txt'
    pairs = get_pairs(str(pair_file))
    for k, vs in pairs.items():
        _k = scene_path / k
        for v in vs:
            _v = scene_path / v
            img_path = Path(merge_pair(_k, _v, output_path / 'temp'))
            run_labelme(img_path, output_path / f'annotations/{img_path.stem}.json', cfg.match_num)

if __name__ == "__main__":
    config = OmegaConf.load("configs/main.yaml")
    main(config)