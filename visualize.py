import pyviz3d as viz
import typer
import numpy as np
import json
import os
from typing import List


def load_json_annotations(path: str, filter: int = 0) -> List[dict]:
  """Loads the door annotations.

  A door consists of four vertices, and a normal indicating the direction of opening.

  Args:
      path (str): Path to the door annotations for a scene.

  Returns:
      []: List of doors. Each entry is a dict with keys {vertices, normal}.
      There are 4 vertices each consisting in  
  """
  try:
    with open(path, "r") as f:
      doors_data = json.load(f)
    if filter is not None:
      doors_list = doors_data[list(doors_data.keys())[filter]]
    else:
      doors_list = doors_data
  except:
    doors_list = []
  return doors_list


def load_mesh_filenames(path: str) -> List[str]:
  try:
    filenames = [f for f in os.listdir(path) if f.endswith('.ply') or f.endswith('.obj') ]
  except:
    filenames = []
  return filenames


def visualize_scene(scene_name: str = '1LXtFkjw3qL'):
  print(f"Showing {scene_name}")
  
  doors_list = load_json_annotations(f'data/doors/{scene_name}.json')
  windows_list = load_json_annotations(f'data/windows/{scene_name}.json')
  stairs_list = load_mesh_filenames(f'data/stairs/{scene_name}')
  structure_list = load_mesh_filenames(f'data/structures/layouts_split_by_entity/{scene_name}')
  poses_list = load_json_annotations(f'data/poses/{scene_name}.json', filter=1)

  v = viz.Visualizer()
  for i, door in enumerate(doors_list):
    points = np.array(door['vertices'])
    points = np.vstack([points, points[0]])
    color = np.array([191.0, 0.0, 0.0])
    v.add_polyline(f'doors;{i}', positions=points, edge_width=0.01, color=color)

  for i, window in enumerate(windows_list):
    points = np.array(window['vertices'])
    points = np.vstack([points, points[0]])
    color = np.array([0.0, 150.0, 242.0])
    v.add_polyline(f'windows;{i}', positions=points, edge_width=0.01, color=color)

  for i, stairs_filename in enumerate(sorted(stairs_list)):
    v.add_mesh(f'stairs;{i}', path=f'data/stairs/{scene_name}/{stairs_filename}')

  for i, structure_filename in enumerate(sorted(structure_list)):
    v.add_mesh(f'structure;{i}', path=f'data/structures/layouts_split_by_entity/{scene_name}/{structure_filename}')

  poses = []
  for i, pose in enumerate(poses_list):
    print(pose['file_path'])
    trafo = pose['transform_matrix']  # 4x4 pose matrix
    poses.append(np.array(trafo)[0:3, 3])

  # v.add_polyline('cam', positions=np.vstack(poses), edge_width=0.05)

  blender_config = viz.BlenderConfig(
      output_prefix=f'~/{scene_name}.png',
      blender_path='/Applications/Blender.app/Contents/MacOS/Blender')
  v.save(f'scene_{scene_name}', blender_config=blender_config)


def main():
  scene_names = [f[:-5] for f in os.listdir('data/doors')]
  for scene_name in scene_names:
    visualize_scene(scene_name)

if __name__ == "__main__":
  typer.run(main)