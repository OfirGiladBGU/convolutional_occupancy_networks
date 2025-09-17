# Server Guide:

- Use server with GTX 1080
- then install the following libs:
```
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install torch-scatter==2.0.7 -f https://pytorch-geometric.com/whl/torch-1.7.1+cu101.html
```

---

# Files Setup:

- Use the copy script in `TreesAutoEncoder` (under: `datasets_visualize/copy_to_repo` dir) to create the dirs:
    - `parse_labels/originals`
    - `parse_preds_fixed/originals`
- Run the `organize_parse_data.py` to setup the files in the required formant for running `generate.py`
- Run the cli: `python generate.py configs/pointcloud_crop/parse.yaml` to get the model predictions.
- Copy the results to `TreesAutoEncoder` under: `datasets_visualize/conv_onet/data_input`:
    - Copy the `parse_labels` (as `labels`) and `parse_preds_fixed` (as `preds_fixed`).
    - Then copy from the `generation` folders the `input` and `meshes` folder to the same level as the `generation` folder.
    - Remove uncessary files:
        - All the contents in `vis` folders
        - The `pkl` files under the `generation` folder.
        - All the files in the `output` folder expect the `mesh_last_300.obj` files.
- [In `TreesAutoEncoder`] Run the `datasets_visualize/translate_and_voxelize.py` script for voxelization alignment.

---

The commands format in use:

```
python generate.py configs/pointcloud_crop/parse.yaml
```
<!-- python generate.py configs/pointcloud/parse.yaml -->