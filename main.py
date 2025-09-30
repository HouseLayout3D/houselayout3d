from datasets import load_dataset_builder, load_dataset, get_dataset_config_names
ds_builder = load_dataset_builder("houselayout3d/HouseLayout3D", "doors")
configs = get_dataset_config_names("houselayout3d/HouseLayout3D")

datasets = {}
for config in configs:
  try:
    datasets[config] = load_dataset("houselayout3d/HouseLayout3D", config)
  except:
    print(f'skipping {config}')
